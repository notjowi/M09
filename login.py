from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

datos = {
    'Mercedes': 'mcast386@xtec.cat',
    'Rayane': 'rayane@rayane.sa',
    'Mohamed': 'moha@gmail.com',
    'Jad': 'jad@gmail.com',
    'Oriol': 'joam@gmail.com',
    'Elias': 'hola123@gmail.com',
    'Armau': 'arnau@gmail.com',
    'Asdrúbal': 'asdrubal@gmail.com',
    'Adrian': 'pedrosanchez@asix2.com',
    'Eric': 'eric@gmail.com',
    'Emma': 'pacosanz@gmail.com',
    'Nishwan': 'nishwan@gmail.com',
    'Javi': 'javi@gmail.com',
    'Novel': 'novelferreras49@gmail.com',
    'Bruno': 'elcigala@gmail.com',
    'David': 'argentino@gmail.com',
    'Judit': 'judit@gmail.com',
    'Joao': 'joao@gmail.com',
    'Laura': 'laura@gmail.com',
    'Enrico': '123@gmail.com',
    'Joel': 'joelcobre@gmail.com',
    'Aaron': 'aaron@gmail.com',
    'Moad': 'moad@gmail.com'
}

@app.route('/dashboard/<name>')
def dashboard(name,resultado=None):
   if name in datos:
      resultado = datos[name]
      return render_template('resultado.html',resultado = resultado)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('dashboard',name = user))
   else:
      user = request.args.get('name')
      return render_template('formula.html')

if __name__ == '__main__':
   app.run(debug = True)