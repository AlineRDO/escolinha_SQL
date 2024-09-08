from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///saude_alunos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    endereco = db.Column(db.String(200))
    contato = db.Column(db.String(20))

class Saude(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    historico_medico = db.Column(db.String(200))
    alergias = db.Column(db.String(100))
    vacinas = db.Column(db.String(200))
    exames_medicos = db.Column(db.String(200))

class Desenvolvimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    notas = db.Column(db.String(100))
    avaliacoes_fisicas = db.Column(db.String(200))
    atividades_extracurriculares = db.Column(db.String(200))


@app.route('/')
def index():
    return jsonify({"Bem-vindo ao sistema de saúde e desenvolvimento dos alunos"})

if __name__ == '__main__':
    db.create_all()  # Criar as tabelas no banco de dados
    app.run(debug=True)
