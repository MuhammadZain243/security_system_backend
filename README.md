# Security System Backend

Backend API for the **Security System**, a configurable, multi-tenant SaaS platform designed for private security companies.

The backend is built with **FastAPI** and acts as the communication layer between the frontend applications and the database package.

---

## Contents

- [Description](#description)
- [System Architecture](#system-architecture)
- [Backend Responsibilities](#backend-responsibilities)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Initial Installation](#initial-installation)
- [Environment Configuration](#environment-configuration)
- [Running the Application](#running-the-application)
- [Available Endpoints](#available-endpoints)
- [API Documentation](#api-documentation)
- [Dependency Management](#dependency-management)
- [Database Package Integration](#database-package-integration)
- [Development Commands](#development-commands)
- [Git Workflow](#git-workflow)
- [Current Scope](#current-scope)
- [Future Backend Modules](#future-backend-modules)
- [Project Rules](#project-rules)

---

## Description

The **Security System Backend** is the API and business-logic layer of the Security System SaaS platform.

The platform is intended for private security companies that currently use separate systems for workforce management, employee management, property management, scheduling, payments, attendance, reporting, and other operational activities.

The purpose of the Security System is to provide these capabilities through one configurable platform.

The system is designed to support multiple security companies. Each company will operate as an independent tenant with its own users, roles, permissions, workflows, statuses, settings, and operational data.

The backend will expose APIs that allow frontend applications to securely communicate with the database layer.

This repository contains backend-related code only.

Database models, schemas, migrations, and database-specific configuration are maintained separately inside the `security_system_database` repository.

---

## System Architecture

The Security System follows a three-tier architecture:

```text
┌───────────────────────────────┐
│       Frontend Layer          │
│                               │
│ Web portals and user          │
│ interfaces                    │
└───────────────┬───────────────┘
                │
                │ HTTP / REST API
                ▼
┌───────────────────────────────┐
│        Backend Layer          │
│                               │
│ FastAPI, business logic,      │
│ authentication, permissions,  │
│ validation and integrations   │
└───────────────┬───────────────┘
                │
                │ Database package
                ▼
┌───────────────────────────────┐
│        Database Layer         │
│                               │
│ PostgreSQL, SQLAlchemy        │
│ models and Alembic migrations │
└───────────────────────────────┘
```

The three main repositories are expected to be:

```text
security_system/
├── security_system_database/
├── security_system_backend/
└── security_system_frontend/
```

---

## Backend Responsibilities

The backend layer will eventually be responsible for:

- Exposing REST APIs
- Validating incoming requests
- Executing business rules
- Authenticating users
- Managing authorization
- Resolving the active tenant
- Enforcing tenant isolation
- Managing database transactions
- Connecting the frontend with the database
- Integrating external services
- Processing payments
- Sending notifications
- Managing background operations
- Returning consistent API responses
- Handling and logging application errors

The backend will not define database tables or database migrations.

---

## Technology Stack

The initial backend uses:

| Technology | Purpose                                           |
| ---------- | ------------------------------------------------- |
| Python     | Primary backend programming language              |
| FastAPI    | API framework                                     |
| Uvicorn    | ASGI development server                           |
| uv         | Python dependency and virtual-environment manager |
| Git        | Source-control management                         |

Additional packages will be added only when their related functionality is implemented.

---

## Project Structure

The initial project structure is intentionally minimal:

```text
security_system_backend/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── .env.example
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
└── uv.lock
```

### Structure Description

#### `app/`

Contains the FastAPI backend application.

#### `app/__init__.py`

Marks the `app` directory as a Python package.

#### `app/main.py`

Contains the initial FastAPI application and basic endpoints.

#### `.env.example`

Documents the environment variables required by the application.

The actual `.env` file must not be committed to Git.

#### `.gitignore`

Defines files and directories that should not be tracked by Git.

#### `.python-version`

Defines the Python version used by the project.

#### `pyproject.toml`

Contains project metadata and dependency definitions.

#### `uv.lock`

Contains the exact resolved dependency versions.

This file should be committed to Git so installations remain consistent across different development and deployment environments.

#### `README.md`

Contains project documentation, setup instructions, commands, architecture details, and development rules.

---

## Prerequisites

Install the following software before setting up the project:

- Git
- Python
- uv

Verify the installations:

```bash
git --version
python --version
uv --version
```

The project should use the Python version declared inside `.python-version`.

---

## Initial Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd security_system_backend
```

### 2. Install dependencies

```bash
uv sync
```

This command creates the project virtual environment and installs the dependencies defined in `pyproject.toml`.

The environment is normally created at:

```text
.venv/
```

### 3. Create the environment file

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

On Linux or macOS:

```bash
cp .env.example .env
```

Update the values in `.env` according to the local environment.

---

## Environment Configuration

The initial `.env.example` contains:

```dotenv
APP_NAME="Security System API"
APP_VERSION="0.1.0"
APP_ENV="development"

HOST="127.0.0.1"
PORT=8000
```

### Environment Variables

| Variable      | Description                    | Default               |
| ------------- | ------------------------------ | --------------------- |
| `APP_NAME`    | Application display name       | `Security System API` |
| `APP_VERSION` | Current backend version        | `0.1.0`               |
| `APP_ENV`     | Active application environment | `development`         |
| `HOST`        | Development server host        | `127.0.0.1`           |
| `PORT`        | Development server port        | `8000`                |

The actual `.env` file must never be committed to the repository.

---

## Running the Application

Start the development server:

```bash
uv run uvicorn app.main:app --reload
```

The command components are:

```text
uv run
```

Runs the command inside the project environment.

```text
uvicorn
```

Starts the ASGI server.

```text
app.main:app
```

Imports the `app` FastAPI instance from `app/main.py`.

```text
--reload
```

Restarts the development server automatically when source files change.

To explicitly provide the host and port:

```bash
uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Stop the server with:

```text
Ctrl + C
```

---

## Available Endpoints

### Root Endpoint

```http
GET /
```

Example response:

```json
{
  "message": "Security System API is running.",
  "version": "0.1.0"
}
```

### Health Endpoint

```http
GET /health
```

Example response:

```json
{
  "status": "healthy"
}
```

The health endpoint confirms that the backend application is running.

Database and external-service health checks will be added later.

---

## API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows developers to:

- View available endpoints
- Inspect request schemas
- Inspect response schemas
- Test endpoints from the browser
- Review validation errors

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

ReDoc provides a documentation-focused view of the API.

### OpenAPI Schema

```text
http://127.0.0.1:8000/openapi.json
```

The OpenAPI schema can later be used for:

- Frontend API client generation
- External integrations
- Automated documentation
- API testing
- Contract validation

---

## Dependency Management

This project uses `uv` for dependency and environment management.

### Install all project dependencies

```bash
uv sync
```

### Add a runtime dependency

```bash
uv add package-name
```

Example:

```bash
uv add pydantic-settings
```

### Add a development dependency

```bash
uv add --dev package-name
```

Example:

```bash
uv add --dev pytest
```

### Remove a dependency

```bash
uv remove package-name
```

### Run a command inside the project environment

```bash
uv run <command>
```

Example:

```bash
uv run python --version
```

### Display the dependency tree

```bash
uv tree
```

### Update the lock file

```bash
uv lock
```

### Update installed dependencies

```bash
uv sync --upgrade
```

Do not manually edit `uv.lock`.

---

## Database Package Integration

The database layer is maintained in a separate repository:

```text
security_system_database
```

It is responsible for:

- SQLAlchemy models
- PostgreSQL schemas
- Database metadata
- Alembic migrations
- Database migration commands
- Database engine configuration
- Database session utilities
- Database package releases

The backend repository must not contain:

```text
models/
migrations/
alembic/
alembic.ini
```

During local development, the database package can later be installed from the neighboring repository:

```bash
uv add --editable ../security_system_database
```

The expected parent structure is:

```text
security_system/
├── security_system_database/
└── security_system_backend/
```

For controlled environments, the backend should consume a released and pinned version of the database package.

Example:

```bash
uv add "security-system-database @ git+https://github.com/<organization>/security_system_database.git@v0.1.0"
```

The exact package name and repository address must match the database project configuration.

Database integration is not part of the initial backend setup.

---

## Development Commands

### Start the backend

```bash
uv run uvicorn app.main:app --reload
```

### Start with a custom host and port

```bash
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Synchronize dependencies

```bash
uv sync
```

### Add a dependency

```bash
uv add package-name
```

### Add a development dependency

```bash
uv add --dev package-name
```

### Remove a dependency

```bash
uv remove package-name
```

### View installed dependencies

```bash
uv tree
```

### Run Python

```bash
uv run python
```

### Check the Python version

```bash
uv run python --version
```

---

## Git Workflow

Check the repository status:

```bash
git status
```

Add files:

```bash
git add .
```

Create the initial commit:

```bash
git commit -m "chore: initialize FastAPI backend"
```

Add the remote repository:

```bash
git remote add origin <repository-url>
```

Push the initial branch:

```bash
git branch -M main
git push -u origin main
```

The following files should normally be committed:

```text
app/
.env.example
.gitignore
.python-version
pyproject.toml
README.md
uv.lock
```

The following files should not be committed:

```text
.env
.venv/
__pycache__/
IDE configuration
local logs
```

---

## Current Scope

The initial backend currently provides:

- A Python project managed with `uv`
- A FastAPI application
- A root endpoint
- A basic health endpoint
- Automatic Swagger documentation
- Automatic ReDoc documentation
- Environment-variable documentation
- Git configuration
- Project setup and execution instructions

The initial setup intentionally does not include complex architecture or unused packages.

---

## Future Backend Modules

The project structure will be expanded only when required.

Future backend areas may include:

```text
app/
├── api/
├── core/
├── dependencies/
├── middleware/
├── schemas/
├── services/
├── repositories/
├── integrations/
└── modules/
```

Possible business modules include:

- Authentication
- Tenant management
- Company management
- User management
- Role management
- Dynamic permissions
- Properties and sites
- Guard management
- Shift management
- Scheduling
- Attendance
- Leave management
- Incident management
- Task management
- Payroll
- Billing
- Payments
- Notifications
- Reports
- Audit logs
- Company settings
- Dynamic statuses
- Dynamic workflows

These directories and modules should be added only when their implementation phase begins.

---

## Project Rules

### 1. Maintain repository separation

Database models and migrations belong in `security_system_database`.

Backend APIs and business logic belong in `security_system_backend`.

Frontend interfaces belong in the frontend repository.

### 2. Avoid premature complexity

Do not create modules, abstractions, or dependencies until they are required by an active feature.

### 3. Avoid duplicated database definitions

The backend must consume the database package instead of copying models from it.

### 4. Keep tenant isolation mandatory

Every tenant-owned operation must eventually be scoped to the active tenant.

### 5. Keep configuration outside source code

Environment-specific values must be stored in environment variables rather than hardcoded into application files.

### 6. Protect secrets

Passwords, API keys, database credentials, and signing secrets must never be committed to Git.

### 7. Pin database package releases

Deployed backend versions should depend on a known database package version.

### 8. Keep API contracts consistent

Request validation, response schemas, errors, pagination, and API versioning should follow shared backend standards once introduced.

### 9. Add functionality in phases

The recommended implementation order is:

```text
1. Initial backend configuration
2. Application settings
3. Database package integration
4. Database session management
5. Common API responses and errors
6. Authentication
7. Tenant resolution
8. Dynamic authorization
9. Business modules
10. External integrations
11. Deployment configuration
```
