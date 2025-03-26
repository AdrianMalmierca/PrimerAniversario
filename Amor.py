from flask import Flask, send_file
import matplotlib.pyplot as plt
import numpy as np
import math

app = Flask(__name__)

def calcular_puntos():
    x_vals = []
    y_vals = []
    
    def heart1(M):
        return 15 * math.sin(M)**3
    
    def heart2(M):
        return 12 * math.cos(M) - 5 * math.cos(2*M) - 2 * math.cos(3*M) - math.cos(4*M)
    
    for i in np.linspace(0, 2*np.pi, 500):
        x = heart1(i) * 18
        y = heart2(i) * 18
        x_vals.append(x)
        y_vals.append(y)
    
    return x_vals, y_vals

@app.route('/')
def generar_imagen():
    # Configurar el gráfico
    plt.figure(figsize=(10, 10))
    plt.style.use('dark_background')
    
    # Calcular y dibujar los puntos
    x, y = calcular_puntos()
    plt.plot(x, y, color='red', linewidth=2)
    
    # Ajustes estéticos
    plt.axis('equal')
    plt.axis('off')
    
    # Guardar y enviar la imagen
    plt.savefig('corazon.png', bbox_inches='tight', pad_inches=0)
    plt.close()
    return send_file('corazon.png', mimetype='image/png')

if __name__ == '__main__':
    app.run()
