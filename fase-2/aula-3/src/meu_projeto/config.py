# Estrutura recomendada para um projeto Python
"""
meu_projeto/
│
├── README.md              # Documentação do projeto
├── requirements.txt       # Dependências do projeto
├── setup.py              # Configuração para instalação
├── .gitignore            # Arquivos ignorados pelo Git
│
├── src/                  # Código fonte principal
│   └── meu_projeto/
│       ├── __init__.py
│       ├── main.py       # Ponto de entrada
│       ├── config.py     # Configurações
│       │
│       ├── models/       # Modelos de dados
│       │   ├── __init__.py
│       │   ├── usuario.py
│       │   └── produto.py
│       │
│       ├── utils/        # Utilitários
│       │   ├── __init__.py
│       │   ├── validacao.py
│       │   └── formatacao.py
│       │
│       └── services/     # Lógica de negócios
│           ├── __init__.py
│           ├── autenticacao.py
│           └── processamento.py
│
├── tests/                # Testes
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_utils.py
│   └── test_services.py
│
├── docs/                 # Documentação
│   └── guia_usuario.md
│
└── examples/            # Exemplos de uso
    └── exemplo_basico.py
"""

# arquivo: src/meu_projeto/config.py
"""Configurações centralizadas do projeto."""

import os
from pathlib import Path

# Diretórios base
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"

# Configurações da aplicação
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///local.db")

# Configurações de logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Criar diretórios necessários
for directory in [DATA_DIR, LOGS_DIR]:
    directory.mkdir(exist_ok=True)