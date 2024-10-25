Claro! Aqui está um exemplo de como você pode solicitar os dados do usuário e armazená-los em um dicionário:

python
Copiar código
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
Se você quiser executar esse código, ele irá pedir para você inserir o nome e o telefone de três pessoas e, em seguida, exibirá o dicionário com os dados armazenados.
