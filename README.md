
## API Endpoints

- `GET /tasks`: Return all tasks.
  ```bash
  curl --request GET http://localhost/tasks
  ```
- `GET /tasks/<id>`: Return specific task by ID.
  ```bash
  curl --request GET http://localhost/tasks/1
  ```
- `POST /tasks`: Add new task with POST request data. Return newly created task.
  ```bash
  curl --request POST --header "Content-Type: application/json" --data '{"Title":"new title","Details":"new details"}' http://localhost/tasks
  ```
- `DELETE /tasks/<id>`: Delete specific task by ID. Return deleted task.
  ```bash
  curl --request DELETE http://localhost/tasks/1
  ```
- `PUT /tasks/<id>`: Update specific task with PUT request data. Return updated task.
  ```bash
  curl --request PUT --header "Content-Type: application/json" --data '{"Title":"updated title","Details":"updated details","Status":"updated status"}' http://localhost/tasks/1
  ```
- `POST /tasks/<id>/done`: Change the status of specific task to "Done". Return completed task.
  ```bash
  curl --request POST http://localhost/tasks/1/done
  ```
- `POST /tasks/reset`: Start over. Return empty task list.
  ```bash
  curl --request POST http://localhost/tasks/reset
  ```
  - `POST /tasks/<id>/ai`: Ask ChatGPT to assist with specific task. ;)
  ```bash
  curl --request POST http://localhost/tasks/2/ai
  ```
