
import numpy as np
import matplotlib.pyplot as plt

# Donnees experimentales eau-methanol a environ 1 atm
T_data = np.array([
    100, 98.4, 96.9, 95.8, 95.1, 94.1, 92.2, 90,
    88.6, 86.9, 85.4, 83.4, 82, 79.1, 78.1, 76.5,
    75.3, 74.2, 73.2, 72, 70.9, 69.2, 68.1, 67.2,
    66.9, 65.7, 65
])

x_data = np.array([
    0, .012, .020, .026, .033, .036, .053, .074,
    .087, .108, .129, .164, .191, .268, .294, .352,
    .402, .454, .502, .563, .624, .717, .790, .843,
    .857, .938, 1
])

y_data = np.array([
    0, .068, .121, .159, .188, .215, .275, .356,
    .395, .440, .488, .537, .572, .648, .666, .704,
    .734, .760, .785, .812, .835, .877, .910, .930,
    .939, .971, 1
])

# Donnees du melange
F = 60               # mol/h
z = 0.40             # fraction molaire methanol
T = 80               # temperature en degres C

# Interpolation a 80 degres C
indices = np.argsort(T_data)
x = np.interp(T, T_data[indices], x_data[indices])
y = np.interp(T, T_data[indices], y_data[indices])

# Fraction molaire d'eau
x_eau = 1 - x
y_eau = 1 - y

# Regle du levier : fraction vaporisee
beta = (z - x) / (y - x)

# Debits molaires des phases
V = beta * F
L = (1 - beta) * F

print("A 80 degres C et 1 atm :")
print(f"x methanol liquide = {x:.3f}")
print(f"x eau liquide = {x_eau:.3f}")
print(f"y methanol vapeur = {y:.3f}")
print(f"y eau vapeur = {y_eau:.3f}")
print(f"Debit liquide L = {L:.2f} mol/h")
print(f"Debit vapeur V = {V:.2f} mol/h")

# Diagramme 1 : diagramme T-x-y
plt.figure(figsize=(8, 5))
plt.plot(x_data, T_data, "o-", label="Courbe bulle (liquide)")
plt.plot(y_data, T_data, "s-", label="Courbe rosee (vapeur)")
plt.scatter(x, T, label="Liquide a 80 C")
plt.scatter(y, T, label="Vapeur a 80 C")
plt.axhline(T, linestyle="--")
plt.xlabel("Fraction molaire en methanol")
plt.ylabel("Temperature (°C)")
plt.title("Diagramme T-x-y eau-methanol a 1 atm")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Diagramme 2 : diagramme d'equilibre y-x
plt.figure(figsize=(7, 5))
plt.plot(x_data, y_data, "o-", label="Equilibre liquide-vapeur")
plt.plot([0, 1], [0, 1], "--", label="Diagonale y = x")
plt.scatter(x, y, label="Equilibre a 80 C")
plt.xlabel("x methanol dans le liquide")
plt.ylabel("y methanol dans la vapeur")
plt.title("Diagramme binaire molaire eau-methanol")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
