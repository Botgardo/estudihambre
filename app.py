from flask import Flask

app = Flask(__name__)
app.secret_key = '12345'

from controlador import *

if __name__  == '__main__':
    app.run(debug=True)