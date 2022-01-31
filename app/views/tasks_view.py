from flask_restful import Resource, reqparse, current_app
"""
    * Resource: é classe que herdaremos para criação de rotas
    * reqparse: utilizado para verificação sobre os atributos mandados pelo body
    * current_app: é o mesmo do flask, utilizaremos para pegar sessão atual
"""

from http import HTTPStatus

from app.models.tasks import TasksModel
from app.schemas.task_schema import task_schema, tasks_schema


"""
    NOTA: os métodos das rotas são definido no nome dos metodos de instância
"""

class AllTasks(Resource):
    def get(self):
        all_tasks = TasksModel .query.all()
        serializer = tasks_schema .dump(all_tasks)

        return {"data": serializer}, HTTPStatus.OK


class Task(Resource):
    def get(self, req_id):
        task = TasksModel .query.get(req_id)

        serializer = task_schema.dump(task)
        return {"data": serializer}, HTTPStatus.OK

    def post(self):
        parse = reqparse.RequestParser()
        """
        reqparse.RequestParser(): utilizamos para pegar os argumentos
        mandado no body da requisição
        """
        parse.add_argument("task", type=str, required=True)

        """
        * parse.add_argument: aqui vamos fazer adição de algus argumentos ao nosso parser

        * "task": uma das chaves que vai vir no body da nossa requisição

        * type=str: o tipo do dado recebido aqui tem que ser uma string, caso seja
          algo diferente irá dar erro

        * required=True: esse dado é requerido, ou seja, se não for passado vai retorar um erro,
          por padrão ele vem como False
        """


        args = parse.parse_args()

        """
            parse.parse_args(): aqui estamos pegado os argumentos que foram passados no body da
            nossa requisição
        """

        task = TasksModel (**args)
        current_app.db.session.add(task)
        current_app.db.session.commit()
        serializer = task_schema.dump(task)

        return serializer, HTTPStatus.OK

    def put(self, req_id):
        parse = reqparse.RequestParser()
        parse.add_argument("task", type=str)

        args = parse.parse_args()

        task = TasksModel .query.get_or_404(req_id)
        for key, value in args.items():
            if value:
                setattr(task, key, value)
                """
                setattr(task, key, value):
                    * o primero parâmetro: passamos o objeto que queremos fazer a alterção

                    * o segundo parâmetro: passamos o nome do atributo que queremos fazer a alteração

                    * o terceiro parâmetro: passamos o novo valor que irá ser atribuido à esse atributo
                """

        current_app.db.session.commit()
        serializer = task_schema.dump(task)

        return {"data": serializer}, HTTPStatus.OK

    def delete(self, req_id):
        task = TasksModel .query.get_or_404(req_id)
        current_app.db.session.delete(task)
        current_app.db.session.commit()

        return {"data": "NO CONTENT"}, HTTPStatus.NO_CONTENT
