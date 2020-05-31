import matplotlib.pyplot as plt
from symbol import ScatterDataGenerator

sdg = ScatterDataGenerator()
dx, dy = sdg.get_data('su')

plt.scatter(dx, dy)

plt.show()