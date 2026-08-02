import O1_load_pdf as load_pdf
from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_text_splitter(chunk_size=600, chunk_overlap=120):
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )


def load_chunks(chunk_size=600, chunk_overlap=120):
    docs = load_pdf.load_pfd_documents()
    text_splitter = get_text_splitter(chunk_size, chunk_overlap)
    chunks = text_splitter.split_documents(docs)
    return chunks


def main():
    chunks = load_chunks(chunk_size=600, chunk_overlap=120)

    print(f"Number of documents: {len(docs)}")
    print(f"Number of chunks: {len(chunks)}")

    if chunks:
        print(f"First chunk: {chunks[0].page_content[:200]}")
        print()

    for i, chunk in enumerate(chunks[:5], start=1):
        source = chunk.metadata.get("source", "unknown")
        page_num = chunk.metadata.get("page", 0) + 1
        print(f"Chunk {i} | {source} | Page {page_num}")
        print(chunk.page_content[:200])
        print()


if __name__ == "__main__":
    main()
