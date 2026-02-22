# 🚀 Production-Ready AI Career Advisor Chatbot

A domain-specific, production-grade GenAI chatbot built using:
- Streamlit (UI)
- Groq LLM API (Llama 3.1 8B Instant)
- AWS EC2 Deployment

## 📌 Overview

This project implements a scalable AI Career Advisor chatbot designed using clean architecture principles and deployed on AWS EC2.

The chatbot provides:
- Career roadmaps
- Skill development guidance
- Interview preparation advice
- Job search strategies
- Professional growth planning

---

## 🏗 Architecture

User → Streamlit UI → LLM Client → Groq API → Response Rendering

Key design principles:
- Separation of concerns
- Environment variable security
- Session-based memory handling
- Modular LLM client wrapper
- Cloud deployment configuration

---

## 🧠 Features

- Multi-turn conversation memory
- Domain-restricted system prompt
- Configurable temperature & token control
- Secure API key management using `.env`
- Public cloud deployment
- Background server execution

---

## 🛠 Tech Stack

- Python 3.10+
- Streamlit
- Groq (Llama 3.1 8B Instant)
- AWS EC2 (Ubuntu)
- SSH & SCP for deployment

---

## 🚀 Deployment (AWS EC2)

1. Launch Ubuntu EC2 instance
2. Open ports:
   - 22 (SSH)
   - 8501 (Streamlit)
3. Upload project using SCP
4. Create virtual environment
5. Install requirements
6. Set environment variables
7. Run: streamlit run app.py 
access on http://13.49.225.248:8501

GROQ_API_KEY=your_api_key_here should be stored in .env file

📈 Future Improvements

Add Nginx reverse proxy

Enable HTTPS with Let's Encrypt

Add authentication

Dockerize application

Implement rate limiting

Add token usage monitoring

👨‍💻 Author

Swastik Dasgupta
AIML Student | GenAI Enthusiast
