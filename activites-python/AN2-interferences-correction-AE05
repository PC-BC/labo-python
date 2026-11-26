import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# PARAMÈTRES À MODIFIER
# ==========================================

y1max = 1.00   # amplitude de l'onde 1
y2max = 1.00   # amplitude de l'onde 2
T = 2.00       # période en secondes
phi = 0        # déphasage en radians

# ==========================================
# CALCULS
# ==========================================

t = np.linspace(0, 6, 500)

y1 = y1max * np.cos(2 * np.pi / T * t)          # onde 1
y2 = y2max * np.cos(2 * np.pi / T * t + phi)    # onde 2
y = y1 + y2                                     # onde résultante

# ==========================================
# AFFICHAGE
# ==========================================

plt.plot(t, y1, label="Onde 1") # légende onde 1
plt.plot(t, y2, label="Onde 2") # légende onde 2
plt.plot(t, y, label="Somme")   # somme : onde résultante

plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.title("Interférences de deux ondes")
plt.legend()
plt.grid()
plt.show()
