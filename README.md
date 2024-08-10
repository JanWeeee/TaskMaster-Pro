# TaskMaster Pro

TaskMaster Pro is a simple task management web application designed for demonstrating an API-Driven Test Automation Framework.

## Setup

1. Create a virtual environment and activate it.
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Visit `http://127.0.0.1:5000/` in your browser.

## API Endpoints

### GET /api/tasks
Retrieve all tasks.

### POST /api/tasks
Create a new task.
- **Request Body**: JSON `{ "title": "Task Title", "description": "Task Description", "due_date": "YYYY-MM-DDTHH:MM:SS" }`

### GET /api/tasks/{id}
Retrieve a specific task by ID.

### PUT /api/tasks/{id}
Update an existing task by ID.
- **Request Body**: JSON `{ "title": "Task Title", "description": "Task Description", "due_date": "YYYY-MM-DDTHH:MM:SS" }`

### DELETE /api/tasks/{id}
Delete a task by ID.

## Deployment

1. Host the Flask app on Heroku or Vercel.
2. Deploy the front-end on Netlify or GitHub Pages.

## Authentication

For now, authentication is not implemented, but the `login.html` is provided for future extension.
