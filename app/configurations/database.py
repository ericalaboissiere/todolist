from flask import Flask
# Importando apenas para typehint

from flask_sqlalchemy import SQLAlchemy
# Importando para termos a conexão com o banco de dados


db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)
    app.db = db


    from app.models.tasks import TasksModel

"""
    * Fazendo a importação de TasksModel para na hora de realizar
    o migrate ele conseguir criar a tabela
"""
