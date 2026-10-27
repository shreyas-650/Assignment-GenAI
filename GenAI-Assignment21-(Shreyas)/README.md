# Assignment 21: LangChain Document Loading and Text Splitter

A hands-on implementation of document ingestion and text preprocessing with **LangChain**. The project loads content from local files and public web pages, converts it into LangChain `Document` objects, and splits it into manageable chunks for downstream LLM and Retrieval-Augmented Generation (RAG) workflows.

## Overview

This assignment covers three areas:

- **Document loading:** Read TXT, Markdown, CSV, and PDF files, along with content from public web pages.
- **Text splitting:** Apply length-based, recursive structure-aware, document-structure-aware, and semantic chunking approaches.
- **Pipeline integration:** Use a unified preprocessing function to load and split content from a local directory or a web URL.

## Tasks Covered

### Part 1 — Document Loaders

| Task | Loader | Purpose |
|---|---|---|
| 1. Text Loader | `TextLoader` | Load a `.txt` file and inspect document count, content preview, and metadata. |
| 2. CSV Loader | `CSVLoader` | Convert CSV rows into individual `Document` objects and print sample content. |
| 3. PDF Loader | `PyPDFLoader` | Load a PDF and inspect its page count and sample page content. |
| 4. Directory Loader | `DirectoryLoader` | Load supported file types from a directory using suitable loader classes. |
| 5. Web Loader | `WebBaseLoader` | Extract textual content from a public webpage and preview the first 500 characters. |

### Part 2 — Text Splitters

| Task | Splitter / Approach | Purpose |
|---|---|---|
| 6. Why splitting is required | Conceptual explanation | Describe context-window limits and why chunking helps with retrieval and processing. |
| 7. Length-based splitting | `CharacterTextSplitter` | Configure chunk size and overlap, then inspect the resulting chunks. |
| 8. Structure-aware splitting | `RecursiveCharacterTextSplitter` | Split using separators that prioritize paragraphs and other text boundaries. |
| 9. Document-structure splitting | Markdown / document-aware separators | Split structured content while considering headings, sections, or page boundaries where available. |
| 10. Semantic splitting | `SemanticChunker` (optional demo) | Explain how embeddings help identify changes in meaning when selecting chunk boundaries. |

### Part 3 — Mini Integration

- **Task 11:** Implement `load_and_split_documents(path_or_url)` to load and split content from a local directory or a web URL, returning a list of chunks.
- **Task 12:** Summarize loader selection, suitable splitters for different data sources, and the role of chunk overlap.

## Technologies Used

- Python
- LangChain Community document loaders
- LangChain text splitters
- PyPDF for PDF extraction
- Beautiful Soup support for webpage parsing

## Installation

Install the core packages in the same Python environment used by the notebook or script:

```bash
pip install -r requirements.txt
```

Use your actual notebook and file names if they differ. The directory loader should be pointed at the correct path relative to the notebook's working directory.

## Unified Preprocessing Pipeline

The integration function follows this workflow:

```text
Local directory or public URL
              │
              ▼
       Select document loader
              │
              ▼
       LangChain Documents
              │
              ▼
          Text splitter
              │
              ▼
       List of text chunks
```

Example usage, assuming the function has been defined in the notebook:

```python
# Load and split files from a local directory
chunks = load_and_split_documents("../data")

# Load and split a public webpage
web_chunks = load_and_split_documents("https://example.com/")

print("Local chunks:", len(chunks))
print("Web chunks:", len(web_chunks))

if chunks:
    print(chunks[0].page_content)
    print(chunks[0].metadata)
```

The local-directory branch supports the configured file types (TXT, Markdown, PDF, and CSV). The web branch uses `WebBaseLoader` for accessible HTML pages; pages rendered primarily through JavaScript may require a different extraction method.

## Key Observations

- **TXT / Markdown:** `TextLoader` loads plain-text content and Markdown files.
- **CSV:** `CSVLoader` represents each row as a document by default.
- **PDF:** `PyPDFLoader` extracts text page by page; scanned image-only PDFs may require OCR.
- **Web pages:** `WebBaseLoader` fetches and parses accessible webpage content.
- **Small or simple text:** `CharacterTextSplitter` is straightforward when a chosen separator is appropriate.
- **Long or mixed-format text:** `RecursiveCharacterTextSplitter` provides a useful general-purpose starting point because it tries preferred separators before splitting more aggressively.
- **Structured content:** Markdown-aware or language-specific separators can help retain headings and section boundaries, but the result depends on the source text and splitter configuration.
- **Semantic chunking:** Embeddings represent text numerically, allowing a semantic splitter to estimate where the meaning changes. This requires an embedding model and additional computation.
- **Chunk overlap:** A small overlap can retain context near chunk boundaries, though excessive overlap increases storage and processing costs.

## Output

The loaders return LangChain `Document` objects. Each document typically contains:

- `page_content` — the extracted text
- `metadata` — source details such as the file path, page number, or row information when supplied by the loader

After splitting, the pipeline returns a list of smaller `Document` chunks that can be passed to later RAG stages, such as embedding generation, vector storage, and retrieval.

## Notes

- Update the source paths and URLs to match your environment.
- A `chunk_size` of `100` is useful for demonstrating splitting, but production RAG pipelines usually need tuning based on the embedding model, content type, and retrieval requirements.
- The HTML-specific splitter configures HTML-oriented separators. `WebBaseLoader` generally returns extracted page text, so the original HTML structure may not remain available for splitting.
- Keep API keys out of source control. Use environment variables or a secret manager for any service credentials.

