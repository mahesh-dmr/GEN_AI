import os

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

import O3_embed as embed


load_dotenv()


def format_context(docs):
    parts = []
    for doc in docs:
        source = doc.metadata.get("source", "unknown")
        page_num = doc.metadata.get("page", 0) + 1
        parts.append(f"Source: {source} | Page: {page_num}\n{doc.page_content[:900]}")
    return "\n\n".join(parts)


def answer_with_openai(question, docs, model_name):
    api_key = os.getenv("OPENAI_API_KEY", "") or os.getenv("openai_api_key", "")
    if not api_key:
        raise ValueError("OPENAI_API_KEY (or openai_api_key) is not set. Add it in your .env file.")

    llm = ChatOpenAI(api_key=api_key, model=model_name, temperature=0.1)
    context_text = format_context(docs)

    prompt = f"""Use only the context to answer the question.
If answer is not in context, say: I could not find this in the document.

Context:
{context_text}

Question:
{question}
"""
    return llm.invoke(prompt).content.strip()


def run_app():
    st.set_page_config(page_title="Simple RAG with OpenAI", layout="wide")
    st.title("Simple RAG with OpenAI")

    question = st.text_input("Ask your question")
    top_k = st.slider("Top documents", min_value=1, max_value=8, value=4)
    model_name = st.selectbox(
        "OpenAI model",
        options=["gpt-4.1-mini", "gpt-4o-mini", "gpt-4.1"],
        index=0
    )

    if st.button("Get Answer"):
        if not question.strip():
            st.warning("Please enter a question.")
            return

        with st.spinner("Loading vector store and retrieving data..."):
            vector_store = embed.load_vector_store(persist_dir="..\\database\\faiss_index")
            docs = vector_store.similarity_search(question, k=top_k)

        if not docs:
            st.warning("No matching documents found.")
            return

        with st.spinner("Generating answer..."):
            try:
                answer = answer_with_openai(question=question, docs=docs, model_name=model_name)
            except Exception as exc:
                st.error(f"OpenAI error: {exc}")
                return

        st.subheader("Answer")
        st.write(answer)


if __name__ == "__main__":
    run_app()
