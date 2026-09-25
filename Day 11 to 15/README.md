# Batch 4 Full Stack - Student Management System

A production-grade, enterprise-structured Full-Stack web application featuring a **React.js** frontend, a **FastAPI** backend, and a **PostgreSQL** relational database managed via **SQLAlchemy**.

The primary objective of the application is to manage student academic records through an interactive **Overview Page** that displays personal information and academic marks in a tabular view, backed by a complete set of CRUD operations.

---

## 📑 Table of Contents
- [1. Project Overview](#1-project-overview)
- [2. Technology Stack](#2-technology-stack)
- [3. Backend Architecture & Design Pattern](#3-backend-architecture--design-pattern)
- [4. Project Directory Structure](#4-project-directory-structure)
- [5. Database Schema & Data Dictionary](#5-database-schema--data-dictionary)
- [6. Request Lifecycle & Data Flow](#6-request-lifecycle--data-flow)
- [7. API Endpoints](#7-api-endpoints)
- [8. Installation & Setup Guide](#8-installation--setup-guide)
  - [Prerequisites](#prerequisites)
  - [Database Configuration](#database-configuration)
  - [Backend Setup (FastAPI)](#backend-setup-fastapi)
  - [Frontend Setup (React.js)](#frontend-setup-reactjs)
- [9. Coding Standards & Best Practices](#9-coding-standards--best-practices)

---

## 1. Project Overview

The **Batch 4 Full Stack Application** is engineered using an enterprise-level layered architectural pattern. The system allows educators and administrators to:
- Register student records containing contact details, department, and academic subject marks.
- Automatically calculate overall performance percentages in the business logic layer.
- View and manage records from a responsive React frontend with full Create, Read, Update, and Delete (CRUD) capabilities.

---

## 2. Technology Stack

| Layer | Technology | Description |
|---|---|---|
| **Frontend** | React.js | Component-driven UI, state management, and responsive data tables |
| **Backend Framework** | FastAPI (Python 3.10+) | High-performance, asynchronous RESTful API framework |
| **Data Validation** | Pydantic v2 | Request/response schema definitions and type validation |
| **Database & ORM** | PostgreSQL & SQLAlchemy 2.0 | Relational database persistence with Object Relational Mapping |
| **DB Driver** | psycopg2-binary | PostgreSQL database adapter for Python |
| **Server** | Uvicorn | Lightning-fast ASGI server implementation |
| **Configuration** | python-dotenv | Environment variable configuration management |

---

## 3. Backend Architecture & Design Pattern

The FastAPI backend strictly follows the **Modular Layered Architecture (Separation of Concerns)** to ensure high maintainability, testability, and scalability.

```
Incoming Request (HTTP)
         │
         ▼
┌──────────────────┐
│   Routers Layer  │  --> Handles endpoints, HTTP methods, and status codes
└────────┬─────────┘
         │  (Validates with Pydantic Schemas)
         ▼
┌──────────────────┐
│  Services Layer  │  --> Executes business logic (e.g., mark calculation)
└────────┬─────────┘
         │  (Transforms into SQLAlchemy Models)
         ▼
┌──────────────────┐
│ Repository Layer │  --> Performs pure database operations & SQL queries
└────────┬─────────┘
         │  (Uses DB session from Core)
         ▼
┌──────────────────┐
│  Database (PG)   │  --> PostgreSQL relational data store
└──────────────────┘
```

### Layer Responsibilities:
1. **`core/`**: Central configuration, database engine initialization (`create_engine`), session factory (`SessionLocal`), declarative base model, and database dependency (`get_db`).
2. **`models/`**: SQLAlchemy database model definitions representing database tables and constraints.
3. **`schemas/`**: Pydantic models for request payload validation, type checking, and response serialization.
4. **`repository/`**: Data Access Layer (DAO) encapsulating all direct database operations (queries, inserts, updates, deletes).
5. **`service/`**: Pure business logic isolated from database operations and HTTP requests (e.g., percentage calculation: `(python + java + database) / 3`).
6. **`routes/`** (or `routers/`): API controllers defining routes, mapping HTTP requests to service/repository functions, and injecting dependencies.
7. **`main.py`**: Application entry point, router registration, middleware setup (CORS), and startup schema migration hooks.

---

## 4. Project Directory Structure

```text
Day 11 to 15/
│
├── backend/
│   ├── core/                          # Database connection and session management
│   │   ├── __init__.py
│   │   └── database.py                # Engine, SessionLocal, Base, and get_db dependency
│   ├── models/                        # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   └── student_details.py         # StudentModel table definition
│   ├── schemas/                       # Pydantic schemas for data validation
│   │   ├── __init__.py
│   │   └── student_schema.py          # StudentSchema input/output schemas
│   ├── repository/                    # Database queries and CRUD execution logic
│   │   ├── __init__.py
│   │   └── student_repository.py      # create_student_repo, read, update, delete
│   ├── service/                       # Business logic layer
│   │   ├── __init__.py
│   │   └── student_service.py         # Percentage computation and business rules
│   ├── routes/                        # API route definitions (Endpoints)
│   │   ├── __init__.py
│   │   └── student_routes.py          # /create-student and CRUD endpoints
│   ├── .env                           # Environment variables (Database URL, credentials)
│   ├── main.py                        # FastAPI app initialization & route aggregation
│   └── requirements.txt               # Backend Python dependencies
│
├── frontend/                          # React.js application
│   ├── public/                        # Static assets & index.html
│   ├── src/
│   │   ├── components/                # Reusable UI components (Table, Modal, Form)
│   │   ├── pages/                     # Overview Page, Add/Edit Student Page
│   │   ├── services/                  # Axios/Fetch API client calls
│   │   ├── App.jsx / App.js           # Main application component
│   │   └── index.jsx / index.js       # React root mount
│   └── package.json                   # Frontend npm dependencies
│
└── README.md                          # Project documentation and KT guide
```

---

## 5. Database Schema & Data Dictionary

Table Name: **`students`**

| Field | Type | Modifiers / Constraints | Description |
|---|---|---|---|
| `id` | `INTEGER` | Primary Key, Auto Increment, Indexed | Unique identifier for the student |
| `name` | `VARCHAR` | Required | Full name of the student |
| `email` | `VARCHAR` | Required, Valid Email | Student email address |
| `phonenumber` | `VARCHAR` | Required | Contact phone number |
| `department` | `VARCHAR` | Required | Academic department (e.g., CSE, IT, ECE) |
| `address` | `VARCHAR` | Required | Residential / contact address |
| `python_mark` | `INTEGER` | Required (0-100) | Marks scored in Python |
| `java_mark` | `INTEGER` | Required (0-100) | Marks scored in Java |
| `database_mark` | `INTEGER` | Required (0-100) | Marks scored in Database |
| `percentage` | `FLOAT` | Computed | Average percentage score: `(python + java + db) / 3` |
| `created_at` | `TIMESTAMP` | Server Default (`func.now()`) | Record creation timestamp |
| `updated_at` | `TIMESTAMP` | On Update (`func.now()`) | Record last modification timestamp |

---

## 6. Request Lifecycle & Data Flow

When creating a new student record:
1. **Client Request**: Frontend sends an HTTP `POST` request to `/create-student` with JSON payload.
2. **Validation**: FastAPI parses the payload against `StudentSchema` (Pydantic validates types and email format).
3. **Business Logic**: `student_routes` passes data to `calculate_percentage()` in `service/student_service.py`.
4. **Model Mapping**: A `StudentModel` instance is constructed containing both input attributes and calculated percentage.
5. **Persistence**: `create_student_repo()` in `repository/student_repository.py` inserts the record into PostgreSQL and commits the transaction.
6. **Response**: FastAPI returns the persisted record along with generated IDs, timestamps, and HTTP 200/201 status.

---

## 7. API Endpoints

FastAPI provides an automatic, interactive API documentation interface accessible at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Primary Endpoints:

| Method | Endpoint | Description | Payload / Params |
|---|---|---|---|
| `GET` | `/abi` | Health check / test endpoint | None |
| `POST` | `/register` | Registers a new user account with hashed password | JSON body (`UserRegisterSchema`) |
| `POST` | `/login` | Authenticates user & generates signed JWT access token | JSON body (`UserLoginRequestSchema`) |
| `GET` | `/verify-token` | Validates JWT token passed via `Authorization: Bearer` header | Header: `Authorization` |
| `GET` | `/user/{id}` | Retrieves user profile by ID (excludes password) | Path parameter: `id` |
| `POST` | `/create-student` | 🔒 Creates a new student record (Requires Bearer JWT) | Header: `Authorization: Bearer <token>`, Body: `StudentSchema` |
| `GET` | `/students` | 🔒 Retrieves all student records (Requires Bearer JWT) | Header: `Authorization: Bearer <token>` |
| `GET` | `/students/{id}` | 🔒 Retrieves a single student by ID (Requires Bearer JWT) | Header: `Authorization: Bearer <token>`, Path: `id` |
| `PUT` | `/students/{id}` | 🔒 Updates existing student & recalculates marks (Requires Bearer JWT) | Header: `Authorization: Bearer <token>`, Body: `StudentSchema` |
| `DELETE`| `/students/{id}` | 🔒 Deletes student record by ID (Requires Bearer JWT) | Header: `Authorization: Bearer <token>`, Path: `id` |

#### Sample Request Body (`POST /create-student`):
```json
{
  "name": "Arun Kumar",
  "email": "arun.kumar@example.com",
  "phonenumber": "9876543210",
  "department": "Computer Science",
  "address": "123, Anna Nagar, Chennai",
  "python_mark": 92,
  "java_mark": 88,
  "database_mark": 95
}
```

#### Sample Response:
```json
{
  "message": "Student create api working",
  "id": 1,
  "name": "Arun Kumar",
  "email": "arun.kumar@example.com",
  "phonenumber": "9876543210",
  "department": "Computer Science",
  "python_mark": 92,
  "java_mark": 88,
  "database_mark": 95,
  "created_at": "2026-09-24T20:15:00",
  "address": "123, Anna Nagar, Chennai",
  "Final Percentage": 91.66666666666667
}
```

---

## 8. Installation & Setup Guide

### Prerequisites
- **Python**: Version 3.10 or higher
- **Node.js**: Version 18.x or higher & npm
- **PostgreSQL Server**: Installed and running locally or remotely

---

### Database Configuration
1. Open PostgreSQL (via `psql` or pgAdmin) and create a database:
   ```sql
   CREATE DATABASE student_db2;
   ```
2. Verify connection credentials (username, password, port, database name).

---

### Backend Setup (FastAPI)

1. Open a terminal and navigate to the backend directory:
   ```bash
   cd "D:\2026\2026 PYTHON CLASS\Batch 4 September\PracticeCode\Day 11 to 15\backend"
   ```

2. Create and activate a Python virtual environment:
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate on Windows (PowerShell)
   .\venv\Scripts\Activate.ps1

   # Activate on Windows (Command Prompt)
   .\venv\Scripts\activate.bat
   ```

3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create/Configure the `.env` file inside `backend/`:
   ```env
   DATABASE_URL=postgresql://<USERNAME>:<PASSWORD>@localhost:5432/student_db2
   ```
   *(Note: URL-encode any special characters in the password, e.g., `@` as `%40`)*

5. Run the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
6. Test in browser:
   - Base URL: `http://localhost:8000`
   - Interactive Docs: `http://localhost:8000/docs`

---

### Frontend Setup (React.js)

1. Navigate to the frontend directory:
   ```bash
   cd "D:\2026\2026 PYTHON CLASS\Batch 4 September\PracticeCode\Day 11 to 15\frontend"
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   # or if using Vite:
   # npm run dev
   ```

4. Access the web application at `http://localhost:3000` (or `http://localhost:5173` if using Vite).

---

## 9. Coding Standards & Best Practices

- **Strict Layer Isolation**:
  - Never execute SQL queries or access the DB session inside route controllers or Pydantic schemas.
  - Route handlers should only call service or repository methods.
- **Data Validation First**:
  - All input contracts must be validated using Pydantic (`EmailStr`, mark ranges).
- **Environment Safety**:
  - Never commit raw passwords or database credentials directly into source control. Always utilize `.env`.
- **CORS Middleware**:
  - Ensure `fastapi.middleware.cors.CORSMiddleware` is configured to allow requests originating from `http://localhost:3000`.
