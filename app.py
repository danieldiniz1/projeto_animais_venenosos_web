from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurações de acesso ao banco de dados
user = 'nvuldbus'
password = 'iBcWjSnkS5_DmGer9xVdn2IOnDqueBpQ'
host = 'tuffi.db.elephantsql.com'
database = 'nvuldbus'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Uma chave secreta bem secreta'

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == ('__main__'):
    app.run(debug=True)