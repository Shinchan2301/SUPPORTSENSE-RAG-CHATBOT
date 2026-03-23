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

⚙️ Setup Instructions
1️⃣ Create a virtual environment
python -m venv .venv
2️⃣ Activate it
.venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
2️⃣ Activate it
.venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Add dataset
Place your CSV file inside:
data/raw/sample_conversations.csv
5️⃣ Preprocess data
py src/preprocess.py
6️⃣ Build vector database
py src/build_index.py
7️⃣ Run the app
streamlit run app.py
7️⃣ Run the app
streamlit run app.py
💡 Example Questions
What kind of risky conversation patterns are present?
What are common opening messages?
Summarize location-related questions.
What sentiment patterns appear in the dataset?
⚠️ Notes
This project uses a public sample dataset for learning purposes
No private or proprietary data is used
🌟 Future Improvements
Add metadata-based filtering
Improve prompt engineering
Add chat history (multi-turn conversation)
Deploy the app online
👨‍💻 Author
Pavan Bhurke
