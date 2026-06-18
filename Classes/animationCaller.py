import random
from Animacoes import terminalAnimation
from Animacoes.jumpscare import foxy

animacoes = [foxy(), terminalAnimation.terminalAnimation()]

class AnimationCaller:
    animacao = random.choice(animacoes)

    @staticmethod
    def callAnimation(animacao):
        animacao