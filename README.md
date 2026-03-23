# 🚀 SupportSense RAG Chatbot

A beginner-friendly **Retrieval-Augmented Generation (RAG)** chatbot built using open-source and free tools.

---

## ✨ Features

- Loads a public conversation dataset  
- Cleans and preprocesses text data  
- Creates embeddings using Sentence Transformers  
- Stores vectors in ChromaDB  
- Retrieves relevant records for a user query  
- Generates grounded answers using a local Ollama model  
- Provides a simple Streamlit UI  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- Sentence Transformers  
- ChromaDB  
- Ollama  
- Qwen2.5 3B  

---

## 📂 Project Structure

```text
supportsense-rag-chatbot/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   └── processed/
├── chroma_db/
└── src/
    ├── load_data.py
    ├── preprocess.py
    ├── build_index.py
    ├── retrieve.py
    └── generate.py for learning purposes and does not use any private or proprietary data.
