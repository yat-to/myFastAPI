# 🚀 FastAPI Backend Setup Guide

This guide explains the steps to easily run a backend using **FastAPI**.

---

## 📦 1. Initial Setup

Make sure you have installed:

* Python ≥ 3.8
* pip (Python package manager)

Check versions:

```bash
python --version
pip --version
```

---

## 🏗️ 2. Create Project

Create a project folder:

```bash
mkdir fastapi-backend
cd fastapi-backend
```

---

## 🧪 3. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

### Mac / Linux:

```bash
source venv/bin/activate
```

### Windows:

```bash
venv\Scripts\activate
```

---

## 📥 4. Install Dependencies

```bash
pip install fastapi uvicorn
```

---

## 📝 5. Create Main File

Create a file named `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello FastAPI 🚀"}

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Hidayat"},
        {"id": 2, "name": "Developer"}
    ]
```

---

## ▶️ 6. Run the Server

```bash
uvicorn app.main:app --reload
```

Explanation:

* `main` = file name (main.py)
* `app` = FastAPI instance
* `--reload` = auto reload during development

---

## 🌐 7. Access the API

Open in your browser:

### Main Endpoint:

```
http://localhost:8000/
```

### Swagger Documentation:

```
http://localhost:8000/docs
```

### Alternative Docs:

```
http://localhost:8000/redoc
```

---

## 🔥 8. Project Structure (Recommended)

```
fastapi-backend/
│
├── app/
│   ├── main.py
│   ├── routers/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── database/
│
├── venv/
├── requirements.txt
└── README.md
```

---

## 📄 9. Generate Requirements

```bash
pip freeze > requirements.txt
```

Install dependencies in another project:

```bash
pip install -r requirements.txt
```

---

## 🛑 10. Stop Server

Press:

```
CTRL + C
```

---

## 🎯 Notes

* FastAPI automatically provides API documentation (Swagger)
* Suitable for modern REST APIs
* Supports async and high performance

---

## 🚀 Next Step

Further development:

* Add database (MySQL / PostgreSQL)
* Implement JWT Authentication
* Apply modular structure (router, service, etc.)

---

Happy Coding! 🔥
