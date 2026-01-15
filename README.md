# Employee Management REST API

A CRUD-based Employee Management API built with Django and Django REST Framework.

## Features
- JWT Authentication
- Create, Read, Update, Delete Employees
- Filtering by department and role
- Pagination (10 per page)
- Proper REST status codes
- Unit tests

## Tech Stack
- Django
- Django REST Framework
- SimpleJWT
- SQLite

## Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Authentication

All employee-related endpoints are secured using **JWT-based authentication**.

### Obtain Access Token

Request body:
```json
{
  "username": "admin",
  "password": "yourpassword"
}
```

## API Endpoints

| Method | Endpoint             | Description                |
| ------ | -------------------- | -------------------------- |
| POST   | /api/employees/      | Create a new employee      |
| GET    | /api/employees/      | List employees (paginated) |
| GET    | /api/employees/{id}/ | Retrieve employee by ID    |
| PUT    | /api/employees/{id}/ | Update employee            |
| DELETE | /api/employees/{id}/ | Delete employee            |


## Pagination & Filtering

### Pagination (10 employees per page):
```bash
/api/employees/?page=2
```
### Filter by department:
```bash
/api/employees/?department=Engineering
```
### Filter by role:
```bash
/api/employees/?role=Developer
```
## Testing
```bash
python manage.py test


