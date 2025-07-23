from pydantic import BaseModel
from typing import Dict, Any

class MeditationSession(BaseModel):
    user_id: str
    session_data: Dict[str, Any]
