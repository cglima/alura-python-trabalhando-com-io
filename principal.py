arquivo_contatos = open('dados/contatos.csv')

for linha in arquivo_contatos:
    print(linha, end="")