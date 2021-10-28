from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

app.secret_key = "192837465"


user = {"username": "Diego", "password": "pruebasimple"}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    if('user' in session and session['user'] == user['username']):
        return render_template('dashboard.html')

    return '<h1>Aun no has iniciado sesión.</h1><a href="/login/" class="btn btn--secondary">Regresar</>'  


@app.route('/login/', methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')     
        if username == user['username'] and password == user['password']:
            
            session['user'] = username
            return redirect('/dashboard/')

        return '<h1>Nombre de usuario o contraseña equivocados</h1><a href="/login/" class="btn btn--secondary">Regresar</>'

    return render_template("login.html")

@app.route('/dashboard/logout/')
def logout():        
    session.pop('user')         
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)