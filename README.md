Todo Notes API (FastAPI)

This is a professional REST API built with FastAPI for managing personal todo notes. It uses SQLAlchemy ORM to perform CRUD (Create, Read, Update, Delete) operations on a local SQLite database. The project follows a modular architecture and includes robust error handling to provide meaningful feedback when resources are not found or when internal errors occur.


How to Run the Application

1. Prerequisites
- Python 3.9 or higher installed
- A virtual environment created and activated

2. Install Dependencies
Run the following command in your terminal:
- pip install fastapi uvicorn sqlalchemy

3. Start the Server
From the project root directory, run:
- uvicorn main:app --reload

4. The server will start at:
- http://127.0.0.1:8000

5. Interactive Testing
You can test all API endpoints directly using Swagger UI:
- http://127.0.0.1:8000/docs


API Endpoints

1. GET /
Bonus: Welcome message (Root endpoint)

2. POST /notes
Create a new note (Returns 201 Created)

3. GET /notes
Fetch all notes

4. PUT /notes/{id}
Update an existing note (Requires full JSON body)

5. DELETE /notes/{id}
Permanently delete a note


Key Features

1. Local Persistence
Uses a local SQLite database (todos.db) which is generated automatically on the first run.

2. Input Validation
Uses Pydantic schemas to ensure all required fields are validated before saving data to the database.

3. Error Handling
Returns 404 Not Found when a note ID does not exist and 500 Internal Server Error for database-related failures.

4.Success Messages
Provides clear and meaningful confirmation messages for delete operations.