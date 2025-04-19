from flask import Flask

app = Flask(__name__)

@app.route("/")
def number():
    return "123"
@app.route("/hello")
def hello():
    return "hello!!"
# app.register_blueprint(app2)
if __name__ == '__main__':
    app.run()