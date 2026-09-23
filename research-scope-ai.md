# Research Scope AI
### AI-Based Research Scope Generator & Research Landscape Explorer

> Turn a raw research idea into a real, evidence-backed research landscape — not a list of AI-generated guesses.

---

## 1. What We're Building

This is not a simple "research scope generator." It's a **Research Landscape Explorer + Scope Generator**.

The user's idea becomes the center of a research map, and the system discovers real, related research around it.

```
                USER'S IDEA
                    │
                    ▼
          ┌───────────────────┐
          │   AI UNDERSTANDS  │
          │   USER INPUT      │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ ACADEMIC SEARCH   │
          │ REAL PAPERS       │
          └─────────┬─────────┘
                    │
                    ▼
        ┌─────────────────────────┐
        │ RESEARCH LANDSCAPE      │
        │                         │
        │    ●────●────●          │
        │   /      \    \         │
        │  ●        ●────●        │
        │       \    \            │
        │        ●────●           │
        └─────────────┬───────────┘
                      │
                      ▼
             RESEARCH SCOPE
                      │
                      ▼
             SATURATION ANALYSIS
```

**Core principle:** graph nodes represent *real* research areas/papers retrieved from academic sources — never fabricated topics.

We use **Semantic Scholar** as the primary academic data source, since its API exposes paper search, abstracts, authors, citations, references, paper URLs, and a recommendations endpoint.

---

## 2. Page 1 — Research Input

The landing page.

```
┌──────────────────────────────────────────────┐
│                                                │
│          RESEARCH SCOPE AI                    │
│                                                │
│   Turn your idea into a research landscape.   │
│                                                │
│ ┌────────────────────────────────────────────┐│
│ │ Describe your research idea...              ││
│ │                                              ││
│ │ I want to develop an AI system that...       ││
│ │                                              ││
│ └────────────────────────────────────────────┘│
│                                                │
│  + Upload / Add context                        │
│                                                │
│             [ Explore Research ]               │
│                                                │
└──────────────────────────────────────────────┘
```

**Input should accept:**
- One sentence
- A paragraph
- A rough idea
- A problem statement
- Multiple paragraphs
- Pasted notes
- A research proposal
- Keywords

Later: support `.txt` / `.pdf` upload.

The AI first converts whatever the user gives into a **structured representation** before doing anything else.

---

## 3. AI Interpretation Layer

**Example input:**
> "I want to make an AI system that can detect fake websites and phishing attacks using URL information and maybe screenshots. I don't know exactly what approach to use."

**System extracts:**

| Field | Value |
|---|---|
| Domain | Cybersecurity |
| Primary problem | Phishing / malicious website detection |
| Possible inputs | URL, webpage content, screenshot, metadata |
| AI areas | NLP, Computer Vision, Multimodal AI, Classification |
| User's intent | Develop a detection system |

This is where the **Groq LLM** comes in — the same API key/model is reused across all AI operations (query building, summarization, gap analysis, scope generation) rather than spinning up separate services for each.

---

## 4. The Research Graph

The centerpiece feature.

```
                         Multimodal
                       Phishing Detection
                              ●
                             /
                            /
          URL Detection ●──● USER IDEA ──● Website
                        /       │            Content
                       /        │
              ●───────●         ●
        ML Phishing           Vision-based
        Detection             Detection
                                │
                                ●
                         Screenshot Analysis
```

Each node = a research direction / research cluster / relevant paper, depending on graph depth.

### Connection Strength

Edges carry a weight:

```
User idea
   │
   ├── URL-based detection       0.91
   ├── Multimodal detection      0.87
   ├── Screenshot detection      0.79
   ├── NLP phishing detection    0.74
   └── Adversarial detection     0.51
```

**Weights must come from measurable signals** — semantic similarity, citation relationships, shared concepts, and/or Semantic Scholar's recommendation relevance — **never invented by the LLM**. This distinction matters when demonstrating the project's rigor.

---

## 5. Research Card (Node Click)

Clicking **"Multimodal Phishing Detection"** opens:

```
┌─────────────────────────────────────────────┐
│ MULTIMODAL PHISHING DETECTION          ×    │
├─────────────────────────────────────────────┤
│ Research Area                                │
│ Cybersecurity • Multimodal AI                │
│                                               │
│ What has been done?                          │
│ Researchers have explored combining          │
│ multiple signals for phishing detection...   │
│                                               │
│ Problem addressed                            │
│ Traditional URL-only approaches can miss...  │
│                                               │
│ Common approaches                            │
│ • Transformer models                         │
│ • CNN-based visual analysis                  │
│ • Multimodal fusion                          │
│                                               │
│ Research gap                                 │
│ ...                                          │
│                                               │
│ YOUR IDEA vs THIS AREA                       │
│ Strong semantic overlap because...           │
│                                               │
│ Possible research scope                      │
│ ...                                          │
│                                               │
│ [ View Papers ]   [ Explore Scope ]          │
└─────────────────────────────────────────────┘
```

This is where the LLM adds value **after** retrieving factual paper data — not before.

---

## 6. Real Papers, Not Dummy Data

**Hard requirement.** For every paper displayed:

- Title
- Authors
- Year
- Abstract
- Citation count
- Research area
- DOI / URL
- Source
- `[ Open Paper ↗ ]`

Semantic Scholar provides title, abstract, authors, citations, references, and paper URLs, plus a **recommendations API** that suggests papers from seed papers.

### Pipeline

```
User Idea
   ↓
LLM → Search Queries
   ↓
Semantic Scholar
   ↓
Real Papers
   ↓
Paper Metadata
   ↓
Embeddings / Similarity
   ↓
Research Clusters
   ↓
Graph
```

---

## 7. "What Has Already Been Done?"

Per research cluster:

- **Existing work** — approaches researchers have investigated (A, B, C…)
- **Problems addressed**
- **Common methodologies** — CNN, Transformer, GNN, traditional ML, multimodal fusion
- **Limitations / gaps** — limited datasets, poor generalization, lack of explainability, high computational cost, limited real-time evaluation

**Important distinction to preserve in the UI:**
- *"The paper explicitly states this limitation"*
  vs.
- *"The AI inferred this possible gap from the retrieved literature."*

---

## 8. "How Is This Connected to MY Idea?"

Every node gets a **Connection Analysis**:

```
YOUR IDEA
    ↓
RELATED AREA
    ↓
WHY THEY ARE CONNECTED
```

- **Shared problem:** Phishing detection
- **Shared data:** URLs + webpage information
- **Shared technique:** Machine learning classification
- **Difference:** Your proposal introduces screenshot-level visual information

The user isn't just browsing papers — they're seeing *how* existing research relates to what they want to do.

---

## 9. Research Scope Generator

```
             Research Area
                   ↓
             Existing Work
                   ↓
              Research Gap
                   ↓
             Your Idea
                   ↓
             Possible Scope
```

**Example output structure:**

**Potential Scope:**
> "Multimodal phishing detection using URL semantics and webpage screenshots with explainable prediction."

- **Problem statement**
- **Research question**
- **Objectives** (1, 2, 3…)
- **Possible methodology**
- **Potential dataset**
- **Evaluation metrics** — Precision, Recall, F1, AUC
- **Expected contribution**

---

## 10. Page 2 — Research Saturation

Instead of just saying *"this area is saturated,"* build a **Research Saturation Matrix**.

```
                    RESEARCH SATURATION

                    Low ─────────────── High

URL Detection       ████████████████████  HIGH
Image Detection     ██████████████░░░░░░  MEDIUM
Multimodal          ████████░░░░░░░░░░░░  LOW-MEDIUM
Explainable AI      ██████████░░░░░░░░░░  MEDIUM
Real-time           ██████░░░░░░░░░░░░░░  LOW
```

Saturation must be **evidence-based**, calculated from signals such as:
- Number of relevant papers
- Publication growth over time
- Citation concentration
- Number of distinct approaches
- Recent-paper activity
- Research-gap frequency

Show *why* the system considers an area more or less saturated — don't just output a number.

---

## 11. Visual Matrix (Scope × Saturation)

```
                    RESEARCH LANDSCAPE

     HIGH ┤
          │       ● URL Detection
          │
SATURATION│                  ● Image Detection
          │
          │            ● Multimodal
          │
          │  ● Explainability
     LOW  └──────────────────────────────
             LOW                    HIGH
                  SCOPE POTENTIAL
```

Lets users visually identify:
- Highly researched areas
- Less explored areas
- Potential research directions

— without the system simply telling them "this is the best."

---

## 12. Technology Stack

```
FRONTEND
────────
Gradio Blocks
Custom HTML / CSS / JavaScript
Plotly / Cytoscape.js / vis-network
        │
        ▼
AI ENGINE
─────────
Groq API (LLM)
        │
        ▼
RESEARCH RETRIEVAL
──────────────────
Semantic Scholar API
OpenAlex API / Crossref
        │
        ▼
NLP / ANALYSIS
──────────────
Sentence Transformers
Embeddings
Cosine Similarity
Clustering
        │
        ▼
DATA
────
Pandas
JSON
NetworkX
        │
        ▼
GOOGLE COLAB
```

Gradio's **Blocks API** is the right choice here — it gives more layout/event control than the basic Interface API, and its HTML component supports custom HTML/CSS/JS for a highly customized UI.

---

## 13. Architecture Principle: Don't Let the LLM Do Everything

**❌ Bad architecture:**
```
User → LLM → "Here are 10 papers" → Graph
```
This risks hallucinated papers, URLs, statistics, and gaps.

**✅ Correct architecture:**
```
                    USER
                      ↓
                GROQ LLM
              Query Builder
                      ↓
             Academic APIs
          ┌───────────┴──────────┐
          ↓                      ↓
     Real Papers            Metadata
          │                      │
          └──────────┬───────────┘
                     ↓
                Embeddings
                     ↓
                 Similarity
                     ↓
                 Clusters
                     ↓
              Research Graph
                     ↓
              GROQ LLM
             Analysis Layer
                     ↓
        ┌────────────┼────────────┐
        ↓            ↓            ↓
     Summary       Gaps       Scope
```

- **Retrieval** provides the facts.
- **Algorithms** provide the relationships.
- **LLM** provides interpretation and readable explanation.

---

## 14. Final Product Concept

**AI-Based Research Scope Generator & Research Landscape Explorer**

### Core Modules

| # | Module | Function |
|---|---|---|
| 01 | Idea Intake | Accept free-form research ideas |
| 02 | AI Topic Understanding | Extract domain, problem, technologies, objectives, keywords |
| 03 | Academic Retrieval | Retrieve real papers from academic databases |
| 04 | Research Graph | Connect related research areas/papers via similarity and relationships |
| 05 | Paper Intelligence | Explain what each paper did — methodology, problem, limitations |
| 06 | Idea-to-Research Mapping | Explain how each direction relates to the user's idea |
| 07 | Scope Generator | Generate a possible research scope per direction |
| 08 | Saturation Analysis | Estimate research activity/saturation from literature signals |
| 09 | Scope × Saturation Matrix | Visualize research opportunity across the landscape |
| 10 | Paper Navigation | Give the user the real paper URL/DOI |

### Bonus Features

**A. Timeline** — publication activity over time for a selected area, to show whether it's emerging, growing, stable, or declining:
```
2019 ──●
2020 ───●
2021 ─────●
2022 ───────●
2023 ─────────●
2024 ───────────●
2025 ─────────────●
2026 ──────────────●
```

**B. Research Evolution:**
```
Traditional ML → Deep Learning → Transformers → Multimodal Models → Current Direction
```

**C. "Explore This Direction"** — clicking a node re-centers the entire analysis around it, so the user navigates through the landscape rather than just viewing it once.

### Core User Journey

```
Idea → Discover → Explore → Understand → Compare → Identify gaps → Generate scope → Analyze saturation → Read real papers
```

### Build Approach

Build in **phases**, not as one giant notebook:
1. Gradio UI + Groq structured analysis + real Semantic Scholar paper retrieval
2. Graph engine (embeddings, similarity, clustering)
3. Saturation engine + matrix visualization

First version can run entirely in **Google Colab** without a separate React app.

---

## 15. Suggested Additions

A few practical gaps worth covering before/while building — kept close to what's already planned, not new scope:

- **API rate limits & caching.** Semantic Scholar's public API has fairly strict rate limits. Add a simple cache layer (e.g., local JSON/SQLite keyed by query) so repeated searches for the same idea/topic don't re-hit the API, and add retry/backoff logic so the demo doesn't break mid-session.
- **Fallback when a query returns few/no papers.** Very niche or oddly-phrased ideas may return sparse results from Semantic Scholar. Since OpenAlex/Crossref are already in the stack, define the fallback order explicitly (Semantic Scholar → OpenAlex → Crossref) and show an honest empty/low-data state in the UI rather than letting the LLM fill the gap.
- **Deduplication across sources.** If you do pull from more than one academic API, papers can appear twice under different IDs — dedupe by DOI/title similarity before building the graph.
- **Handling vague input.** If the user's idea is too short or too broad (e.g., just "AI in healthcare"), the AI Interpretation Layer should detect low specificity and ask one clarifying question before running retrieval, instead of generating a shaky graph from thin input.
- **Confidence/evidence labeling in the UI, consistently.** You already planned the "explicit vs. inferred" distinction for gaps (section 7) — apply the same visual treatment (e.g., a small badge: "From paper" vs. "AI-inferred") everywhere the LLM adds interpretation, including scope generation and connection analysis, so it's consistent across the whole app.
- **Exporting the output.** Since the end product is a "Possible Research Scope," let the user export a generated scope (and maybe the paper list) as a `.txt`/`.md` file at minimum — useful for demo purposes and for the user's actual proposal writing.
- **Basic session state.** Even in Colab/Gradio, keep the last graph + scope in session state so clicking between nodes doesn't force a fresh API pull each time.
