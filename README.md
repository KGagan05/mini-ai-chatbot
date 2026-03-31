📌 Overview

This project implements an AI-powered chatbot using Natural Language Processing (NLP) techniques.

The chatbot answers user queries by retrieving the most relevant information from a predefined knowledge base, making it a simple example of a Retrieval-Augmented Generation (RAG) system.

⸻

🎯 Objective

To build a chatbot that can understand user questions and return the most relevant answer based on stored knowledge.
User Query → Text Vectorization → Similarity Search → Best Matching Response

🧠 Key Concept

🔹 Retrieval-Augmented Generation (RAG)

Instead of generating answers from scratch, the chatbot:
	•	Converts user queries into vectors
	•	Compares them with stored knowledge vectors
	•	Retrieves the most similar response

⸻

🏗 Project Structure

ai-chatbot
│
├── data.txt              # Knowledge base
├── chatbot.py           # NLP logic
├── app.py               # FastAPI backend
├── templates/
│   └── index.html       # UI
└── README.md


