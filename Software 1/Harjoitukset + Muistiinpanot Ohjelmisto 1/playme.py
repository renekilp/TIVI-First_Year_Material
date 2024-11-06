from flask import Flask, Response

app = Flask(__name__)


@app.route("/min/<a>/<b>/<c>/")
def find_min(a, b, c):
    #   k = min(a, b, c)
    luku1 = int(a)
    luku2 = int(b)
    luku3 = int(c)

    result = min(luku1, luku2, luku3)

    response = {
        "a": luku1,
        "b": luku2,
        "c": luku3,
        "min": result
    }
    return response


if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=5000)