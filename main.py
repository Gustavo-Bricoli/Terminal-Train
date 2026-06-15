from npcAleatorio import npc

#classes
class Estacao:
    def __init__(self, nome):
        self.nome = nome
        self.fila = []
    def __repr__(self):
        return self.nome    
    
class Trem:
    def __init__(self, estacao_atual, estacoes):
        self.estacoes = estacoes
        self.indice_atual = 0
        self.passageiros = []

    def embarcar(self, npc):
        self.passageiros.append(npc)
    def desembarcar(self, npc):
        #for passageiro in self.passageiros[:]:
        if npc.destino == self.estacao_atual():
            self.passageiros.remove(npc)
            print(f"{npc.nome} desembarcou em {self.estacao_atual().nome}")
    def proxima_estacao(self):
        self.indice_atual = (self.indice_atual + 1) % len(self.estacoes)

    def processar_estacao(self):
        estacao = self.estacao_atual()
        for passageiro in self.passageiros[:]:
            self.desembarcar(passageiro)
        while len(estacao.fila) > 0:
            npc = estacao.fila.pop(0)
            self.embarcar(npc)
            print(f"{npc.nome} embarcou em {estacao.nome}")
        
    def estacao_atual(self):
        return self.estacoes[self.indice_atual]


#criacao dos objetos
a = Estacao("A")
b = Estacao("B")
c = Estacao("C")
d = Estacao("D")
estacoes = [a,b,c,d]
trem = Trem(a, estacoes)

#adicionando os npcs as filas das estacoes
'''a.fila.append(joao)
b.fila.append(maria)
c.fila.append(clovis)
d.fila.append(fulano)'''

#testando
for estacao in estacoes:
    print(estacao.nome, estacao.fila)

#faz o trem dar 2 voltas
for _ in range(8):
    print(f"\nEstação {trem.estacao_atual()}")
    trem.processar_estacao()
    print("Passageiros:", trem.passageiros)
    trem.proxima_estacao()

#testando se funfou
print(f"Passageiros no trem: {trem.passageiros}")
