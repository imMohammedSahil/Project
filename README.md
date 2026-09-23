# 🔬 Research Scope AI
### AI-Based Research Scope Generator & Evidence-Backed Research Landscape Explorer

Turn raw, unpolished research ideas into real, evidence-backed research landscapes and publication-grade proposals — powered by **Semantic Scholar**, **OpenAlex**, **NetworkX / Vis-Network**, **Plotly**, and **Groq LLM**.

---

## 🌟 Key Innovations & Features

1. **Zero Hallucination Guarantee (Real Academic Papers)**:
   - Queries **Semantic Scholar Graph API** and **OpenAlex API** in real-time.
   - Every paper node displays verified **Authors, Publication Year, Citation Counts, Abstracts, and Direct DOI Links**.
2. **AI Interpretation & Specificity Layer**:
   - Decomposes free-form student ideas into Domain, Modalities, Sub-problems, and targeted Academic Search Queries using Groq (`openai/gpt-oss-120b` / `qwen/qwen3.8-27b`).
   - Detects vague inputs and prompts clarifying questions.
3. **Semantic Similarity Knowledge Graph**:
   - Calculates **true cosine similarity edge weights** between the user's idea and published literature clusters.
   - Physics-based interactive visual graph powered by `vis-network`.
4. **Evidence-Based Literature Gaps**:
   - Clear distinction with color-coded badges:
     - 🟢 `[From Paper]`: Direct limitations extracted from published abstracts.
     - 🟣 `[AI-Inferred]`: Gaps extrapolated by literature analysis.
5. **Research Saturation & 2D Landscape Matrix**:
   - Evidence-based multi-signal saturation formula (Volume, Citation Density, Recent Publication Velocity 2019–2026).
   - 2D Plotly Matrix: **Scope Potential vs Research Saturation** to locate *Sweet Spot / High Opportunity* research directions.
6. **Autonomous Scope Generator & 1-Click Export**:
   - Generates Formal Problem Statements, Research Questions (RQ1-3), Step-by-Step Objectives (RO1-4), Proposed Architecture, Datasets, and Evaluation Metrics.
   - 1-Click Export to `.md` (Markdown) and `.json`.

---

## 🚀 Quick Start (Local Machine)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Groq API Key
Set your API key in the environment or in the UI Settings tab:
```bash
set GROQ_API_KEY=gsk_...
```

### 3. Launch the Application
For development, use Gradio's hot-reload mode. Keep this command running and
changes to the Python files will reload the app automatically:
```bash
gradio app.py
```

For a normal launch without hot reload:
```bash
python app.py
```
Open your browser at `http://127.0.0.1:7860`.

---

## 🎓 Running in Google Colab (For Faculty Presentation)

We provide a self-contained, 1-click notebook `Research_Scope_AI_Colab.ipynb`:

1. Upload `Research_Scope_AI_Colab.ipynb` to [Google Colab](https://colab.research.google.com/).
2. Run the first cell to install dependencies:
   ```python
   !pip install -q gradio groq plotly networkx pandas requests sentence-transformers
   ```
3. Run the application cell:
   ```python
   demo.launch(share=True, debug=True)
   ```
4. Click the generated **Public Gradio URL** (`https://...gradio.live`) to present the live interface to your faculty directly from Google Colab!

---

## 🏛️ System Architecture

```
                  USER'S RESEARCH IDEA
                          │
                          ▼
            ┌───────────────────────────┐
            │   AI Interpretation Layer │
            │   (Groq LLM / Llama 3)    │
            │   • Domain & Modalities   │
            │   • Academic Search Query │
            │   • Specificity Analysis  │
            └─────────────┬─────────────┘
                          │
                          ▼
            ┌───────────────────────────┐
            │ Academic Retrieval Engine │
            │ (Semantic Scholar/OpenAlex│
            │ + SQLite/JSON Caching)    │
            │ • Real Papers, Citations  │
            │ • Real DOIs, URLs, Years  │
            └─────────────┬─────────────┘
                          │
                          ▼
            ┌───────────────────────────┐
            │   Embeddings & Graph      │
            │   (Cosine Sim + NetworkX) │
            │ • Real Similarity Weights │
            │ • Topic Clustering        │
            └─────────────┬─────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ Interactive   │ │ Research Deep │ │ Saturation    │
│ Vis-Network   │ │ Dive & Scope  │ │ Matrix &      │
│ Graph Map     │ │ Generator     │ │ Timeline      │
└───────────────┘ └───────────────┘ └───────────────┘
```

---

## 📂 Project Structure

```
c:\Holidays\Day 3\
├── config.py                 # Global settings, API endpoints, caching & model config
├── cache_manager.py          # SQLite response cache for queries & paper metadata
├── academic_retrieval.py     # Semantic Scholar & OpenAlex API search engine
├── llm_engine.py             # Groq LLM client & heuristic fallback synthesizer
├── embeddings_graph.py       # Cosine similarity, NetworkX graph & Vis-Network HTML
├── saturation_engine.py      # Multi-signal saturation formulas & Plotly charts
├── scope_generator.py        # Publication-grade research scope synthesizer
├── export_utils.py           # Markdown & JSON exporter
├── ui_components.py          # Glassmorphism dark CSS & HTML card templates
├── app.py                    # Complete Gradio Blocks interactive web app
├── Research_Scope_AI_Colab.ipynb # 1-Click Google Colab Notebook
├── requirements.txt          # Package dependencies
└── README.md                 # Documentation & Presentation Guide
```
