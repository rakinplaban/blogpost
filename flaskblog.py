from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hello():
    return "<h1 style='font-size:200px;color:green;'>Hello world!</h1>"


@app.route("/new_route")
def new_route():
    return "<h1 style='font-size:20px;color:yellow;'>Hello world!</h1>"


if __name__ == '__main__':
    app.run(debug=True)