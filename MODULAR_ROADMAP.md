# Research Scope AI — Modular Development Roadmap

This document outlines the step-by-step modular development plan. We will build, test, and verify each block individually before moving to the next.

---

## 🧩 Overview of Modules

| Block | Module Name | Focus Area | Key Deliverables |
|:---:|:---|:---|:---|
| **Block 1** | **Academic Retrieval & Cache Engine** | Real Papers & Data Layer | `config.py`, `cache_manager.py`, `academic_retrieval.py` |
| **Block 2** | **AI Interpretation & Query Engine** | Idea Breakdown & LLM Logic | `llm_engine.py` (Groq LLM + Fallback synthesizer) |
| **Block 3** | **Embeddings & Research Graph** | Semantic Similarity & Graph | `embeddings_graph.py`, `vis-network` interactive HTML |
| **Block 4** | **Saturation Engine & Visual Matrix** | Evidence Analysis & Trends | `saturation_engine.py`, Plotly 2D Landscape Matrix & Timeline |
| **Block 5** | **Research Scope Generator & Exporter** | Actionable Proposal & Export | `scope_generator.py`, `export_utils.py` (Markdown export) |
| **Block 6** | **Gradio Interactive UI Dashboard** | Full Visual Frontend | `app.py`, `ui_components.py` (Custom CSS & Blocks UI) |
| **Block 7** | **Google Colab Package & Testing** | Faculty Presentation Setup | `Research_Scope_AI_Colab.ipynb`, `requirements.txt`, `README.md` |

---

## 📦 Detailed Breakdown of Blocks

### 🔹 Block 1: Academic Retrieval & Cache Engine
- **Purpose**: Connect to real academic sources so all papers, DOIs, authors, citations, and abstracts are authentic.
- **Key Files**:
  - `config.py`: Environment setup, API endpoints, rate limits, default presets.
  - `cache_manager.py`: SQLite / JSON cache to store query results locally (prevents rate limits and makes repeat queries instant).
  - `academic_retrieval.py`:
    - Semantic Scholar API search & recommendations client.
    - OpenAlex API fallback for niche or sparse topics.
    - Title / DOI deduplication and metadata extraction.
- **Verification**: Run standalone retrieval test on sample research topics to verify real paper data.

---

### 🔹 Block 2: AI Interpretation & Query Builder
- **Purpose**: Understand user input (from single keywords to multi-paragraph proposals) and extract structured research metadata.
- **Key Files**:
  - `llm_engine.py`:
    - Groq LLM client (supporting Llama 3 / Mixtral models).
    - Intelligent fallback synthesizer (rules/heuristics) for offline or keyless testing.
    - Extraction functions: Domain, Primary Problem, Input Modalities, AI Sub-fields, and Targeted Academic Search Queries.
    - Literature gap classification: distinguishes `[From Paper]` vs `[AI-Inferred]`.
- **Verification**: Feed raw text into the interpreter and inspect structured JSON output and generated search queries.

---

### 🔹 Block 3: Embeddings & Research Graph Engine
- **Purpose**: Compute mathematical semantic similarity between user idea and papers, cluster related directions, and render an interactive physics-based network graph.
- **Key Files**:
  - `embeddings_graph.py`:
    - SentenceTransformers / Cosine similarity vector calculator.
    - NetworkX graph construction (Center Node = User Idea, Cluster Nodes = Research Directions, Leaf Nodes = Real Papers).
    - Edge weights based on true mathematical cosine similarity (0.0 to 1.0).
    - Vis-Network HTML interactive visualizer (zoom, drag, click, node physics).
- **Verification**: Generate sample graph HTML and verify in browser that nodes render with real weights and click interactivity.

---

### 🔹 Block 4: Saturation Engine & 2D Landscape Matrix
- **Purpose**: Calculate evidence-based research saturation and plot the Scope × Saturation Matrix.
- **Key Files**:
  - `saturation_engine.py`:
    - Saturation formula based on paper count, publication growth (2019–2026), citation concentration, and methodology diversity.
    - 2D Plotly Matrix: Scope Potential (X-axis) vs Saturation Level (Y-axis).
    - 4 Quadrants: *Sweet Spot (High Potential / Moderate Saturation)*, *Saturated Baseline*, *Emerging Niche*, *Sparse/High Risk*.
    - Timeline velocity chart showing year-by-year research volume.
- **Verification**: Generate Plotly charts with real paper metadata and check quadrant placements.

---

### 🔹 Block 5: Research Scope Generator & Report Exporter
- **Purpose**: Synthesize research gaps, paper literature, and user idea into a complete, academic-grade research proposal scope.
- **Key Files**:
  - `scope_generator.py`:
    - Generates: Problem Statement, Research Questions, Step-by-step Objectives, Proposed Methodology & Architecture, Recommended Datasets, Evaluation Metrics (F1, Precision, Recall, AUC), and Expected Novel Contribution.
  - `export_utils.py`:
    - 1-click export of complete Research Scope + bibliography to formatted Markdown (`.md`) and `.json`.
- **Verification**: Test scope generation on a cluster and verify the generated markdown file.

---

### 🔹 Block 6: Gradio Interactive UI Dashboard
- **Purpose**: Assemble all backend modules into a polished, dark-mode glassmorphic Gradio Blocks application.
- **Key Files**:
  - `ui_components.py`: Custom CSS styling, card templates, badges (`[From Paper]` vs `[AI-Inferred]`), HTML containers.
  - `app.py`:
    - **Tab 1**: Research Idea & Graph Exploration (Input box, Vis-Network interactive graph, concept breakdown).
    - **Tab 2**: Research Intelligence & Node Deep-Dive (Node card, connection analysis, paper links with DOIs).
    - **Tab 3**: Scope Generator & Proposal Builder (Interactive scope customizer & 1-click Markdown download).
    - **Tab 4**: Saturation Matrix & Timeline Explorer (Plotly 2D matrix + publication timeline).
    - **Tab 5**: Settings & Presets (API key configuration, sample research idea presets).
- **Verification**: Launch local Gradio server (`python app.py`) and interactively test all user journeys.

---

### 🔹 Block 7: Google Colab Packaging & Presentation Setup
- **Purpose**: Package everything into a 1-click Google Colab notebook ready for faculty presentation.
- **Key Files**:
  - `Research_Scope_AI_Colab.ipynb`: Ready-to-run notebook with dependencies, Groq key prompt, modular code execution, and `demo.launch(share=True)`.
  - `requirements.txt`: Python package list (`gradio`, `groq`, `sentence-transformers`, `plotly`, `networkx`, `pandas`, `requests`).
  - `README.md`: Clear documentation with setup steps for both local and Google Colab environments.
- **Verification**: Run notebook cells and verify that Gradio launches with a working public share link.

---

## 🚀 Execution Strategy

We will proceed **one block at a time**:
1. Build the block's code files.
2. Run automated tests to verify functionality.
3. Review and get your feedback before advancing to the next block.
