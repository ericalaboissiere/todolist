from flask import Flask
from os import getenv
from app.configurations import database, migrations, serializers, views

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
    """
        Aqui passei o 'SQLALCHEMY_DATABASE_URI' que foi feito no .env
    """

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    """
        Aqui passei False para evitar mensagens de avisos no terminal
    """
    app.config["JSON_SORT_KEYS"] = False
    """
        Setei como False para o Flask não organizar nossas keys por ordem alfabetica
    """
    database.init_app(app)
    migrations.init_app(app)
    serializers.init_app(app)
    """
        Iniciando as configurações do db e da migration, que agora estão prontas para uso
    """
    views.init_app(app)
    """
        Chamei o init das views para que a nossas rotas sejam inicializadas corretamente
    """

    return app
