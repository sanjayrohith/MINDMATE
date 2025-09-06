# MVP_MIND_MATE/models/chat.py
from typing import Optional, Dict, Any
from pydantic import BaseModel


class UserMemory(BaseModel):
    user_id: str
    name: Optional[str] = None
    recent_mood: Optional[str] = None
    career_goals: Optional[str] = None
    last_session_summary: Optional[str] = None
    # Add any other user-specific details you want to remember


class ChatRequest(BaseModel):
    user_id: str
    message: str


class ChatResponse(BaseModel):
    response: str
    user_memory_updated: bool = False


class UserProfileUpdate(BaseModel):
    user_id: str
    name: Optional[str] = None
    recent_mood: Optional[str] = None
    career_goals: Optional[str] = None
    last_session_summary: Optional[str] = None
    # Fields for direct profile updates, useful for a "settings" page
