from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

def load_pfd_documents():
    folder_path = "D:\\git_repo\\GEN_AI\\03_RAG\\DATA"
    loader = DirectoryLoader(folder_path, glob="**/*.pdf", loader_cls=PyPDFLoader)
    docs = loader.load()
    return docs


def main():
    docs = load_pfd_documents()
    for doc in docs:
        page_num = doc.metadata.get("page", 0) + 1
        print(f"--- Page {page_num} ---")
        print("Metadata:", doc.metadata)
        print("Content:", doc.page_content[:10])  # show first 500 chars per page
        print()
    
if __name__ == "__main__":
    main()
