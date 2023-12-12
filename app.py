#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# app.py
# Importando as bibliotecas necessárias
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

# Criação do aplicativo Flask
app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db' 

# Inicialização do SQLAlchemy com o aplicativo Flask
db = SQLAlchemy(app)

# Inicialização do Flasgger (para documentação da API Swagger) com o aplicativo Flask
swagger = Swagger(app)

# Modelo de Pessoa para o SQLAlchemy
class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)

# Modelo de Treinamento para o SQLAlchemy
class Treinamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=False)

# Rota para adicionar uma nova pessoa
@app.route('/pessoa', methods=['POST'])
def add_pessoa():
    """
    Crie uma nova pessoa
    Use esta rota para adicionar uma nova pessoa ao banco de dados.
    ---
    parameters:
      - name: nome
        in: body
        type: string
        required: true
        description: O nome da pessoa
    responses:
      200:
        description: O ID da nova pessoa
    """
    nome = request.json['nome']
    nova_pessoa = Pessoa(nome=nome)
    db.session.add(nova_pessoa)
    db.session.commit()
    return {'id': nova_pessoa.id}, 200

# Rota para deletar uma pessoa
@app.route('/pessoa/<int:id>', methods=['DELETE'])
def delete_pessoa(id):
    """
    Deleta uma pessoa
    Use esta rota para deletar uma pessoa do banco de dados pelo ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: O ID da pessoa
    responses:
      200:
        description: Pessoa deletada
    """
    Pessoa.query.filter_by(id=id).delete()
    db.session.commit()
    return {'result': 'Pessoa deletada'}, 200

# Rota para adicionar um novo treinamento
@app.route('/treinamento', methods=['POST'])
def add_treinamento():
    """
    Crie um novo treinamento
    Use esta rota para adicionar um novo treinamento ao banco de dados.
    ---
    parameters:
      - name: titulo
        in: body
        type: string
        required: true
        description: O título do treinamento
      - name: pessoa_id
        in: body
        type: integer
        required: true
        description: O ID da pessoa
    responses:
      200:
        description: O ID do novo treinamento
    """
    titulo = request.json['titulo']
    pessoa_id = request.json['pessoa_id']
    novo_treinamento = Treinamento(titulo=titulo, pessoa_id=pessoa_id)
    db.session.add(novo_treinamento)
    db.session.commit()
    return {'id': novo_treinamento.id}, 200

# Rota para deletar um treinamento
@app.route('/treinamento/<int:id>', methods=['DELETE'])
def delete_treinamento(id):
    """
    Deleta um treinamento
    Use esta rota para deletar um treinamento do banco de dados pelo ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: O ID do treinamento
    responses:
      200:
        description: Treinamento deletado
    """
    Treinamento.query.filter_by(id=id).delete()
    db.session.commit()
    return {'result': 'Treinamento deletado'}, 200

# Rota para buscar um treinamento
@app.route('/treinamento/<int:id>', methods=['GET'])
def get_treinamento(id):
    """
    Busca um treinamento
    Use esta rota para buscar um treinamento no banco de dados pelo ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: O ID do treinamento
    responses:
      200:
        description: Os detalhes do treinamento
    """
    treinamento = Treinamento.query.get(id)
    if treinamento is None:
        return {'error': 'Treinamento não encontrado'}, 404
    return {
        'id': treinamento.id,
        'titulo': treinamento.titulo,
        'pessoa_id': treinamento.pessoa_id
    }, 200

# Rota para buscar os treinamentos de uma pessoa
@app.route('/pessoa/<int:id>/treinamentos', methods=['GET'])
def get_treinamentos_pessoa(id):
    """
    Busca os treinamentos de uma pessoa
    Use esta rota para buscar os treinamentos de uma pessoa no banco de dados pelo ID da pessoa.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: O ID da pessoa
    responses:
      200:
        description: A lista de treinamentos da pessoa
    """
    treinamentos = Treinamento.query.filter_by(pessoa_id=id).all()
    if not treinamentos:
        return {'error': 'Nenhum treinamento encontrado para esta pessoa'}, 404
    return {
        'treinamentos': [
            {
                'id': treinamento.id,
                'titulo': treinamento.titulo
            }
            for treinamento in treinamentos
        ]
    }, 200

# Função principal para iniciar o aplicativo Flask
def main():
    with app.app_context():
        db.create_all()
    app.run(debug=True)

if __name__ == '__main__':
    main()


# In[ ]:




