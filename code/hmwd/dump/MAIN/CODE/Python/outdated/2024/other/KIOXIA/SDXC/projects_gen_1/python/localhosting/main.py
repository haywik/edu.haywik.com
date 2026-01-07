from flask import *

x = 0
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/more')
def more():
    return "More"


@app.route('/other')
def other():
    global x
    while True:
        x = int(x)
        x = x + 1
        x = str(x)
        return f"other {x}"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
