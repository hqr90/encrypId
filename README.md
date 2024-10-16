# EncrypId 🛡️🔐

**EncrypId** é uma ferramenta poderosa e intuitiva desenvolvida em Python para encriptar e decriptar suas credenciais sensíveis de forma segura. Com uma interface de linha de comando (CLI) robusta e uma interface gráfica amigável (GUI) construída com PyQt5, EncrypId garante que suas informações confidenciais estejam sempre protegidas contra acessos não autorizados.

![EncrypId Banner](banner.png)

---

## 📚 Índice

- [Por que EncrypId?](#por-que-encrypid)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
  - [Instalação via `pip`](#instalação-via-pip)
  - [Interface de Linha de Comando (CLI)](#interface-de-linha-de-comando-cli)
  - [Interface Gráfica (GUI)](#interface-gráfica-gui)
- [Exemplos de Uso](#exemplos-de-uso)
- [Boas Práticas de Segurança](#boas-práticas-de-segurança)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## Por que EncrypId?

Em um mundo cada vez mais digital, proteger informações sensíveis é essencial. Seja para armazenar credenciais de acesso a serviços como Firebase, GPT ou outras APIs, garantir que esses dados estejam seguros evita riscos de segurança e acessos indesejados. EncrypId oferece uma solução simples e eficaz para gerenciar suas credenciais com segurança máxima.

---

## Funcionalidades

- **Encriptação de Credenciais:** Converta seus arquivos YAML contendo credenciais em arquivos binários encriptados.
- **Decriptação de Credenciais:** Recupere suas credenciais de arquivos encriptados de forma segura.
- **Interface de Linha de Comando (CLI):** Execute operações de encriptação e decriptação diretamente pelo terminal.
- **Interface Gráfica (GUI):** Utilize uma interface amigável para gerenciar suas credenciais sem a necessidade de comandos.
- **Gestão de Senhas Segura:** Utilize senhas fortes para proteger suas credenciais e evite armazená-las diretamente no código.

---

## Tecnologias Utilizadas

- **Python 3.8+**
- **PyQt5:** Para a construção da interface gráfica.
- **Click:** Para a criação da interface de linha de comando.
- **Cryptography:** Biblioteca robusta para operações de criptografia.
- **PyYAML:** Para manipulação de arquivos YAML.
- **Python-dotenv:** Para gerenciamento de variáveis de ambiente.

---

## Estrutura do Projeto

```
encrypid/
├── encrypid/
│   ├── __init__.py            # Inicializa o pacote EncrypId
│   ├── encrypid.py            # Classe principal para encriptação e decriptação
│   └── encrypid_ui.py         # Interface gráfica com PyQt5
├── tests/
│   ├── __init__.py
│   └── test_encrypid.py
├── LICENSE
├── README.md
├── setup.py
├── pyproject.toml
├── requirements.txt
└── MANIFEST.in
```

---

## Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/hqr90/encrypid.git
cd encrypid
```

### 2. Criar um Ambiente Virtual (Recomendado)

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4. Publicar no PyPI (Opcional)

Para tornar o EncrypId instalável via `pip`, você pode publicar o pacote no [PyPI](https://pypi.org/). Siga os passos descritos na seção [Tornar o EncrypId Instalável via `pip`](#como-usar).

---

## Como Usar

EncrypId está disponível tanto via **CLI** quanto via **GUI**. Além disso, você pode instalar o EncrypId diretamente via `pip` para facilitar o uso.

### Instalação via `pip`

Após publicar no PyPI, instale o EncrypId usando:

```bash
pip install encrypid
```

### Interface de Linha de Comando (CLI)

A CLI permite que você encripte e decripte suas credenciais diretamente pelo terminal.

#### 🔒 Encriptar Credenciais

```bash
encrypid encrypt -i caminho/para/credentials.yaml -o caminho/para/credentials_encrypted.bin
```

**Parâmetros:**
- `-i`, `--input-file`: Caminho para o arquivo YAML de credenciais a ser encriptado.
- `-o`, `--output-file`: Caminho para salvar o arquivo encriptado.

**Exemplo:**

```bash
encrypid encrypt -i credentials.yaml -o credentials_encrypted.bin
```

Será solicitado que você insira uma senha segura para encriptar as credenciais.

#### 🔓 Decriptar Credenciais

```bash
encrypid decrypt -i caminho/para/credentials_encrypted.bin -o caminho/para/decrypted_credentials.yaml
```

**Parâmetros:**
- `-i`, `--input-file`: Caminho para o arquivo encriptado a ser decriptado.
- `-o`, `--output-file`: (Opcional) Caminho para salvar o arquivo YAML de saída. Se omitido, as credenciais serão exibidas no terminal.

**Exemplo:**

```bash
encrypid decrypt -i credentials_encrypted.bin -o decrypted_credentials.yaml
```

Ou para exibir no terminal:

```bash
encrypid decrypt -i credentials_encrypted.bin
```

#### 🔑 Gerar Chave (Opcional)

```bash
encrypid generate_key
```

Este comando serve para verificar se a senha está funcionando corretamente, embora a geração de chave seja gerenciada internamente.

### Interface Gráfica (GUI)

A GUI proporciona uma experiência visual para gerenciar suas credenciais sem a necessidade de comandos.

#### 🔧 Executar a GUI

Após a instalação via `pip`, inicie a GUI usando:

```bash
encrypid-gui
```

**Funcionalidades Disponíveis:**

- **Encriptar Credenciais:**
  - Selecione o arquivo YAML de entrada.
  - Escolha onde salvar o arquivo encriptado.
  - Insira e confirme a senha.
  - Clique em "Encriptar" para processar.

- **Decriptar Credenciais:**
  - Selecione o arquivo encriptado.
  - (Opcional) Escolha onde salvar o arquivo YAML de saída.
  - Insira a senha.
  - Clique em "Decriptar" para processar.

- **Logs e Mensagens de Status:**
  - Área dedicada para exibir mensagens de sucesso, erros e logs de operações.

#### 📸 Tela Inicial da GUI

![EncrypId GUI](screenshot.png)

---

## Exemplos de Uso

### 1. Encriptando Credenciais via CLI

```bash
encrypid encrypt -i credentials.yaml -o credentials_encrypted.bin
```

**Passo a Passo:**

1. Execute o comando acima no terminal.
2. Insira e confirme a senha quando solicitado.
3. O arquivo `credentials_encrypted.bin` será criado com suas credenciais encriptadas.

### 2. Decriptando Credenciais via CLI

```bash
encrypid decrypt -i credentials_encrypted.bin -o decrypted_credentials.yaml
```

**Passo a Passo:**

1. Execute o comando acima no terminal.
2. Insira a senha utilizada na encriptação.
3. O arquivo `decrypted_credentials.yaml` será criado com suas credenciais decriptadas.

### 3. Utilizando a GUI

1. Execute o comando da GUI:

   ```bash
   encrypid-gui
   ```

2. Na seção de encriptação:
   - Clique em "Selecionar Arquivo" para escolher `credentials.yaml`.
   - Clique em "Selecionar Destino" para definir onde salvar `credentials_encrypted.bin`.
   - Insira e confirme a senha.
   - Clique em "Encriptar".

3. Na seção de decriptação:
   - Clique em "Selecionar Arquivo" para escolher `credentials_encrypted.bin`.
   - (Opcional) Clique em "Selecionar Destino" para definir onde salvar `decrypted_credentials.yaml`.
   - Insira a senha.
   - Clique em "Decriptar".

---

## Boas Práticas de Segurança

1. **Proteja Seus Arquivos Encriptados:**
   - Adicione `credentials_encrypted.bin` e `.env` ao seu `.gitignore` para evitar que sejam versionados.
   
     ```gitignore
     # .gitignore
     credentials_encrypted.bin
     .env
     ```

2. **Gerencie as Permissões dos Arquivos:**
   - Restrinja as permissões para que apenas o usuário atual possa ler e escrever os arquivos sensíveis.
   
     ```bash
     chmod 600 credentials_encrypted.bin
     chmod 600 .env
     ```

3. **Armazene a Senha com Segurança:**
   - Utilize ferramentas de gerenciamento de segredos, como **AWS Secrets Manager**, **Azure Key Vault**, ou **HashiCorp Vault**, para armazenar e gerenciar suas senhas de forma segura.

4. **Rotação de Senhas:**
   - Periodicamente, altere a senha utilizada para encriptar as credenciais e regenere o arquivo encriptado para manter a segurança.

5. **Auditoria e Monitoramento:**
   - Monitore acessos aos arquivos de credenciais e às variáveis de ambiente para detectar quaisquer acessos não autorizados.

6. **Evite Expor Senhas em Logs:**
   - Assegure-se de que senhas ou dados sensíveis não sejam registrados em logs ou exibidos no terminal inadvertidamente.

---

## Contribuição

Contribuições são bem-vindas! Se você deseja melhorar o EncrypId, siga os passos abaixo:

1. **Fork este repositório.**
2. **Crie uma branch para sua feature:**

   ```bash
   git checkout -b feature/nova-feature
   ```

3. **Commit suas mudanças:**

   ```bash
   git commit -m "Adiciona nova feature"
   ```

4. **Push para a branch:**

   ```bash
   git push origin feature/nova-feature
   ```

5. **Abra um Pull Request.**

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENCE).

---

### Contato

Para dúvidas, sugestões ou contribuições, entre em contato:

- **Email:** rebello.hiltonqueiroz@gmail.com
- **LinkedIn:** [hqr90](https://www.linkedin.com/in/hqr90/)
- **GitHub:** [hqr90](https://github.com/hqr90)

---

✨ **Proteja suas credenciais com EncrypId e garanta a segurança dos seus dados!** ✨
