# MVP_MIND_MATE/ollama_utils.py
import os
import requests
from dotenv import load_dotenv


load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama2")  # Default model


def generate_ollama_response(prompt: str) -> str:
    """
    Sends a prompt to the Ollama API and returns the generated response.
    """
    ollama_api_url = f"{OLLAMA_HOST}/api/generate"
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False  # For simplicity, not streaming for now
    }
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(ollama_api_url, headers=headers, json=payload, timeout=300)  # Increased timeout
        response.raise_for_status()  # Raise an exception for HTTP errors

        ollama_data = response.json()
        llm_response_content = ollama_data.get("response", "Error: No response from LLM.")
        return llm_response_content

    except requests.exceptions.Timeout:
        print(f"Error: Ollama request timed out after 300 seconds.")
        return "Sorry, the AI is taking too long to respond. Please try again later."
    except requests.exceptions.ConnectionError:
        print(f"Error: Could not connect to Ollama at {OLLAMA_HOST}. Is it running?")
        return "Sorry, I can't connect to my brain right now. Please check the backend."
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama: {e}")
        return f"An error occurred with the AI: {e}"
    except json.JSONDecodeError:  # Should be imported if used directly, but requests.json() handles it
        print("Error decoding Ollama response.")
        return "An unexpected error occurred with the AI response format."
