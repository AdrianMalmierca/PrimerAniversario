import math
import time
from flask import Flask, Response, send_file

app = Flask(__name__)

def heart1(M):
    return 15 * math.sin(M) ** 3

def heart2(M):
    return 12 * math.cos(M) - 5 * math.cos(2 * M) - 2 * math.cos(3 * M) - math.cos(4 * M)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stream")
def stream():
    def generate():
        for i in range(500):
            x = heart1(i * 0.05) * 18
            y = heart2(i * 0.05) * 18
            yield f"{x},{y}\n"
            time.sleep(0.02)  # Simula la animación con pausas
    return Response(generate(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True)
