# encrypid.py

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
import yaml


class EncrypId:
    def __init__(self, password: str):
        """
        Inicializa o EncrypId com a senha fornecida.

        Parâmetros:
        - password (str): Senha para encriptar e decriptar os dados.
        """
        self.password = password

    def derive_key(self, salt: bytes) -> bytes:
        """
        Deriva uma chave criptográfica a partir de uma senha e um salt usando PBKDF2 HMAC SHA256.

        Parâmetros:
        - salt (bytes): Um salt aleatório.

        Retorna:
        - key (bytes): A chave derivada.
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # Fernet requer chaves de 32 bytes
            salt=salt,
            iterations=100_000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.password.encode()))
        return key

    def encrypt_data(self, data: bytes) -> bytes:
        """
        Encripta dados usando a senha fornecida.

        Parâmetros:
        - data (bytes): Dados a serem encriptados.

        Retorna:
        - encrypted (bytes): Dados encriptados (salt + encrypted).
        """
        salt = os.urandom(16)  # Gera um salt aleatório
        key = self.derive_key(salt)
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        # Armazena o salt + encrypted data
        return salt + encrypted

    def decrypt_data(self, encrypted_data: bytes) -> bytes:
        """
        Decripta dados encriptados usando a senha fornecida.

        Parâmetros:
        - encrypted_data (bytes): Dados encriptados (salt + encrypted).

        Retorna:
        - decrypted (bytes): Dados decriptados.
        """
        salt = encrypted_data[:16]  # Extrai os primeiros 16 bytes como salt
        encrypted = encrypted_data[16:]
        key = self.derive_key(salt)
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted)
        return decrypted

    def save_encrypted_credentials(self, credentials: dict, output_file: str):
        """
        Encripta as credenciais e salva em um arquivo.

        Parâmetros:
        - credentials (dict): Dicionário com as credenciais a serem encriptadas.
        - output_file (str): Caminho para o arquivo de saída encriptado.
        """
        # Converte o dicionário para bytes YAML
        data_bytes = yaml.dump(credentials).encode('utf-8')
        encrypted = self.encrypt_data(data_bytes)
        with open(output_file, 'wb') as f:
            f.write(encrypted)
        print(f"Credenciais encriptadas e salvas em: {output_file}")

    def load_encrypted_credentials(self, input_file: str) -> dict:
        """
        Carrega e decripta as credenciais de um arquivo encriptado.

        Parâmetros:
        - input_file (str): Caminho para o arquivo de entrada encriptado.

        Retorna:
        - credentials (dict): Dicionário com as credenciais decriptadas.
        """
        with open(input_file, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = self.decrypt_data(encrypted_data)
        credentials = yaml.safe_load(decrypted_data.decode('utf-8'))
        return credentials
