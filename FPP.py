import numpy as np
import matplotlib.pyplot as plt


def fpp(portofino, sf90):

    x, y = [portofino, 0], [0, sf90]

    plt.plot(x, y, linewidth=3)

    plt.xlabel('Modelo Portofino')
    plt.ylabel('Modelo SF90')
    plt.title('FPP - Ferrari')

    plt.show()

fpp(1135, 499)
