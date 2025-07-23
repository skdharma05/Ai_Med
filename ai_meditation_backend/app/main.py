from fastapi import FastAPI
from app.schemas import ScriptRequest
from app.gemini_script_generator import generate_script_with_gemini as generate_script
from app.tts_service import synthesize_speech
from app.db import sessions_collection
from datetime import datetime
import os
from fastapi.responses import FileResponse

app = FastAPI()

@app.post("/generate-script")
def create_script(data: ScriptRequest, user_id: str = "guest"):
    script = generate_script(data.duration_minutes, data.difficulty, data.theme)

    for i, segment in enumerate(script["segments"]):
        for j, action in enumerate(segment["actions"]):
            if action["type"] == "speak":
                text = action["parameters"]["text"]
                filename = f"{user_id}_seg{i}_act{j}"
                synthesize_speech(text, filename)
                action["audio_url"] = f"/get-audio/{filename}"

    # Store in MongoDB
    sessions_collection.insert_one({
        "user_id": user_id,
        "timestamp": datetime.utcnow(),
        "session_data": script
    })

    return script

@app.get("/get-audio/{filename}")
def get_audio(filename: str):
    filepath = f"audio/{filename}.mp3"
    if os.path.exists(filepath):
        return FileResponse(filepath, media_type="audio/mpeg")
    return {"error": "Audio not found"}

@app.get("/history/{user_id}")
def get_history(user_id: str):
    sessions = sessions_collection.find({"user_id": user_id})
    history = []
    for s in sessions:
        s["_id"] = str(s["_id"])
        history.append(s)
    return history
