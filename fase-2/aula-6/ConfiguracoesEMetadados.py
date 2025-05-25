# Armazenando configurações
config = {
    "debug": True,
    "max_usuarios": 100,
    "servidor": "localhost",
    "porta": 8080
}

# Usando as configurações
if config["debug"]:
    print("Modo debug ativado")
