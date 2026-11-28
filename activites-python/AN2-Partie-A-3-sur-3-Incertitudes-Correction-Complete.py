import numpy as np
import matplotlib.pyplot as plt
from math import *

pH1 = [7,7,8,7,7,6,7,7,7,6,7,7,8,7]
pH2 = [7.32,7.12,7.29,6.9,7.36,6.95,7.13,7.36,7.34,7.09,7.02,7.19,7.18,7.35]

plt.hist(pH1, 10, label='Mesures au papier pH')
plt.hist(pH2, 10, label='Mesures au pH-metre')
plt.xlabel("Mesures de pH")
plt.ylabel("Nombre de mesures")
plt.title("Histogramme de la série de mesures")
plt.legend()
plt.show()

# Calcul des moyennes et écart-types
pH1moyen = np.mean(pH1)
pH2moyen = np.mean(pH2)
pH1ecarttype = np.std(pH1, ddof=1)
pH2ecarttype = np.std(pH2, ddof=1)
print(pH1moyen, pH2moyen, pH1ecarttype, pH2ecarttype) # affichage

# Calcul des incertitudes-types
u_pH1 = pH1ecarttype / sqrt(14)
u_pH2 = pH2ecarttype / sqrt(14)
print("u_pH1=",u_pH1, "u_pH2=",u_pH2)   # affichage
