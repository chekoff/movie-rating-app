# Movie Rating App

## Description
A simple multi-user movie rating app using React + Flask + SQLite. All data is stored locally.

## Features
- Select username before rating
- Rate predefined movies
- Ratings saved with timestamps in SQLite DB
- Backend returns the rating payload including the timestamp

## Gitpod Setup
1. Fork this repository to your GitHub account
2. Open it in Gitpod by prefixing the repo URL with `https://gitpod.io/#`

   Example:
   ```
   https://gitpod.io/#https://github.com/yourusername/movie-rating-app
   ```
3. Wait for the workspace to initialize — it will set up the backend and frontend automatically

## Local Setup

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install flask flask-cors
python init_db.py  # Initializes movies.db with tables and sample data
python app.py      # Starts backend server at http://localhost:5000
```

### Frontend
```bash
cd frontend
npm install
npm start          # Starts React frontend at http://localhost:3000
```

## Candidate Task
> Add a timestamp column to the `ratings` table (already done) and make sure it is returned in the response payload of `/rate`.

**Hint:** You may extend the returned payload or format the timestamp for better readability.

## Notes
- App is entirely offline
- No cloud dependencies
- For test purposes only
