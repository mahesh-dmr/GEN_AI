# RAG Pipeline Notes

## Overview
This folder has four Python files that implement a simple PDF-to-answer RAG flow.

## File 1: O1_load_pdf.py
- Loads all PDF files from 03_RAG/DATA using DirectoryLoader and PyPDFLoader.
- Each loaded item is a single page document with metadata such as source and page.
- main() prints a short page preview for quick inspection.

## File 2: O2_chunk_pdf.py
- Imports O1 and splits loaded pages into chunks using RecursiveCharacterTextSplitter.
- Default settings are chunk_size 600 and chunk_overlap 120.
- load_chunks() returns reusable chunks for embedding and retrieval.

## File 3: O3_embed.py
- Imports O2 and creates embeddings with all-MiniLM-L6-v2.
- Builds a FAISS vector store from the chunks.
- save_vector_store() writes index.faiss and index.pkl to 03_RAG/database/faiss_index.
- load_vector_store() reopens the saved FAISS index with the same embedding model.

## File 4: O4_Generation.py
- Streamlit app that loads .env and reads OPENAI_API_KEY.
- Retrieves top similar chunks from FAISS for the user question.
- Sends context plus question to ChatOpenAI and shows the final answer.
- Default UI model is gpt-4.1-mini.

## Steps to Run
1. From this folder, run: python O3_embed.py
2. Ensure .env in the project root contains: OPENAI_API_KEY=your_key_here
3. Run the app: python -m streamlit run O4_Generation.py
4. Ask questions in the browser UI.

## When to Rebuild
If PDF files change, rerun python O3_embed.py before starting Streamlit again.
