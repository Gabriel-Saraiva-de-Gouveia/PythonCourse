#arquivo = open("primeiro_arquivo.txt", "w")
#arquivo.write("Saraiva não aguenta mais ")
#arquivo.close() #fechar, pois, caso não fechá-lo, não será mais possível abri-lo
#with open("primeiro_arquivo.txt", "w") as arquivo:
#   arquivo.write("\nAvada Kedrava")

with open("primeiro_arquivo.txt", "r") as arquivo:
    for linha in arquivo.readline():
        print(linha)