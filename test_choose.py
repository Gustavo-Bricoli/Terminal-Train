from Classes import animationCaller
import collections

counter = collections.Counter()
for _ in range(100000):
    func = animationCaller.AnimationCaller.choose_animation(foxy_prob=0.001)
    counter[func.__name__] += 1
print(counter)
