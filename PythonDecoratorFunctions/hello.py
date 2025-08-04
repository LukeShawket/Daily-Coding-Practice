from flask import Flask

app = Flask(__name__)

def bolder(function):
    def wrapper(*args, **kwargs):
        result = function
        return f"<b>{result}</b>"
    return wrapper

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
    '<p>This is a paragraph.</p>' \
    '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDg1azcycHM4eTR1dGE1eHhqdG5ocGxtdTRwN2szcnk2cGtqeWlyeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uUP7F5A1rQR9uKls9P/giphy.gif" width=200>'

@app.route("/whatsnew")
@bolder
def whats_new():
    return "Nothing"

@app.route("/username/<name>/<int:age>")
def greet(name, age):
    return f"Hello {name}, You are {age} years old."


if __name__ == "__main__":
    app.run(debug=True)


