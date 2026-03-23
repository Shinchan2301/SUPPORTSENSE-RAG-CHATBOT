import sys
print("Script started!", flush=True)

import pandas as pd
print("Pandas imported", flush=True)
import chromadb
print("ChromaDB imported", flush=True)
from sentence_transformers import SentenceTransformer
print("SentenceTransformer imported", flush=True)

INPUT_FILE = "data/processed/cleaned_conversations.csv"
CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "support_conversations"

def main():
    try:
        print("Loading cleaned dataset...", flush=True)
        df = pd.read_csv(INPUT_FILE)
        print("Dataset loaded!", flush=True)

        print("Loading embedding model...", flush=True)
        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        print("Model loaded!", flush=True)

        print("Connecting to ChromaDB...", flush=True)
        client = chromadb.PersistentClient(path=CHROMA_PATH)

        # Delete old collection if it exists
        existing_collections = [c.name for c in client.list_collections()]
        if COLLECTION_NAME in existing_collections:
            client.delete_collection(COLLECTION_NAME)

        collection = client.create_collection(name=COLLECTION_NAME)

        documents = []
        metadatas = []
        ids = []

        print("Preparing documents...", flush=True)
        for i, row in df.iterrows():
            text = str(row.get("text", ""))
            notes = str(row.get("notes", ""))

            full_text = text
            if notes and notes != "nan":
                full_text += f"\nNotes: {notes}"

            metadata = {
                "category": str(row.get("category", "unknown")),
                "intent": str(row.get("intent", "unknown")),
                "sentiment": str(row.get("sentiment", "unknown")),
                "chat_phase": str(row.get("chat_phase", "unknown")),
                "escalation_level": str(row.get("escalation_level", "unknown"))
            }

            documents.append(full_text)
            metadatas.append(metadata)
            ids.append(f"doc_{i}")

        print("Creating embeddings...", flush=True)
        embeddings = model.encode(documents, show_progress_bar=True).tolist()

        print("Saving to ChromaDB...", flush=True)
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids,
            embeddings=embeddings
        )

        print("Index built successfully!", flush=True)
        print("Total documents indexed:", len(documents), flush=True)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr, flush=True)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()