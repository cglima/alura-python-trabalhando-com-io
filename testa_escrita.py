arquivo_contatos = open("dados/contatos-escrita.csv", encoding="latin_1", mode="w")
contato = "11,Carol,carol@carol.com.br\n"
arquivo_contatos.write(contato)
