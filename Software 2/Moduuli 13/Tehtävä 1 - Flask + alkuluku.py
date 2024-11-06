from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/alkuluku/<luku>')
def primenum(luku):
    try:
        num = int(luku)
        prime = None
        if luku < 2:
            prime = False
        else:
            prime = True
            for i in range(2, int(luku / 2) + 1):
                if luku % i == 0:
                    prime = False
                    break
        status = 200
        response = {"Number": num, "Prime": prime}

    except ValueError:
        status = 400
        response = {"Status": status, "Message": "Virhe luku-syötteessä!"}

    json_vast = json.dumps(response)
    return Response(response=json_vast, status=status, mimetype='application/json')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


