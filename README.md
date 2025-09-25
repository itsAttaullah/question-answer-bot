# 🧠 AI Chatbot with Memory

A conversational **AI chatbot** powered by **FastAPI**, **Streamlit**, **Groq API**, and **SQLAlchemy**. The bot supports **real-time streaming** responses and maintains **persistent conversation history** by storing past messages in a database.

---

## 🚀 Features

* **🔥 Streaming Responses:** Get rapid, real-time responses from the powerful Groq API.
* **💾 Persistent History:** Chat history is stored using **SQLAlchemy** (defaulting to SQLite but easily configurable for PostgreSQL, MySQL, etc.).
* **📚 Context-Aware:** The bot remembers the last $N$ messages to maintain a fluid, context-rich conversation.
* **🎨 Simple Frontend:** A user-friendly chat interface built with **Streamlit**.
* **⚡ Robust Backend:** A high-performance RESTful API powered by **FastAPI**.
* **🐍 Pure Python:** Built entirely in Python.

---

## 🏗️ Project Structure

```bash
📂 simple-bot
┣ 📜 main.py       # FastAPI backend: API routes and core logic
┣ 📜 crud.py       # Database operations (Create, Read, Update, Delete)
┣ 📜 db_config.py  # SQLAlchemy engine and session setup
┣ 📜 schemas.py    # Pydantic models for data validation
┣ 📜 utils.py      # Groq API helper functions
┣ 📜 frontend.py   # Streamlit UI for the chatbot
┣ 📜 requirements.txt # Project dependencies
┗ 📂 pycache     # Auto-generated
That's an excellent clarification! You want the content in a single block, but use the standard GitHub Markdown features like headings (#), lists (* or -), code blocks (```), and bold/italics, instead of putting the entire thing in a single, large code block.

Here is the correct, combined, and styled GitHub README content:

Markdown

# 🧠 AI Chatbot with Memory

A conversational **AI chatbot** powered by **FastAPI**, **Streamlit**, **Groq API**, and **SQLAlchemy**. The bot supports **real-time streaming** responses and maintains **persistent conversation history** by storing past messages in a database.

---

## 🚀 Features

* **🔥 Streaming Responses:** Get rapid, real-time responses from the powerful Groq API.
* **💾 Persistent History:** Chat history is stored using **SQLAlchemy** (defaulting to SQLite but easily configurable for PostgreSQL, MySQL, etc.).
* **📚 Context-Aware:** The bot remembers the last $N$ messages to maintain a fluid, context-rich conversation.
* **🎨 Simple Frontend:** A user-friendly chat interface built with **Streamlit**.
* **⚡ Robust Backend:** A high-performance RESTful API powered by **FastAPI**.
* **🐍 Pure Python:** Built entirely in Python.

---

## 🏗️ Project Structure

```bash
📂 simple-bot
┣ 📜 main.py       # FastAPI backend: API routes and core logic
┣ 📜 crud.py       # Database operations (Create, Read, Update, Delete)
┣ 📜 db_config.py  # SQLAlchemy engine and session setup
┣ 📜 schemas.py    # Pydantic models for data validation
┣ 📜 utils.py      # Groq API helper functions
┣ 📜 frontend.py   # Streamlit UI for the chatbot
┣ 📜 requirements.txt # Project dependencies
┗ 📂 pycache     # Auto-generated
⚙️ Installation
1. Clone the Repository
git clone https://github.com/itsAttaullah/question-answer-bot.git
cd simple-bot
2. Set Up Virtual Environment
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
🔑 Environment Variables
Create a file named .env in the project root and add your keys:
# SQLAlchemy Database URL. Example shown is for SQLite.
# Change this to use PostgreSQL, MySQL, etc.
DATABASE_URL=sqlite:///./chat_history.db

# Your Groq API Key
GROQ_API_KEY=your_api_key_here
▶️ Running the Project
1. Start the Backend (FastAPI + Uvicorn)
uvicorn main:app --reload]
Backend runs at: http://127.0.0.1:8000
2. Start the Frontend (Streamlit)
streamlit run frontend.py
Frontend runs at: http://localhost:8501
That's an excellent clarification! You want the content in a single block, but use the standard GitHub Markdown features like headings (#), lists (* or -), code blocks (```), and bold/italics, instead of putting the entire thing in a single, large code block.

Here is the correct, combined, and styled GitHub README content:

Markdown

# 🧠 AI Chatbot with Memory

A conversational **AI chatbot** powered by **FastAPI**, **Streamlit**, **Groq API**, and **SQLAlchemy**. The bot supports **real-time streaming** responses and maintains **persistent conversation history** by storing past messages in a database.

---

## 🚀 Features

* **🔥 Streaming Responses:** Get rapid, real-time responses from the powerful Groq API.
* **💾 Persistent History:** Chat history is stored using **SQLAlchemy** (defaulting to SQLite but easily configurable for PostgreSQL, MySQL, etc.).
* **📚 Context-Aware:** The bot remembers the last $N$ messages to maintain a fluid, context-rich conversation.
* **🎨 Simple Frontend:** A user-friendly chat interface built with **Streamlit**.
* **⚡ Robust Backend:** A high-performance RESTful API powered by **FastAPI**.
* **🐍 Pure Python:** Built entirely in Python.

---

## 🏗️ Project Structure

```bash
📂 simple-bot
┣ 📜 main.py       # FastAPI backend: API routes and core logic
┣ 📜 crud.py       # Database operations (Create, Read, Update, Delete)
┣ 📜 db_config.py  # SQLAlchemy engine and session setup
┣ 📜 schemas.py    # Pydantic models for data validation
┣ 📜 utils.py      # Groq API helper functions
┣ 📜 frontend.py   # Streamlit UI for the chatbot
┣ 📜 requirements.txt # Project dependencies
┗ 📂 pycache     # Auto-generated
⚙️ Installation
1. Clone the Repository
Bash

git clone https://github.com/itsAttaullah/question-answer-bot.git
cd simple-bot
2. Set Up Virtual Environment
Bash

python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
3. Install Dependencies
Bash

pip install -r requirements.txt
🔑 Environment Variables
Create a file named .env in the project root and add your keys:

Code snippet

# SQLAlchemy Database URL. Example shown is for SQLite.
# Change this to use PostgreSQL, MySQL, etc.
DATABASE_URL=sqlite:///./chat_history.db

# Your Groq API Key
GROQ_API_KEY=your_api_key_here
▶️ Running the Project
1. Start the Backend (FastAPI + Uvicorn)
Bash
uvicorn main:app --reload
Backend runs at: http://127.0.0.1:8000

2. Start the Frontend (Streamlit)
Bash
streamlit run frontend.py
Frontend runs at: http://localhost:8501

📡 API Endpoints
Method	Endpoint	Description
POST	/chat	Send a message and get a streaming AI response.
GET	/history	Retrieve the last N messages from the DB.
/history?limit=10	(Example: retrieves the last 10 messages)

🤝 Contributing
Pull requests are welcome! If you’d like to contribute:
Fork the repo.
Create a new branch (git checkout -b feature/my-feature).
Commit your changes.
Open a Pull Request (PR).
