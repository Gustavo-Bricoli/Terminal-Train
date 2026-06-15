import random
from main import estacoes

nomes = [
    "Joao",
    "Maria",
    "Clovis",
    "Ana",
    "Pedro",
    "Julia",
    "Carlos"
]

nome = random.choice(nomes)
destino = random.choice(estacoes)

class NPC:
    def __init__(self, nome, destino):
        self.nome = nome
        self.destino = destino

    #usado para mostrar o nome do NPC no print(estacao.fila)
    
    def __repr__(self):
        return self.nome
    

#estacao inicial 