numero=int(input("Digite um numero: "))
while numero<100:
    print("\t" + str(numero))
    numero=numero+1
print("Laço encerrado...")

tabuada=int(input("Digite um numero para exibir a tabuada"))
print("Tabuada do número ", tabuada)
for valor in range(1,11,1): #inicio + fim + incremento
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))