#with open("teste.txt", "r") as arquivo:
#   conteudo = arquivo.read()

#with faz com que não seja necessário utilizar o método "close()
with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo. ")

with open("teste.txt", "a") as arquivo:
    arquivo.write("Continuação do texto. ")

    ##BACANA! :)
