
## API Endpoints

- `GET /tasks`: Return all tasks.
- `GET /tasks/<id>`: Return specific task by ID.
- `POST /tasks`: Add new task with POST request data. Return newly created task.
- `DELETE /tasks/<id>`: Delete specific task by ID. Return deleted task.
- `PUT /tasks/<id>`: Update specific task with PUT request data. Return updated task.
- `PUT /tasks/<id>/done`: Change the status of specific task to "Done". Return completed task.
- `POST /tasks/reset`: Start over. Return empty task list.
