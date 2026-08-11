# Deployment Guide

## Backend

Install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

Run API server:

```bash
uvicorn app.main:app --reload
```

API will run on:

```
http://localhost:8000
```

## Frontend

Install dependencies:

```bash
cd frontend
npm install
```

Run development server:

```bash
npm run dev
```

## Production Roadmap

Planned deployment:

- Frontend: Vercel
- Backend: Render / Railway
- Database: PostgreSQL
