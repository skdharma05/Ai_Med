# AI Meditation Backend

This is a backend service for generating meditation scripts and audio using Google Gemini AI, Google Cloud Text-to-Speech, and MongoDB.

---

## Features

- Generate meditation scripts with Google Gemini AI
- Synthesize meditation audio with Google Cloud Text-to-Speech
- Store and retrieve user sessions with MongoDB

---

## Prerequisites

- Python 3.10+
- [Google Cloud account](https://console.cloud.google.com/)
- [MongoDB Atlas account](https://www.mongodb.com/cloud/atlas)
- Google Gemini API key

---

## Installation

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd ai_meditation_backend/ai_meditation_backend
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   venv\Scripts\activate   # On Windows
   # source venv/bin/activate   # On Mac/Linux
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root with the following content:
   ```
   GOOGLE_APPLICATION_CREDENTIALS=service_account.json
   MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/meditation_db
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

   - Download your Google Cloud service account JSON and place it in the project directory as `service_account.json`.
   - Replace `<username>` and `<password>` in `MONGODB_URI` with your MongoDB Atlas credentials.
   - Replace `your_gemini_api_key_here` with your Gemini API key.

---

## Running the Server

```sh
uvicorn main:app --reload
```
*(Replace `main:app` with your actual FastAPI entrypoint if different.)*

---

## API Endpoints

- `POST /generate-script`  
  Generate a meditation script using Gemini AI.

- `GET /get-audio/:filename`  
  Retrieve generated audio files.

- `GET /history/:user_id`  
  Get user session history.

---

## Notes

- Ensure your Google Cloud and MongoDB credentials are kept secure.
- Do **not** commit your `.env` or `service_account.json` to public repositories.

---

## License

MIT