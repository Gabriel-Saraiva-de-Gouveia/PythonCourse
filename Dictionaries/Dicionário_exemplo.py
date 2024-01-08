usuarios = []
print(usuarios)

usuarios = {"harry" : ["Harry o Potter", "24/12/2017", "grifindor_01"],
            "hermione" : ["Hermione Granger", "22/01/2019", "grifindor_02"]}
print(usuarios)

usuarios["black"] = ["Sirius Black", "24/12/2017", "grifindor_04"]
print(usuarios)

print("####----####")
print(usuarios.get("hermione"))

# base de manipulação de um dicionário. Pesquisar mais operações...