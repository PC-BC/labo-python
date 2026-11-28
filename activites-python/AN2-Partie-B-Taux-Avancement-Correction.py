from math import *
print("Saisir la valeur de la concentration :")
C = float(input("C = "))    # saisir la concentration molaire C
while C <= 0: # On vérifie que c est strictement positif
    print ("C doit être strictement positif")
    C = float(input("C = "))    # On demande à nouveau la valeur de c.
KA = float(input("KA = "))  # On demande la valeur de la constante d’acidité KA du couple acide-base.
while KA <= 0: # On vérifie que KA est strictement positif
    print ("KA doit être strictement positif")
    KA = float(input("KA = "))    # On demande à nouveau la valeur de KA.
delta = KA**2 + 4*C*KA    # On calcule le discriminant delta, forcément positif car c et KA positifs. L'équation a donc deux solutions dont une seule positive que l'on retient.

# ligne suivante à compléter :
tau = (-KA + sqrt(delta)) /(2*C)

print("Le taux d'avancement est tau = ")
print(tau)
