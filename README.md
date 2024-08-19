# ranking-application
This repository contains a full-stack web application that ranks companies given a search term built using React for the frontend, Flask for the backend, and GraphQL for API queries. Docker and Docker Compose are used for containerization. In addition, a sentence transformer model is utilized for ranking implementation.

## Getting Started

### 1. Clone the Repository
```
 $ git clone https://github.com/abilalakin/ranking-application.git
 $ cd ranking-application
```
### 2. Build and Run the Application with Docker Compose
#### Step 1: Build the Docker Images
```
docker-compose build
```
#### Step 2: Start the Services
```
docker-compose up
```
- The React frontend will be accessible at http://localhost:3000.
- The Flask backend will be accessible at http://localhost:8000.
- The GraphQL API will be accessible at http://localhost:8000/graphql.

#### Step 3: Stopping the Application
```
docker-compose down
```

## Development
If you prefer to run the app locally without Docker:
### Running the Backend Locally
####  Setup a Virtual Environment (Optional/Recommended)
```
python3 -m venv venv
```
- On macOS and Linux:
```
source venv/bin/activate
```
- On Windows:
```
.\venv\Scripts\activate
```
####  Install Requirements and Run the Flask App
```
$ cd backend # Navigate to the backend directory
$ pip install -r requirements.txt # Install the required Python packages
$ python3 -m flask run # Run the Flask application
```
### Running the Frontend Locally
```
$ cd ui # Navigate to the frontend directory
$ npm install # Install the required npm packages
$ npm start # Start the React development server
```
