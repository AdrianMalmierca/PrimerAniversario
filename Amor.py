import math
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, Response
import io

app = Flask(__name__)

# Definir las funciones de la forma del corazón
def heart1(M):
    return 15 * np.sin(M)**3

def heart2(M):
    return 12 * np.cos(M) - 5 * np.cos(2*M) - 2 * np.cos(3*M) - np.cos(4*M)

@app.route('/heart')
def generate_heart():
    # Generar los puntos del corazón
    M = np.linspace(0, 2 * np.pi, 1000)
    x = heart1(M)
    y = heart2(M)

    # Crear la figura y el gráfico
    plt.figure(figsize=(6,6))
    plt.plot(x, y, color='red')
    plt.fill(x, y, color='red')
    plt.axis('equal')
    plt.gca().set_facecolor('black')
    plt.axis('off')

    # Guardar la imagen en memoria
    img_io = io.BytesIO()
    plt.savefig(img_io, format='png', dpi=300, bbox_inches='tight')
    img_io.seek(0)
    plt.close()

    # Devolver la imagen generada como respuesta
    return Response(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
