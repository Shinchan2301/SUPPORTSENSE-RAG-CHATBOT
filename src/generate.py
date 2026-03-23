import ollama

def build_prompt(query, retrieved_docs):
    context_blocks = []

    for i, item in enumerate(retrieved_docs, start=1):
        meta = item["metadata"]
        text = item["text"]

        block = f"""
Document {i}:
Category: {meta.get('category', 'unknown')}
Intent: {meta.get('intent', 'unknown')}
Sentiment: {meta.get('sentiment', 'unknown')}
Chat Phase: {meta.get('chat_phase', 'unknown')}
Escalation Level: {meta.get('escalation_level', 'unknown')}

Text:
{text}
"""
        context_blocks.append(block)

    context = "\n".join(context_blocks)

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

Rules:
1. Do not make up information
2. If answer is unclear, say: "Not enough information found"
3. First give a short summary
4. Then give 3 key insights in bullet points

User Question:
{query}

Context:
{context}
"""
    return prompt


def generate_answer(query, retrieved_docs, model_name="qwen2.5:3b"):
    prompt = build_prompt(query, retrieved_docs)

    response = ollama.chat(
        model=model_name,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]


# Test block
if __name__ == "__main__":
    import sys
    print("Starting generate.py...", flush=True)
    
    try:
        from retrieve import retrieve_context
        print("retrieve_context imported successfully", flush=True)

        query = "What kind of risky conversation patterns are present?"
        print(f"Query: {query}", flush=True)

        retrieved_docs = retrieve_context(query, top_k=3)
        print(f"Retrieved {len(retrieved_docs)} documents", flush=True)

        answer = generate_answer(query, retrieved_docs)
        print("\nGenerated Answer:\n")
        print(answer)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr, flush=True)
        import traceback
        traceback.print_exc()