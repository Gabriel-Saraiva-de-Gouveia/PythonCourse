#base_dados = []
#with open("iris.data", "r") as arquivo:
#    for registro in arquivo.readlines():
#        base_dados.append(registro.split(","))

#print(base_dados)

#print(float(base_dados[0][0]) + float(base_dados[1][1]))
import json
dicionario = {
    "POTTER": ["HARRY POTTER", "14/10/2002", "HOGWARDS"],
    "HERMIONE": ["HERMIONE GRANGER", "22/07/2004", "ASKABAN"]
}
with open("base_dados1.json", "w") as arq_json:
    #print(dicionario)
    # for chave, dados in dicionario.itens():
    #     print(chave + " " + str(dados))
    json.dump(dicionario, arq_json)
