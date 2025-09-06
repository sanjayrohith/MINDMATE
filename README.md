# 🧠 MINDMATE - AI-Powered Memory Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18+-blue.svg)](https://reactjs.org/)

MINDMATE is an intelligent AI chat companion that remembers your conversations, understands your mood, and provides empathetic responses powered by Ollama and LLaMA2. Built with a beautiful, responsive web interface and a robust FastAPI backend.

## ✨ Features

- 🧠 **Persistent Memory**: Remembers user preferences, mood, and conversation history
- 💬 **Empathetic Conversations**: AI responses tailored to your emotional state
- 🎨 **Beautiful UI**: Modern, responsive interface with smooth animations
- 🔄 **Real-time Chat**: Instant messaging with typing indicators
- 👤 **User Profiles**: Personalized experience with mood tracking and career goals
- 🌙 **Dark/Light Mode**: Adaptive theme support
- 🚀 **Fast & Scalable**: Built with FastAPI for high-performance backend
- 🔒 **Privacy-First**: All data stored locally with optional cloud sync

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **Ollama** - Local LLM inference engine
- **LLaMA2** - Meta's large language model
- **Pydantic** - Data validation and settings management
- **Python 3.8+** - Core programming language

### Frontend
- **React 18** - Modern UI library
- **Tailwind CSS** - Utility-first CSS framework
- **Babel** - JavaScript compiler
- **HTML5** - Semantic markup

### Infrastructure
- **JSON** - Local data persistence
- **CORS** - Cross-origin resource sharing
- **Environment Variables** - Configuration management

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed and running
- LLaMA2 model pulled in Ollama

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sanjayrohith/MINDMATE.git
   cd MINDMATE
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn python-dotenv requests pydantic
   ```

3. **Set up Ollama**
   ```bash
   # Install Ollama (if not already installed)
   # Visit https://ollama.ai/ for installation instructions
   
   # Pull the LLaMA2 model
   ollama pull llama2
   ```

4. **Configure environment variables**
   ```bash
   # Create a .env file (optional)
   echo "OLLAMA_HOST=http://localhost:11434" > .env
   echo "OLLAMA_MODEL=llama2" >> .env
   ```

5. **Start the backend server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

6. **Open the frontend**
   - Open `index.html` in your web browser
   - Or serve it with a local server:
   ```bash
   python -m http.server 3000
   ```

## 📚 API Documentation

Once the server is running, visit:
- **Interactive API Docs**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc

### Key Endpoints

#### Chat with AI
```http
POST /chat
```

**Request Body:**
```json
{
  "user_id": "user123",
  "message": "Hello, how are you today?"
}
```

**Response:**
```json
{
  "response": "Hello! I'm doing great, thank you for asking. How are you feeling today?",
  "user_memory_updated": true
}
```

#### Update User Profile
```http
POST /update_user_profile
```

**Request Body:**
```json
{
  "user_id": "user123",
  "name": "John Doe",
  "recent_mood": "happy",
  "career_goals": "Software Developer",
  "last_session_summary": "Discussed career goals and coding projects"
}
```

#### Get User Memory
```http
GET /user_memory/{user_id}
```

## 🏗️ Project Structure

```
MINDMATE/
├── 📄 main.py                 # FastAPI application entry point
├── 🌐 index.html              # React frontend application
├── 🔧 ollama_utils.py         # Ollama API integration utilities
├── 📊 models/
│   └── chat.py                # Pydantic models for API requests/responses
├── 💾 memory/
│   └── memory_store.py        # User memory management system
├── 🗂️ memory.json             # Local user data storage
├── 🚫 .gitignore              # Git ignore rules
└── 📖 README.md               # Project documentation
```

## 🎨 Features in Detail

### Memory System
MINDMATE's memory system tracks:
- **User Identity**: Name and unique ID
- **Emotional State**: Recent mood and emotional patterns
- **Career Information**: Professional goals and aspirations
- **Session History**: Summaries of previous conversations
- **Contextual Learning**: Adaptive responses based on user history

### Conversation Flow
1. User sends a message through the web interface
2. Backend retrieves user's memory and context
3. AI generates empathetic response using LLaMA2
4. Response is refined and cleaned for optimal presentation
5. User memory is updated with new conversation insights
6. Response is sent back to the frontend with smooth animations

### UI/UX Features
- **Responsive Design**: Works seamlessly on desktop and mobile
- **Typing Indicators**: Visual feedback during AI response generation
- **Message Bubbles**: Distinct styling for user and AI messages
- **Smooth Animations**: CSS transitions for enhanced user experience
- **Accessibility**: ARIA labels and keyboard navigation support

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OLLAMA_HOST` | `http://localhost:11434` | Ollama server endpoint |
| `OLLAMA_MODEL` | `llama2` | LLM model to use |

### Customization

#### Changing the AI Model
```python
# In .env file
OLLAMA_MODEL=codellama  # or any other Ollama model
```

#### Adjusting Response Length
```python
# In main.py, modify the refine_response function
def refine_response(raw: str) -> str:
    # Modify the line limit here
    return "\n".join(out[:5])  # Change from 3 to 5 lines
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 for Python code
- Use semantic commit messages
- Add tests for new features
- Update documentation as needed
- Ensure cross-platform compatibility

## 🐛 Troubleshooting

### Common Issues

**Ollama Connection Error**
```bash
# Ensure Ollama is running
ollama serve

# Check if the model is available
ollama list
```

**CORS Issues**
- Ensure the frontend is served from an allowed origin
- Check CORS middleware configuration in `main.py`

**Memory File Permissions**
```bash
# Ensure write permissions for memory.json
chmod 644 memory.json
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Meta AI** for the LLaMA2 model
- **Ollama** team for the excellent local inference engine
- **FastAPI** community for the amazing framework
- **React** team for the powerful UI library
- **Tailwind CSS** for the beautiful styling system

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/sanjayrohith/MINDMATE/issues)
- **Discussions**: [GitHub Discussions](https://github.com/sanjayrohith/MINDMATE/discussions)
- **Email**: [Contact the maintainer](mailto:sanjayrohith@example.com)

---

<div align="center">

**Made with ❤️ by [Sanjay Rohith](https://github.com/sanjayrohith)**

*MINDMATE - Where AI meets empathy*

</div>
