import matplotlib.pyplot as plt
import numpy as np

#déclaration des listes des mesures de P et V
volume = [0.0002, 0.0004, 0.0006, 0.0008, 0.001]
pression = [307000, 150000, 101700, 75800, 61000]
temperature = [300, 280, 260, 240, 225]

V = np.array(volume)
P = np.array(pression)
T = np.array(temperature)

n = (P*V)/(8.31*T)

# Affichage du graphique
plt.xlabel('T (en K)')
plt.ylabel('n (en mol)')
plt.title("Quantité de matière n en fonction de T")
plt.grid()
plt.plot(T, n,'bx')
plt.show()
