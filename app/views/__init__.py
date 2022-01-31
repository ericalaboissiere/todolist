from flask import Flask


def init_app(app: Flask):
    from app.views.tasks_view import bp_task
    app.register_blueprint(bp_task)
    """
        Importamos e registramos corretamente nossa rota task_view criada
    """
