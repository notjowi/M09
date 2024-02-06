from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dhello():
    return "Hello World!"

#Ejercicio 1
@app.route("/parellsenar/<int:numero>")
def parinpar(numero):
    return f'El numero {numero} es par' if numero % 2 == 0 else f'El numero {numero} no es par'
#Ejercicio 2
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
#Ejercicio 3
@app.route('/edad100/<username>/<int:number>')
def edad(username=None, number=None, resultado=None):
    resultado = 2023 + (100 - number)
    return render_template('hello2.html', username=username, number=number, resultado=resultado)
#Ejercicio 4
@app.route('/background')
def background():
    return render_template('hello3.html')