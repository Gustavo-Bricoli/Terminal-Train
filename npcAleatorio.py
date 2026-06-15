import random

class NPC:
    def __init__(self, nome, destino, origem):
        self.nome = nome
        self.destino = destino
        self.origem = origem

    def __repr__(self):
        return self.nome

def criar_npcs(estacoes):
    nomes = [
        "Joao",
        "Maria",
        "Clovis",
        "Ana",
        "Pedro",
        "Julia",
        "Carlos"
    ]
    
    npcs = []
    for i in range(10):
        nome = random.choice(nomes)
        origem = random.choice(estacoes)
        destino = random.choice(estacoes)
        while destino == origem:
            destino = random.choice(estacoes)
        npc = NPC(nome, destino, origem)
        origem.fila.append(npc)
        npcs.append(npc)
    return npcs