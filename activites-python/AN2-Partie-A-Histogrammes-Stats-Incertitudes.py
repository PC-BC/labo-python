import numpy as np
import matplotlib.pyplot as plt

pH1 = [] # A completer avec les mesures du papier pH
pH2 = [] # A completer avec les mesures du pH-metre

plt.hist(pH1, 10, label='Mesures au papier pH')
plt.hist(pH2, 10, label='Mesures au pH-metre')
plt.xlabel("Mesures de pH")
plt.ylabel("Nombre de mesures")
plt.title("Histogramme de la serie de mesures")
plt.legend()
plt.show()
