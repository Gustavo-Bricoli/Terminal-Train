import sys
import os

# O método resource_path() é usado para localizar arquivos de recursos
# (como sons e animações) tanto quando o projeto é executado com
# "python main.py" quanto quando é empacotado com PyInstaller.
#
# Quando o programa é empacotado com PyInstaller em modo onefile,
# os arquivos extras são extraídos para uma pasta temporária e o
# PyInstaller define a variável sys._MEIPASS para indicar esse local.
# Nesse caso, usamos sys._MEIPASS como base para construir o caminho.
# Isso é só para animações e áudios que dependem de uma file que está em outro lugar 
# além do arquivo em que tem sua funcao. Por isso precisa disso no skeleton e no jumpscare, mas não no terminalTrem
# já que o texto usado para a animacao do trem ja esta no proprio arquivo em que tem sua funcao de chamado e retorno da animacao
#
# Quando o programa roda normalmente no Python, usamos o diretório
# atual do projeto (os.path.abspath('.')) como base.
#
# Exemplo de uso:
#   from utils import resource_path
#   arquivo = resource_path('Sons/mp3/foxyrun.mp3')
#   with open(arquivo, 'rb') as f:
#       ...

def resource_path(relative_path: str) -> str:
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')

    return os.path.abspath(os.path.join(base_path, relative_path))
