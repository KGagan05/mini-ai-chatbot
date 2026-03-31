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

⚙️ Technologies Used
	•	Python
	•	FastAPI
	•	Scikit-learn
	•	Jinja2
	•	HTML

⸻

🔍 How It Works

1️⃣ Knowledge Base

A text file (data.txt) contains predefined information.

2️⃣ Text Vectorization

Uses TF-IDF Vectorizer to convert text into numerical vectors.

3️⃣ Similarity Matching

Uses Cosine Similarity to find the most relevant response.

4️⃣ Response Generation

Returns the closest matching sentence from the dataset.

⸻

▶️ How to Run

Install dependencies

pip install fastapi uvicorn scikit-learn jinja2

Run the chatbot

uvicorn app:app --reload

Example 
You: What is NLP?
Bot: NLP stands for Natural Language Processing.





