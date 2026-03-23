import streamlit as st
import sys

st.set_page_config(page_title="SupportSense RAG Chatbot", layout="wide")

try:
    from src.retrieve import retrieve_context
    from src.generate import generate_answer
except Exception as e:
    st.error(f"❌ Error loading dependencies: {str(e)}")
    st.stop()

st.title("SupportSense RAG Chatbot")
st.write("Ask questions about the public support conversation dataset.")

query = st.text_input("Enter your question:")

top_k = st.slider("Number of retrieved records", min_value=3, max_value=10, value=5)

if st.button("Get Answer"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Retrieving relevant records..."):
            retrieved_docs = retrieve_context(query, top_k=top_k)

        with st.spinner("Generating answer..."):
            answer = generate_answer(query, retrieved_docs)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Retrieved Context")
        for i, item in enumerate(retrieved_docs, start=1):
            st.markdown(f"### Record {i}")
            st.write("**Metadata:**", item["metadata"])
            st.write(item["text"])
            st.markdown("---")