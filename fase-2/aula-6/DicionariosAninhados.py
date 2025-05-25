# Informações de empresa
empresa = {
    "nome": "Tech Corp",
    "departamentos": {
        "TI": {"funcionarios": 10, "orcamento": 50000},
        "RH": {"funcionarios": 5, "orcamento": 30000}
    }
}

# Acessando dados aninhados
print(empresa["departamentos"]["TI"]["funcionarios"])  # 10
