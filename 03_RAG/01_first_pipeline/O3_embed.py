import O2_chunk_pdf as chunk_pdf
from pathlib import Path
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def get_embedding_model(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    return HuggingFaceEmbeddings(model_name=model_name)


def build_vector_store(chunks=None, chunk_size=600, chunk_overlap=120):
    if chunks is None:
        chunks = chunk_pdf.load_chunks(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    embedding_model = get_embedding_model()
    vector_store = FAISS.from_documents(chunks, embedding_model)
    return vector_store, chunks


def save_vector_store(vector_store, persist_dir="..\\database\\faiss_index"):
    base_path = Path(__file__).resolve().parent
    save_path = (base_path / persist_dir).resolve()
    save_path.mkdir(parents=True, exist_ok=True)
    vector_store.save_local(str(save_path))
    return save_path


def load_vector_store(persist_dir="..\\database\\faiss_index"):
    base_path = Path(__file__).resolve().parent
    load_path = (base_path / persist_dir).resolve()
    embedding_model = get_embedding_model()
    vector_store = FAISS.load_local(
        str(load_path),
        embedding_model,
        allow_dangerous_deserialization=True
    )
    return vector_store


def main():
    vector_store, chunks = build_vector_store()
    save_path = save_vector_store(vector_store)

    print(f"Number of chunks embedded: {len(chunks)}")
    print(f"FAISS index saved at: {save_path}")

    sample_query = "What is this document about?"
    results = vector_store.similarity_search(sample_query, k=3)

    print(f"Top results for query: {sample_query}")
    for i, doc in enumerate(results, start=1):
        source = doc.metadata.get("source", "unknown")
        page_num = doc.metadata.get("page", 0) + 1
        print(f"Result {i} | {source} | Page {page_num}")
        print(doc.page_content[:200])
        print()


if __name__ == "__main__":
    main()
