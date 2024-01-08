from Funções.FunctionsIdentification import *

minhaLista=[]
print("Preenchendo")
preencherInventario(minhaLista)
print("Exibindo")
exibirInventario(minhaLista)

print("Pesquisando")
localizarPorNome(minhaLista)
print("Alterando")
depreciarPorNome(minhaLista, 20)

print("Excluindo")
print(excluirPorSerial(minhaLista)) #somente esta função possuí retorno
exibirInventario(minhaLista)

print("Resumindo")
resumirValores(minhaLista)