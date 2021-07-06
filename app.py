from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Alterar para as informações do banco de vcs
user = 'bwuqslwc'
password = 'XvkMKgFaa1In_ZxwakcZSWNZb4A7PESS'
host = 'batyr.db.elephantsql.com'
database = 'bwuqslwc'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "a9dcd386-0568-409d-9123-5c8aff7a511d"

db = SQLAlchemy(app)

class animais(db.Model): #modelar a classe baseado na tabela animais
    id = db.Column(db.Integer, primary_key=True)
    nomeanimal = db.Column(db.String(255), nullable=False)
    imagemurl = db.Column(db.String(255), nullable=False)

    def __init__(self, nomeanimal, imagemurl):
        self.nomeanimal = nomeanimal
        self.imagemurl = imagemurl
    
    @staticmethod
    def read_all(): #aqui ele faz um query = select * 
        return animais.query.order_by(animais.id.asc()).all()

    @staticmethod
    def read_single(id_registro): #aqui é basicamente a pesquisa que fazemos no bando Select * from animais where id = x (esse x é o numero do id que ele vai buscar na url)
        return animais.query.get(id_registro)
    
    @staticmethod
    def conta(): 
        return animais.query.count()
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, novo_nomeanimal, nova_imagemurl):
        self.nomeanimal = novo_nomeanimal
        self.imagemurl = nova_imagemurl

        self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

@app.route("/")
def index():
    total = animais.conta()
    return render_template("index.html", total=total)

@app.route("/read")
def read_all():
    registros = animais.read_all()
    return render_template("read_all.html", registros=registros)

@app.route("/read/<id_registro>")
def read_id(id_registro):
    registro = animais.read_single(id_registro)
    return render_template("read_single.html", registro=registro)

@app.route("/create", methods=('GET', 'POST'))
def create():
    novo_id = None
    if request.method == 'POST':
        form = request.form
        registro = animais(form['nomeanimal'], form['imagemurl']) # aqui ainda preciso acrescentar no form as outras linhas do banco
        registro.save()
        novo_id = registro.id

    return render_template("create.html", novo_id=novo_id)

@app.route('/update/<id_registro>', methods=('GET', 'POST'))
def update(id_registro):
    sucesso = False

    registro = animais.read_single(id_registro)

    if request.method == 'POST':
        form = request.form
        registro.update(form['nomeanimal'], form['imagemurl']) 
        sucesso = True
    return render_template('update.html', registro=registro, sucesso=sucesso)

@app.route('/delete/<id_registro>')
def delete(id_registro):
    registro = animais.read_single(id_registro)
    return render_template("delete.html", registro=registro)

@app.route('/delete/<id_registro>/confirmed')
def delete_confirmed(id_registro):
    sucesso = False 

    registro = animais.read_single(id_registro)

    if registro:
        registro.delete()
        sucesso = True

    return render_template("delete.html", registro=registro, sucesso=sucesso)

if (__name__ == "__main__"):
    app.run(debug=True)