from flask import Flask, request, redirect, url_for, render_template
import requests
import json

app = Flask(__name__)

link = "https://primeira-base-251e9-default-rtdb.firebaseio.com/bd/clientes_forms"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']

        dados = {
            "nome": nome,
            "email": email,
        }
        requisicao = requests.post(f'{link}/.json', data=json.dumps(dados))
        print(requisicao)
        print(requisicao.text)
    return redirect(url_for('index'))

@app.route('/blog')
def blog():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
