🧠 AI Chatbot with Memory

A conversational AI chatbot powered by FastAPI, Streamlit, Groq API, and SQLAlchemy.
The bot supports real-time streaming responses and remembers past conversations by storing them in a database.

🚀 Features

🔥 Streaming responses from Groq API

💾 Persistent chat history stored in postgresql database

📚 Context-aware conversations (last N messages are remembered)

🎨 Simple Streamlit frontend for chatting with the bot

⚡ FastAPI backend with REST endpoints

🐍 Written fully in Python
🏗️ Project Structure
📂 simple-bot
 ┣ 📜 main.py          # FastAPI backend (API + DB integration)
 ┣ 📜 crud.py          # Database operations
 ┣ 📜 db_config.py     # SQLAlchemy engine & session setup
 ┣ 📜 schemas.py       # Pydantic models
 ┣ 📜 utils.py         # Groq API helper functions
 ┣ 📜 frontend.py      # Streamlit UI for chatbot
 ┣ 📜 requirements.txt # Dependencies
 ┗ 📂 __pycache__      # Auto-generated
⚙️ Installation
1️⃣ Clone repo
git clone https://github.com/itsAttaullah/question-answer-bot.git
cd simple-bot
2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
requirements.txt
fastapi
uvicorn
psycopg2-binary
sqlalchemy
pydantic
httpx
python-dotenv
streamlit
pip install -r requirements.txt
🔑 Environment Variables
Create a .env file in the project root:
DATABASE_URL=postgres:///./chatbot...
GROQ_API_KEY=your_api_key_here
▶️ Running the Project
Start Backend (FastAPI + Uvicorn)
uvicorn main:app --reload
Backend runs at: http://127.0.0.1:8000
Start Frontend (Streamlit)
streamlit run frontend.py
Frontend runs at: http://localhost:8501
📡 API Endpoints
POST /chat → Send a message and get streaming AI response
GET /history?limit=10 → Retrieve last N messages from DB

🤝 Contributing
Pull requests are welcome! If you’d like to contribute:
Fork the repo
Create a new branch (feature/my-feature)
Commit your changes
Open a PR

