from flask import Flask, render_template, request, redirect
from pessoa import Pessoa


pessoas = [
    Pessoa('Jean', 42, 1.80),
    Pessoa('Larissa', 28, 1.58),
    Pessoa('Haiko', 82, 1.75)
]

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html', pessoas = pessoas, title = 'Home')

@app.route('/novo')
def novo():
    return render_template('novo.html')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    pessoas.append(Pessoa(nome, idade, altura))
    return redirect('/')



app.run(debug=True)