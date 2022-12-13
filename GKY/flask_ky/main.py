from flask import Flask

app = Flask(__name__)

@app.route('/<number>')
def helloWorld(number):
    return 'HelloWorld %s'%(number)

app.run()