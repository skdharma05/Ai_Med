from pydantic import BaseModel

class ScriptRequest(BaseModel):
    duration_minutes: int
    difficulty: str
    theme: str
