# FastAPI Learning Journey 🚀

A hands-on journey to learning FastAPI and Python Backend Development.

I am building my backend engineering skills to prepare for a career as a **GenAI Engineer**.

My learning approach focuses on practical coding, solving exercises, debugging errors, and preparing for technical interviews.

## 🎯 Learning Goals

- Understand HTTP and REST API fundamentals.
- Build REST APIs using FastAPI.
- Learn request handling and response handling.
- Understand path and query parameters.
- Learn Pydantic and data validation.
- Work with PostgreSQL and SQLAlchemy.
- Understand authentication and authorization.
- Learn API testing and deployment.

## 🛠️ Technology Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- PostgreSQL
- SQLAlchemy
- Pytest
- Git and GitHub
- Docker

## 📚 Learning Progress

| Day | Topics | Status |
|---|---|---|
| Day 1 | HTTP fundamentals, REST APIs, HTTP methods, status codes, path parameters and query parameters | Completed |
| Day 2 | Pydantic, request body and data validation | Upcoming |
| Day 3 | APIRouter, dependency injection and middleware | Upcoming |
| Day 4 | PostgreSQL and SQLAlchemy | Upcoming |
| Day 5 | Authentication, authorization and file handling | Upcoming |
| Day 6 | Testing, error handling and logging | Upcoming |
| Day 7 | Docker and deployment | Upcoming |

## 📅 Day 1 — FastAPI and REST API Fundamentals

**Date:** November 17, 2026

### 1. Backend Fundamentals

- What is a server?
- Client and server communication.
- What is FastAPI?
- What is Uvicorn?
- What is ASGI?
- How FastAPI handles HTTP requests and responses.

### 2. HTTP Methods

| Method | Purpose |
|---|---|
| GET | Retrieve data |
| POST | Create or submit data |
| PUT | Replace an existing resource |
| PATCH | Partially update an existing resource |
| DELETE | Delete a resource |

### 3. HTTP Status Codes

| Status Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

### 4. API Endpoints

An API endpoint is a specific URL path and HTTP method used to perform an operation on a server.

Example:

```python
@app.get("/students")
def get_students():
    return {"message": "Student details"}
```

### 5. Path Parameters

Path parameters are values included in the URL path to identify a specific resource.

Example:

```python
@app.get("/students/{student_id}")
def student_details(student_id: int):
    return {
        "student_id": student_id
    }
```

Example URL:

```text
/students/25
```

### 6. Query Parameters

Query parameters pass additional information through the URL.

Example:

```python
@app.get("/students")
def get_students(limit: int = 10):
    return {
        "limit": limit
    }
```

Example URLs:

```text
/students
/students?limit=10
/students?limit=50
```

### 7. Path Parameters vs Query Parameters

| Path Parameter | Query Parameter |
|---|---|
| Part of URL path | Comes after `?` |
| Identifies a resource | Passes additional information |
| `/students/25` | `/students?limit=10` |

## 💻 Practical Work

Today's hands-on exercises included:

- Creating GET `/courses`.
- Creating GET `/students/{student_id}`.
- Creating GET `/students` with a query parameter.
- Creating GET `/courses/{course_id}`.
- Creating GET `/products/{product_name}`.
- Practicing multiple path parameters.
- Debugging FastAPI endpoint errors.

## 🎤 Interview Preparation

Topics practiced:

1. What is an API endpoint?
2. What is FastAPI?
3. What is Uvicorn?
4. What is a path parameter?
5. What is a query parameter?
6. Difference between GET and POST.
7. Difference between PUT and PATCH.
8. What are HTTP status codes?
9. Difference between 401 and 403.
10. What does HTTP 422 mean in FastAPI?

## 📌 Next Learning Target — Day 2

- Pydantic
- BaseModel
- Field and Annotated
- Request body
- Data validation
- Required and optional fields
- Response models

---

**Learning by building, practicing, debugging, and improving every day.**