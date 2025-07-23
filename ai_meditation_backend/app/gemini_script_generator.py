import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_script_with_gemini(duration_minutes, difficulty, theme):
    prompt = f"""
You are a meditation script generator.

Generate a meditation program in JSON format based on:
- Duration: {duration_minutes} minutes
- Difficulty: {difficulty}
- Theme: {theme}

JSON structure must follow this format:
{{
  "title": "string",
  "duration_seconds": number,
  "theme": "string",
  "difficulty": "string",
  "background_music": "string",
  "segments": [
    {{
      "title": "string",
      "type": "string",
      "start_time_seconds": number,
      "end_time_seconds": number,
      "actions": [
        {{
          "type": "speak",
          "start_time_seconds": number,
          "duration_seconds": number,
          "parameters": {{
            "text": "string"
          }}
        }}
      ]
    }}
  ]
}}

Only return valid JSON.
"""

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    try:
        json_output = json.loads(response.text)
        return json_output
    except Exception as e:
        return {"error": "Invalid JSON from Gemini", "raw": response.text}
