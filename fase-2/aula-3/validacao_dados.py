# arquivo: validacao_dados.py

# EXEMPLO DE ALTA COESÃO (BOM)
"""Módulo coeso focado apenas em validação de dados."""

import re
from datetime import datetime
from typing import Optional

class ValidadorDados:
    """Classe com alta coesão - todas as funções relacionadas à validação."""

    @staticmethod
    def validar_email(email: str) -> bool:
        """Valida formato de email."""
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(padrao, email))

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """Valida CPF brasileiro."""
        cpf = re.sub(r'[^0-9]', '', cpf)

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        # Validação do primeiro dígito
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = 11 - (soma % 11)
        digito1 = 0 if digito1 >= 10 else digito1

        if int(cpf[9]) != digito1:
            return False

        # Validação do segundo dígito
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = 11 - (soma % 11)
        digito2 = 0 if digito2 >= 10 else digito2

        return int(cpf[10]) == digito2

    @staticmethod
    def validar_data(data_str: str, formato: str = "%d/%m/%Y") -> bool:
        """Valida se uma string representa uma data válida."""
        try:
            datetime.strptime(data_str, formato)
            return True
        except ValueError:
            return False


# arquivo: servico_usuario.py

# EXEMPLO DE BAIXO ACOPLAMENTO (BOM)
"""Serviço com baixo acoplamento - depende de abstrações."""

from abc import ABC, abstractmethod
from typing import Dict, Optional

# Interface (abstração)
class RepositorioUsuario(ABC):
    @abstractmethod
    def buscar(self, id_usuario: int) -> Optional[Dict]:
        pass

    @abstractmethod
    def salvar(self, usuario: Dict) -> bool:
        pass

class ServicoUsuario:
    """Serviço com baixo acoplamento - depende da interface, não da implementação."""

    def __init__(self, repositorio: RepositorioUsuario):
        self.repositorio = repositorio  # Injeção de dependência

    def obter_usuario(self, id_usuario: int) -> Optional[Dict]:
        """Obtém usuário usando o repositório injetado."""
        return self.repositorio.buscar(id_usuario)

    def atualizar_usuario(self, id_usuario: int, dados: Dict) -> bool:
        """Atualiza usuário com validação."""
        usuario = self.repositorio.buscar(id_usuario)
        if not usuario:
            return False

        usuario.update(dados)
        return self.repositorio.salvar(usuario)
