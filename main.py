import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

# Project imports
from models.chat import ChatRequest, ChatResponse, UserProfileUpdate, UserMemory
from memory.memory_store import get_user_memory_data, update_user_memory_data
from ollama_utils import generate_ollama_response

# Load environment variables
load_dotenv()

app = FastAPI(
    title="MindMate AI Assistant Backend",
    description="FastAPI app for empathetic chat interactions with memory, powered by Ollama + LLaMA2.",
    version="1.1.3"
)

# CORS configuration (for hackathon MVP)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", summary="Health check")
async def root():
    return {"message": "MindMate AI Assistant Backend is up and running!"}

# -- Helper Functions --

def refine_response(raw: str) -> str:
    """
    Clean up the raw LLM output:
      - Remove unwanted prefixes/emojis
      - Dedupe and strip empty lines
    Also limit to first 3 lines for brevity.
    """
    # Remove unwanted tokens
    for token in ["Bot:", "MindMate:", "bot:", "mindmate:", "😊", "🤗"]:
        raw = raw.replace(token, "")
    # Split and dedupe
    lines = [l.strip() for l in raw.split("\n")]
    seen = set()
    out = []
    for line in lines:
        if line and line not in seen:
            seen.add(line)
            out.append(line)
    # Limit to first 3 lines
    return "\n".join(out[:3])


def inject_tail_motivation(user_message: str) -> str:
    """
    Optionally append a motivational line based on keywords.
    """
    txt = user_message.lower()
    if any(k in txt for k in ["breakup", "heartbreak", "rejected", "broke up"]):
        return "\nKeep going—each step forward is progress. 💪"
    if any(k in txt for k in ["succeed", "success", "goal", "motivation"]):
        return "\nYou have what it takes—keep believing in yourself. 🚀"
    return ""

@app.post("/chat", response_model=ChatResponse, summary="Chat with MindMate")
async def chat_endpoint(request: ChatRequest):
    user_id = request.user_id
    user_msg = request.message.strip()

    # 1. Load memory and chat history
    memory = get_user_memory_data(user_id) or {}
    history = memory.get("chat_history", [])

    # 2. System prompt instructing brevity and format
    PRE_PROMPT = (
        "You are MindMate, an emotionally intelligent AI mental wellness assistant.\n"
        "Respond in 1-3 concise lines separated by '\n'.\n"
        "Do NOT prefix lines with any labels."

    )

    # 3. Append recent conversation history (last 5 turns only to keep relevant)
    recent = history[-10:]
    history_txt = "\n".join([f"{turn['role'].capitalize()}: {turn['message']}" for turn in recent])

    # 4. Construct final prompt
    full_prompt = f"{PRE_PROMPT}\n{history_txt}\nUser: {user_msg}\nMindMate:"

    # 5. Query Ollama
    raw = generate_ollama_response(full_prompt).strip()

    # 6. Clean, refine, and limit output
    clean = refine_response(raw)
    tail = inject_tail_motivation(user_msg)
    reply = clean + tail

    # 7. Update chat history in memory
    history.append({"role": "user", "message": user_msg})
    history.append({"role": "bot",  "message": reply})
    update_user_memory_data(user_id, {"chat_history": history[-20:]})

    return ChatResponse(response=reply, user_memory_updated=True)

@app.post("/update_user_profile", response_model=ChatResponse, summary="Update user profile")
async def update_user_profile(user_profile: UserProfileUpdate):
    data = user_profile.dict(exclude_unset=True)
    uid  = data.pop("user_id", None)
    if not uid or not data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid profile data.")
    update_user_memory_data(uid, data)
    return ChatResponse(response="Profile updated.", user_memory_updated=True)

@app.get("/get_user_profile/{user_id}", response_model=UserMemory, summary="Get user profile")
async def get_user_profile(user_id: str):
    data = get_user_memory_data(user_id) or {}
    return UserMemory(**data, user_id=user_id)

