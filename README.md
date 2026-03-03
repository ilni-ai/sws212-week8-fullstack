# SWS 212 -- Week 8 Full-Stack Application

This project demonstrates a full-stack application using:

-   ⚛ React 19.2 (Vite)
-   ⚡ FastAPI (Python 3.13+)
-   🍃 MongoDB Atlas (Cloud Database)

The application implements full CRUD functionality for managing
students.

------------------------------------------------------------------------

## 🏗 Architecture

Frontend → FastAPI Backend → MongoDB Atlas

-   Frontend runs on: http://localhost:5173
-   Backend runs on: http://localhost:8000
-   API docs available at: http://localhost:8000/docs

------------------------------------------------------------------------

## 📁 Project Structure

    Week_8/
    ├── backend/
    │   ├── core/
    │   ├── models/
    │   ├── routes/
    │   ├── utils/
    │   ├── main.py
    │   └── requirements.txt
    └── frontend/

------------------------------------------------------------------------

## ⚙ Backend Setup (Local)

``` bash
cd backend
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

Create a `.env` file inside `backend/`:

    MONGO_URI=your_mongodb_connection_string
    DB_NAME=college_db

------------------------------------------------------------------------

## ⚛ Frontend Setup (Local)

``` bash
cd frontend
npm install
npm run dev
```

------------------------------------------------------------------------

## 🌐 Deployment Flow (Week 8 Lab)

1.  Develop locally\
2.  Push to GitHub\
3.  Open in GitHub Codespaces\
4.  Deploy backend to Render\
5.  Connect to MongoDB Atlas

------------------------------------------------------------------------

## 🔐 Security Note

The `.env` file is excluded via `.gitignore` and must not be committed.

Production deployments use environment variables configured in Render.
