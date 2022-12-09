from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/novo')
def novo():
    return render_template('novo.html')



app.run(debug=True)