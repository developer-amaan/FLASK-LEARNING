from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello , world!'

@app.route("/bye")
def bye():
    return 'bye  bye'

@app.route("/<name>")
def name(name):
    return f"Hello there {name}"

@app.route("/username/<name>")
def username(name):
    return f"Hello there {name}"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello this is {name}, I am {number} years old"


if __name__ == "__main__":
    app.run(debug=True)
