# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using FastAPI by defining endpoints, handling requests, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description

Build a FastAPI application with endpoints for a simple items catalog. Your API should let users list items, retrieve item details, add new items, update existing items, and delete items.

#### Requirements
Completed program should:
- Use FastAPI to define the application and route handlers
- Add a GET `/items` endpoint that returns all items
- Add a GET `/items/{item_id}` endpoint that returns a single item by ID
- Add a POST `/items` endpoint to create a new item
- Add a PUT `/items/{item_id}` endpoint to update an existing item
- Add a DELETE `/items/{item_id}` endpoint to remove an item
- Use Pydantic models for request validation and response data
- Return appropriate HTTP status codes for success and error cases

### 🛠️ Validate Requests and Document the API

#### Description

Add request validation rules and use FastAPI’s built-in documentation to verify your API behavior.

#### Requirements
Completed program should:
- Validate incoming request data with Pydantic model field types and constraints
- Return a 400 error for invalid input data
- Show the API documentation at `/docs` when the server is running
- Include a short note in the README explaining how to run the app with `uvicorn`
