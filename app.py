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

def checkmail(name):
   if name in datos:
      email = datos[name]
      return email
   return 'No encontrado'

@app.route('/addmail',methods = ['POST', 'GET'])
def addmail():
   if request.method == 'POST':
      nom = request.form['name']
      email = request.form['email']
      datos[nom] = email
      return render_template('resultadoaddmail.html')
   else:
      return render_template('formaddmail.html')
      

@app.route('/getmail',methods = ['POST', 'GET'])
def getmail():
   if request.method == 'POST':
      nom = request.form['name']
      email = checkmail(nom)
      return render_template('formpostmail.html',resultado = email)
   else:
      return render_template('formgetmail.html')

if __name__ == '__main__':
   app.run(debug = True)