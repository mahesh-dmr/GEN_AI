# Project Guidelines

## Purpose
This is a learning project for Generative AI / RAG concepts. Code should be written clearly for a beginner — readability matters more than elegance.

## Code Style
- Write beginner-friendly Python: short functions, simple variable names, no clever one-liners
- No type hints required unless they genuinely aid clarity
- Comments only when the code cannot speak for itself — one short line only
- No docstrings on simple functions

## Libraries
- Always use LangChain libraries (`langchain`, `langchain-community`) as the primary abstraction for LLM, RAG, and document loading tasks
- Prefer LangChain document loaders (e.g., `PyPDFLoader`) over raw PDF libraries

## What to Build
- Always generate complete, runnable code — no stubs, no "TODO: implement this"
- Keep scripts self-contained in a single file unless the user asks to split them
- No extra CLI flags, config files, or abstractions unless asked
- No disk writes / file persistence unless the user asks for it

## Do Not
- Do not add features the user did not ask for
- Do not create markdown documentation files unless explicitly asked
- Do not refactor working code unless asked
