**To Do List**
**Version 1.0.0**

Platform designed to manage organize your tasks, in which it's possible to register, edit and delete. This is only the backend API.

**Getting started**

1. git clone [To do List](git@github.com:ericalaboissiere/todolist.git)
2. cd to the directory where requirements.txt is located.
3. activate your virtualenv.
4. ```$ pip install -r requirements.txt in your shell.
5. create .env file
6. set environment variables
5. ```$ flask db init
6. ```$ flask db migrate -m "Initial migration."
7. ```$ flask db upgrade
8. ```$ flask run

**Routes**

- POST /api/task - creates tasks
- GET /api/task - list all tasks
- GET /api/task/pk - get task by id
- PUT /api/task/pk - updates task data
- DELETE /api/task/pk - delete tasks using primary key

**Examples of Requests:**

- Create task: POST /api/task
>{
>	"task": "Study"
>}


- Get by id: GET /api/task/pk
>{
>  "data": {
>    "id": 2,
>    "task": "Work"
>  }
>}


- Get all: GET /api/task
>{
>  "data": [
>    {
>      "id": 1,
>      "task": "Study"
>    },
>    {
>      "id": 2,
>      "task": "Work"
>    },
>    {
>      "id": 3,
>      "task": "Meeting"
>    }
>  ]
>}

- Changing a task: PUT /api/task/pk
>{
>	"task": "Study"
>}


**Deleting a task**: DELETE /api/task/pk
