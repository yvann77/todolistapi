# Description
api_description = """
# Task List API

This is a simple API for managing a task list using Firebase as the database.

## Endpoints

- `/todos`: List all tasks and add a new task.
- `/todos/{id}`: Retrieve, update, or delete a specific task.

## Authentication

This API does not require authentication.

## Error Handling

- If a task is not found, a 404 error will be returned.
- If there is an error with the request data, a 400 error will be returned.

"""