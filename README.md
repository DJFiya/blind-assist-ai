# Blind Assist AI

Blind Assist AI is a vision-based assistive system designed to help blind and visually impaired users understand their surroundings through real-time camera input, computer vision, and conversational AI.

The system captures live video from a camera, sends frames to the 12 Labs API for scene understanding, and passes the resulting description to Gemini AI, which answers user questions about the environment. The responses are delivered via text-to-speech for hands-free accessibility. All interactions are securely stored in MongoDB and accessed through an Auth0-protected dashboard built with a React frontend deployed on Vercel.

Developed in 36 hours at Hack the 6ix 2025.

## How It Works

1. A camera captures the current scene.
2. The image is sent to the 12 Labs API, which returns a detailed description of objects, actions, and spatial information.
3. The description forms the context for Gemini AI, which responds to user questions such as:
   - “Is there someone near me?”
   - “What objects are on my right?”
4. Gemini’s answers are converted to speech using text-to-speech technology.
5. All scene descriptions, questions, and answers are stored in MongoDB for review.
6. A web dashboard secured with Auth0 allows users to log in and view past scenes and interactions.

## Tech Stack

- **Computer Vision:** 12 Labs API
- **Conversational AI:** Gemini API
- **Text-to-Speech:** pyttsx3 or gTTS
- **Backend:** Python with FastAPI
- **Frontend:** React generated with Vercel v0
- **Authentication:** Auth0
- **Database:** MongoDB Atlas
- **Deployment:** Vercel (frontend), optional Render or other for backend

## Setup Instructions

### Backend

1. Clone the repo and navigate to the backend directory.
2. Create a Python virtual environment and activate it:
    ```bash
    python -m venv .venv  
    source .venv/bin/activate    # Windows: .venv\Scripts\activate  
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt  
    ```
4. Create a `.env` file with your API keys and connection strings:
    ```ini
    TWELVE_LABS_API_KEY=your_12labs_key  
    GEMINI_API_KEY=your_gemini_key  
    MONGODB_URI=your_mongodb_connection_string  
    AUTH0_CLIENT_ID=your_auth0_client_id  
    AUTH0_DOMAIN=your_auth0_domain  
    ```
5. Start the FastAPI backend:
    ```bash
    uvicorn app:app --reload  
    ```

### Frontend

1. Use https://v0.dev to generate a React dashboard with Auth0 authentication.
2. Modify API endpoints to connect to your backend.
3. Deploy the frontend to Vercel with:
    ```bash
    vercel deploy  
    ```
4. Users can log in, view scene history, ask questions, and hear answers.

This project demonstrates how computer vision and natural language processing can empower users with visual impairments to better navigate and understand their environments in real time.

Thank you for reviewing our submission!
