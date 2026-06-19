from Sistemas.animationSelector import choose_animation
class AnimationCaller:
    @staticmethod
    def callAnimation(animacao=None, *, override_weights: dict | None = None):
        if animacao is not None:
            func = animacao
        else:
            func = choose_animation(override_weights)

        return func()
