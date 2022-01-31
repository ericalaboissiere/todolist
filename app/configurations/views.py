from flask import Flask
from flask_restful import Api

def init_app(app: Flask):
    api = Api(app) # última linha adicionada ao código

    from app.views.tasks_view import Task, AllTasks

    api.add_resource(AllTasks, "/api/task")

    """
        * api.add_resource: utilizado para adicionarmos as rotas, os parâmetros recebidos
          serão resource, *urls e **kwargs

        * AllTasks: passamos primeiro, pois o primeiro parâmetro é resource

        * '/api/task': a url passamos por segundo para entrar nos args de urls
    """

    api.add_resource(Task, "/api/task", endpoint="/task", methods=["POST"])

    """
        * methods=['POST']: utilizado para especificar qual método essa rota irá utilizar, aqui
          eu só passo o 'POST' por que essa é a unica rota que não irá precisar receber um
          '<int:req_id> (declarado na linha abaixo)

        * endpoint='/all_tasks': utilizado quando adicionamos dois ou mais recursos para a
          mesma classe, visto que por padrão o flask restful define o endpoint igual ao
          nome da classe, porém em minúsculo. Dessa forma para evitarmos a existência de dois
          recursos com o mesmo endpoint, atribuímos um valor árbitrario para o mesmo
    """

    api.add_resource(
        Task,
        "/api/task/<int:req_id>",
        endpoint="/task/<int:req_id>",
        methods=["GET", "PUT", "DELETE"],
    )
