🚀 Full-Stack Portfolio Application

A production-ready React + FastAPI + PostgreSQL portfolio application designed to showcase Projects, Skills, About info, and Contact submissions through a modern full-stack architecture.

This project demonstrates real software engineering ability: backend API design, database modeling, frontend development, API integration, and deployment.

📌 Features
⭐ Frontend (React + Vite + TailwindCSS)

Modern React app using Vite

Fast development + HMR

TailwindCSS styling

Axios for API calls

Fully responsive portfolio UI (Projects, Skills, About, Contact)

Easy to deploy (Vercel / Netlify)

⭐ Backend (FastAPI + SQLAlchemy + PostgreSQL)

Fully RESTful API

CRUD Operations for:
✔ About
✔ Skills
✔ Projects
✔ Contact messages

PostgreSQL database

Auto timestamping

Clean router structure

Pydantic v2 schemas

Swagger docs included

🗂️ Project Structure
portfolio/
│── backend/
│     ├── app/
│     │     ├── main.py
│     │     ├── core/
│     │     ├── models/
│     │     ├── schemas/
│     │     └── routers/
│     ├── requirements.txt
│
│── frontend/
│     ├── src/
│     ├── public/
│     ├── package.json
│     └── vite.config.js
│
│── .gitignore
│── README.md

⚙️ Backend Setup
1️⃣ Create and activate virtual environment
cd backend
python3 -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Configure database

Located in: backend/app/core/database.py

DATABASE_URL = "postgresql://username:password@localhost:5432/portfolio"

4️⃣ Run API server
uvicorn app.main:app --reload


API Docs:
👉 http://127.0.0.1:8000/docs

🎨 Frontend Setup
1️⃣ Install dependencies
cd frontend
npm install

2️⃣ Run development server
npm run dev


Frontend runs at:
👉 http://localhost:5173

🔌 API Endpoints
📘 About
Method	Endpoint	Description
GET	/about/	Get about info
POST	/about/	Create about info
PUT	/about/{id}	Update about info
DELETE	/about/{id}	Delete about section
📗 Skills
Method	Endpoint	Description
GET	/skills/	Get all skills
POST	/skills/	Add skill
PUT	/skills/{id}	Update skill
DELETE	/skills/{id}	Delete skill
📙 Projects
Method	Endpoint	Description
GET	/projects/	Get all projects
GET	/projects/{id}	Get single project
POST	/projects/	Add project
PUT	/projects/{id}	Update project
DELETE	/projects/{id}	Delete project
📕 Contact
Method	Endpoint	Description
GET	/contact/	Get all messages
POST	/contact/	Submit user message
DELETE	/contact/{id}	Delete message
🌐 Connecting Frontend → Backend

Create file:

frontend/src/api.js


Add:

export const API_BASE = "http://127.0.0.1:8000";


Use example:

import axios from "axios";
import { API_BASE } from "./api";

const res = await axios.get(`${API_BASE}/skills/`);

🚀 Deployment Guide
Backend Deployment (Render / Railway / Fly.io)

Push backend folder to GitHub

Deploy FastAPI service

Configure environment variables

Deploy PostgreSQL database

Update frontend API URL

Frontend Deployment (Vercel / Netlify)
npm run build


Deploy folder:

dist/


Environment variable:

VITE_API_URL=https://your-backend-url.com

🧪 Testing
Backend Testing

Run Swagger UI:
👉 http://127.0.0.1:8000/docs

Frontend Testing

Use browser console + Network tab.

👨‍💻 Author

Shamar Weekes
Full-Stack Developer • Cybersecurity • AI • FIU CS

This application demonstrates:

Full-stack web engineering

Database modeling + API architecture

Professional frontend development

Deployment-ready folder structure

Real-world project development