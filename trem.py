from estacao 

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
    
trem = Trem(a, estacoes)