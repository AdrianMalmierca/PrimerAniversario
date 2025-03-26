import math
import time
from flask import Flask, Response, send_from_directory
from gevent.pywsgi import WSGIServer  # 🟢 Permite mejor manejo de streaming en Vercel
from gevent import monkey

monkey.patch_all()  # 🔄 Parchea la ejecución para ser no bloqueante

app = Flask(__name__)

def heart1(M):
    return 15 * math.sin(M) ** 3

def heart2(M):
    return 12 * math.cos(M) - 5 * math.cos(2 * M) - 2 * math.cos(3 * M) - math.cos(4 * M)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")  # "." indica el mismo directorio

@app.route("/stream")
def stream():
    def generate():
        for i in range(500):
            x = heart1(i * 0.05) * 18
            y = heart2(i * 0.05) * 18
            print(f"Enviando: {x},{y}")  # 👀 Verifica que se están enviando datos
            yield f"{x},{y}\n"
            time.sleep(0.02)  # 🔄 Ahora es manejado mejor con gevent

    return Response(generate(), mimetype="text/plain")

if __name__ == "__main__":
    http_server = WSGIServer(("0.0.0.0", 5000), app)
    http_server.serve_forever()
