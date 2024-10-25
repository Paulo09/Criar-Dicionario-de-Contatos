# Inicializa um dicionário vazio
contatos = {}

# Solicita os dados de 3 pessoas
for i in range(3):
    nome = input("Insira o nome da pessoa: ")
    telefone = input("Insira o número de telefone: ")
    contatos[nome] = telefone

# Exibe o dicionário preenchido
print("\nDicionário de Contatos:")
print(contatos)
