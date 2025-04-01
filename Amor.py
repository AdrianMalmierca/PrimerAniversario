import math
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, Response
import io
import time

app = Flask(__name__)

# Definir las funciones de la forma del corazón
def heart1(M):
    return 15 * np.sin(M)**3

def heart2(M):
    return 12 * np.cos(M) - 5 * np.cos(2*M) - 2 * np.cos(3*M) - np.cos(4*M)

@app.route('/heart')
def generate_heart():
    M = np.linspace(0, 2 * np.pi, 1000)
    x = heart1(M)
    y = heart2(M)

    # Crear la figura y el gráfico
    plt.figure(figsize=(6, 6))
    plt.axis('equal')
    plt.gca().set_facecolor('black')
    plt.axis('off')

    # Preparamos el objeto BytesIO para enviar la imagen sin guardarla en disco
    img_io = io.BytesIO()

    # Inicia el streaming de la imagen
    def generate_frame():
        for i in range(1, len(M)):
            # Trazo actual: solo dibujar hasta el punto i
            plt.plot(x[:i], y[:i], color='red')
            plt.fill(x[:i], y[:i], color='red')

            # Guardamos la imagen en el objeto BytesIO
            img_io.seek(0)
            plt.savefig(img_io, format='png', dpi=300, bbox_inches='tight')
            img_io.seek(0)

            # Enviamos la imagen generada
            yield img_io.read()

            # Limpiar la figura para la siguiente iteración
            plt.clf()

            # Hacer una pausa para simular el dibujo (ajusta el tiempo si quieres que sea más rápido o lento)
            time.sleep(0.05)

    # Regresamos un StreamingResponse que irá enviando cada "frame"
    return Response(generate_frame(), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
