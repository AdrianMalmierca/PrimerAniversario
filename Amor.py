from flask import Flask, send_file
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

def generar_corazon():
    # Generar puntos para el corazón
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    
    # Crear la figura
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, color="red")
    plt.axis("equal")
    plt.axis("off")
    
    # Guardar la imagen
    plt.savefig("corazon.png", bbox_inches="tight", pad_inches=0)
    plt.close()

@app.route("/")
def mostrar_corazon():
    # Generar el corazón si no existe
    generar_corazon()
    return send_file("corazon.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
