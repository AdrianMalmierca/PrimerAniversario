import math
import matplotlib.pyplot as plt
from flask import Flask, send_file

app = Flask(__name__)

def heart1(M):
    return 15 * math.sin(M) ** 3

def heart2(M):
    return 12 * math.cos(M) - 5 * math.cos(2 * M) - 2 * math.cos(3 * M) - math.cos(4 * M)

@app.route("/")
def generate_heart():
    M = [i * 0.1 for i in range(0, 628)]
    X = [heart1(m) for m in M]
    Y = [heart2(m) for m in M]

    plt.figure(figsize=(6, 6), facecolor="black")
    plt.plot(X, Y, "r")
    plt.axis("off")
    
    plt.savefig("heart.png", bbox_inches="tight", facecolor="black")
    plt.close()

    return send_file("heart.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
