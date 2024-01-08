nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
prioridade="NÃO"
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa?").upper()
"""if idade>=65:
    prioridade="SIM"
print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))"""
if idade>=65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")

elif doenca_infectocontagiosa=="SIM":
    print("O paciente " + nome + " deve ser direcionado para sala de espera reservada")

else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário!")