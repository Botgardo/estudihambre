from flask import render_template, request, redirect, session, url_for
from app import app

@app.route("/")
def index():
    return render_template("index.html", show_footer = True, show_profile = True)

account_rutas = ['name','age','email']
@app.route('/account/create/<input>',  methods=['GET', 'POST'])
def account_create(input):
     if input not in account_rutas:
         return "Error no existe la pregunta", 404
     
     if 'action' in request.form and request.form['action'] == 'back':
            # Obtener el índice de la pregunta actual
            current_index = account_rutas.index(input)
            if current_index - 1 >= 0:  # Verificar que no sea la primera pregunta
                prev_input = account_rutas[current_index - 1]
                return redirect(url_for('account_create', input=prev_input))
            else:
                return redirect(url_for('index'))  # Redirigir al inicio si no hay preguntas anteriores

     if request.method == 'POST':

        # Guardar la de la sesion
        session[input] = request.form.get(input)

        # Obtener el índice de la pregunta actual
        current_index = account_rutas.index(input)

        if current_index + 1 < len(account_rutas):
            next_input = account_rutas[current_index + 1]
            return redirect(url_for('account_create', input=next_input))
        else:
            return redirect(url_for('prueba'))

     return render_template("account/form.html", show_footer = False, show_profile = False, input = input)

@app.route('/account/create/welcome')
def prueba():
    session_data = []
    for key, value in session.items():
        session_data.append(f"{key}: {value}")
    
    return "<br>".join(session_data)

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