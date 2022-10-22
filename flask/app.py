from flask import Flask
app = Flask(__name__)

@app.route("/number")
def number():
    return "123"
@app.route("/hello")
def hello():
    return "hello!!"

if __name__ == '__main__':
    app.run()