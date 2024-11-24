from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mariadb:3306/school'
db = SQLAlchemy(app)

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    ra = db.Column(db.String(9), unique=True, nullable=False)

@app.route('/aluno', methods=['POST'])
def cadastrar_aluno():
    data = request.json
    aluno = Aluno(nome=data['nome'], ra=data['ra'])
    db.session.add(aluno)
    db.session.commit()
    return jsonify({"message": "Aluno cadastrado com sucesso!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
