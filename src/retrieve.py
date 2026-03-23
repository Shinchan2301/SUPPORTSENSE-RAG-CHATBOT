import sys
print("Script started!", flush=True)

try:
    import chromadb
    print("ChromaDB imported", flush=True)
    from sentence_transformers import SentenceTransformer
    print("SentenceTransformer imported", flush=True)

    CHROMA_PATH = "chroma_db"
    COLLECTION_NAME = "support_conversations"

    print("Loading embedding model for retrieval...", flush=True)
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    print("Model loaded!", flush=True)

    print("Connecting to ChromaDB...", flush=True)
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_collection(COLLECTION_NAME)
    print("ChromaDB connected!", flush=True)

    def retrieve_context(query, top_k=5):
        print(f"Retrieving for query: {query}", flush=True)

        query_embedding = model.encode([query]).tolist()[0]

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        docs = results["documents"][0]
        metas = results["metadatas"][0]

        combined = []
        for doc, meta in zip(docs, metas):
            combined.append({
                "text": doc,
                "metadata": meta
            })

        return combined


    if __name__ == "__main__":
        sample_query = "What kind of risky conversation patterns are present?"
        results = retrieve_context(sample_query, top_k=3)

        print("\nTop retrieved results:\n", flush=True)
        for i, item in enumerate(results, start=1):
            print(f"Result {i}", flush=True)
            print("Metadata:", item["metadata"], flush=True)
            print("Text:", item["text"], flush=True)
            print("-" * 50, flush=True)

except Exception as e:
    print(f"ERROR: {e}", file=sys.stderr, flush=True)
    import traceback
    traceback.print_exc()
