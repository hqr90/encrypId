# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="encrypid",  # Nome do pacote no PyPI
    version="0.1.0",  # Versão inicial
    author="Hilton Queiroz Rebello",
    author_email="rebello.hiltonqueiroz@gmail.com",
    description="Uma ferramenta para encriptar e decriptar credenciais de forma segura.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hqr90/encrypid",  # URL do repositório
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "cryptography",
        "PyQt5",
        "click",
        "pyyaml",
        "python-dotenv",
    ],
    entry_points={
        'console_scripts': [
            'encrypid=encrypid.encrypid_cli:cli',
            'encrypid-gui=encrypid.encrypid_ui:main',  # Comando para a GUI
        ],
    },
)
