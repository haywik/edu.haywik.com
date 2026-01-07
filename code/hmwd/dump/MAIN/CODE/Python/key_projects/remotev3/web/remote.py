from flask import Flask,render_template

a = Flask(__name__)





@a.route('/')
def domain():
    return render_template("domain.html")

@a.route('/login')
def login():
    return "login template"







if __name__ == "__main__":
    a.run(debug=True)
