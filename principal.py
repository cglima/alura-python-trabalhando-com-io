import contatos_utils
try:
    # contatos = contatos_utils.csv_para_contatos("dados/contatos.csv")
    # contatos_utils.contatos_para_pickle(contatos, 'dados/contato.pickle')
    contatos = contatos_utils.pickle_para_contatos('dados/contato.pickle')

    for contato in contatos:
        print(f"{contato.id} - {contato.nome} - {contato.email}")
except FileNotFoundError:
    print("Arquivo não encontrado")
except PermissionError:
    print("Sem permissão para escrita")