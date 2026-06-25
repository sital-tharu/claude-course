# Claude Course — Building LLM Applications

A hands-on course project covering the fundamentals of building LLM-powered applications: chatbots, tool use, agentic loops, and a full RAG pipeline.

## Project Structure

| File | Topic |
|---|---|
| `request.ipynb` | First API call, multi-turn conversation basics |
| `chatbot.py` | Simple CLI chatbot with conversation history |
| `1_chatbot.py` | Enhanced chatbot with system prompt, streaming, and temperature control |
| `tools.ipynb` | Function/tool calling and an agentic loop |
| `websearch_tool.ipynb` | Web search tool with domain restrictions |
| `chunking.ipynb` | Text chunking strategies (character, sentence, section) |
| `embeddings.ipynb` | Generating embeddings with VoyageAI |
| `vectordb.ipynb` | Custom in-memory vector store with cosine/euclidean search |
| `report.md` | Sample document used as RAG source data |

## Setup

**1. Create and activate a virtual environment**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

**2. Install dependencies**

```bash
pip install openai python-dotenv voyageai
```

**3. Configure environment variables**

Create a `.env` file in the project root:

```
OPENROUTER_API_KEY=your_openrouter_key_here
VOYAGE_API_KEY=your_voyageai_key_here
```

- Get an OpenRouter API key at [openrouter.ai](https://openrouter.ai)
- Get a VoyageAI key at [voyageai.com](https://www.voyageai.com) (needed for embedding notebooks)

## Running the Chatbots

```bash
# Basic chatbot
python chatbot.py

# Enhanced chatbot (streaming + system prompt)
python 1_chatbot.py
```

## Notebooks Overview

### `request.ipynb` — API Basics
First API calls using the OpenAI SDK pointed at OpenRouter. Covers single-turn and multi-turn conversation with manual message history management.

### `tools.ipynb` — Tool Use & Agentic Loop
Defines two custom tools (`add_duration_to_datetime`, `set_reminder`) with JSON schemas and runs them inside an agentic loop that keeps calling the model until no more tool calls are requested.

### `websearch_tool.ipynb` — Web Search
Uses OpenRouter's `web_search_preview` tool type, restricted to trusted medical/health domains (NIH, CDC, Mayo Clinic, etc.), with citation output.

### `chunking.ipynb` — Text Chunking
Three chunking strategies for preparing documents for RAG:
- **Character-based** — fixed size with overlap
- **Sentence-based** — groups sentences with overlap
- **Section-based** — splits on markdown `##` headings

### `embeddings.ipynb` — Embeddings
Generates vector embeddings from document chunks using the `voyage-3-large` model.

### `vectordb.ipynb` — Vector Store
A pure-Python `VectorIndex` class built from scratch. Supports:
- Adding documents (auto-embeds via a provided function)
- Cosine and Euclidean distance metrics
- Top-k similarity search

Together, `chunking` → `embeddings` → `vectordb` form a complete RAG pipeline.

## Models Used

| Provider | Model | Used in |
|---|---|---|
| OpenRouter | `google/gemini-2.5-flash-lite` | `1_chatbot.py`, `tools.ipynb`, `websearch_tool.ipynb` |
| OpenRouter | `nex-agi/nex-n2-pro:free` | `chatbot.py`, `request.ipynb` |
| VoyageAI | `voyage-3-large` | `embeddings.ipynb`, `vectordb.ipynb` |