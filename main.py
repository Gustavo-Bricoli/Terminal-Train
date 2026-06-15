from npcAleatorio import npc

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
