from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return 'Hola Que Tal'

    app.run()
