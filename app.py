from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Esta es la pagina principal'

@app.route('/account/create/<input>')
def account_create(input):
    return f'Esta es la pagina para registrase {input}'

@app.route('/account/create/bienvenida')
def account_welcome():
    return 'Esta es la pagina para recibir al usuario recien ingresado'

@app.route('/account/login')
def account_login():
    return 'Esta es la pagina para iniciar sesion'

@app.route('/account/settings')
def account_settings():
    return 'Esta es la pagina para configurar el perfil'

@app.route('/food/diary')
def food_diary():
    return 'Esta es la pagina para llevar registro de alimentacion'

@app.route('/food/mine')
def food_mine():
    return 'Esta es la pagina para crear dieta'