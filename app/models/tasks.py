from . import db
"""
    Aqui fiz a importação do db a partir do app/models/__init__.py
"""

class TasksModel(db.Model): # db.Model para criação da tabela
    __tablename__ = "tasks"
    """
        Aqui declarei o nome da tabela, caso __tablename__
        não seja declarado, o nome da tabela será o nome da classe
    """

    id = db.Column(db.Integer, primary_key=True)
    """
        * db.Column: para criação de coluna
        * db.Integer: indicando que essa coluna é um integer
        * primary_key = True: indicando que essa coluna é uma primary_key
    """

    task = db.Column(db.String(100), nullable=False, unique=True)
    """
        * db.Column: para criação de coluna
        * db.String(100): indicando que essa coluna é um varchar(100)
        * nullable = False: indicando que não será permitido valores nullos,
          por default é definido como True.
        * unique = True: indicando que a task deve ser unica no banco
    """

