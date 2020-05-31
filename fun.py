import matplotlib.pyplot as plt
import random
from symbol import ScatterDataGenerator

sdg = ScatterDataGenerator()
dx, dy = sdg.get_data(['suicide', 'toi'])

dx = [x + random.uniform(-0.02, 0.02) for x in dx]
dy = [y + random.uniform(-0.02, 0.02) for y in dy]

for _ in range(1000):
    dx.append(random.uniform(min(dx), max(dx)))
    dy.append(random.uniform(min(dy), max(dy)))

plt.scatter(dx, dy)

plt.show()