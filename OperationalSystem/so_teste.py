import platform
import getpass
from datetime import datetime

# print("Nome maquina:..........", platform.node())
# print("Arquitetura:..........", platform.architecture())
# print("Sistema Operacional:..........", platform.system())
# print("Versao do SO:..........", platform.release())
# print("Processador:..........", platform.processor())
# print("Versao do Python:..........", platform.python_version())
#
# print(datetime.now())

usuario = (getpass.getuser()) #usuário da maquina
senha = (getpass.getpass("Digite sua senha:...")) # modo password

if usuario == 'casa' and senha == 'Bitch_okay':
    print("Bem-Vinda Rihana The Queen")
else:
    print("Get the fuck out here!! (read as Nick Minaj voice)")