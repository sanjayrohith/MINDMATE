#memory_store.py

import json
from pathlib import Path
from typing import Dict, Any, Optional

MEMORY_FILE = Path("memory.json")

def load_all_memory() -> Dict[str, Any]:
    if not MEMORY_FILE.exists():
        return {}
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Warning: {MEMORY_FILE} is empty or malformed. Starting with empty memory.")
        return {}

def save_all_memory(data: Dict[str, Any]):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_user_memory_data(user_id: str) -> Optional[Dict[str, Any]]:
    all_memory = load_all_memory()  # ✅ FIXED
    user_data = all_memory.get(user_id)
    if user_data is not None:
        user_data["user_id"] = user_id  # ✅ inject user_id
    return user_data

def update_user_memory_data(user_id: str, new_data: Dict[str, Any]):
    all_memory = load_all_memory()
    current_user_data = all_memory.get(user_id, {})
    current_user_data.update(new_data)
    all_memory[user_id] = current_user_data
    save_all_memory(all_memory)

if not MEMORY_FILE.exists():
    save_all_memory({})
