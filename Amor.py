import math
import matplotlib.pyplot as plt
import numpy as np

# Definir las funciones de la forma del corazón
def heart1(M):
    return 15 * np.sin(M)**3

def heart2(M):
    return 12 * np.cos(M) - 5 * np.cos(2*M) - 2 * np.cos(3*M) - np.cos(4*M)

# Generar los puntos del corazón
M = np.linspace(0, 2 * np.pi, 1000)
x = heart1(M)
y = heart2(M)

# Crear la figura
plt.figure(figsize=(6,6))
plt.plot(x, y, color='red')
plt.fill(x, y, color='red')
plt.axis('equal')
plt.gca().set_facecolor('black')
plt.axis('off')

# Guardar la imagen
plt.savefig('/path/to/your/project/heart.png', dpi=300, bbox_inches='tight')
plt.close()
