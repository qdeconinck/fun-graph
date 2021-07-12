import matplotlib.pyplot as plt
import random
from symbol import ScatterDataGenerator

sdg = ScatterDataGenerator()
dx, dy = sdg.get_data(['suis-je un beau', 'graphe pour ta', 'these ?'])

dx = [x + random.uniform(-0.02, 0.02) for x in dx]
dy = [y + random.uniform(-0.02, 0.02) for y in dy]

min_dx = min(dx)
max_dx = max(dx)
min_dy = min(dy)
max_dy = max(dy)

for _ in range(5000):
    dx.append(random.uniform(min_dx, max_dx))
    dy.append(random.uniform(min_dy, max_dy))

plt.scatter(dx, dy)

plt.show()