import matplotlib.pyplot as plt
from symbol import ScatterDataGenerator

sdg = ScatterDataGenerator()
dx, dy = sdg.get_data(['suicide', 'toi'])

plt.scatter(dx, dy)

plt.show()