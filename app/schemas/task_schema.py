from app.models.tasks import TasksModel
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


class TasksSchema(SQLAlchemySchema):
    class Meta:
        model = TasksModel

    id = auto_field()
    task = auto_field()

task_schema = TasksSchema()
tasks_schema = TasksSchema(many=True)
