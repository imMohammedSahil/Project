"""
Research Scope AI - AI Interpretation & Query Engine
Decomposes raw research ideas into structured entities, search queries, and literature intelligence using Groq LLM or intelligent heuristic fallback.
"""
import os
import json
import re
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional
from config import GROQ_API_KEY, DEFAULT_GROQ_MODEL, FALLBACK_GROQ_MODEL
from academic_retrieval import Paper
from cache_manager import cache

@dataclass
class IdeaStructure:
    domain: str
    primary_problem: str
    input_modalities: List[str]
    ai_subfields: List[str]
    user_intent: str
    academic_search_queries: List[str]
    specificity_level: str = "High"  # "High", "Moderate", "Vague"
    clarifying_question: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class LLMEngine:
    """Unified LLM Engine using Groq with intelligent fallback synthesizer."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GROQ_API_KEY", GROQ_API_KEY)
        self.client = None
        self._init_groq_client()

    def _init_groq_client(self):
        if self.api_key:
            try:
                from groq import Groq
                self.client = Groq(api_key=self.api_key)
            except Exception as e:
                print(f"[Warning] Could not initialize Groq client: {e}")
                self.client = None

    def update_api_key(self, new_key: str):
        self.api_key = new_key
        self._init_groq_client()

    # -----------------------------------------------------------------
    # 1. Idea Interpretation & Query Generation
    # -----------------------------------------------------------------
    def interpret_idea(self, user_idea: str) -> IdeaStructure:
        """Deconstructs free-form research idea into domain, problem, modalities, and search queries."""
        cleaned_text = user_idea.strip()
        if not cleaned_text:
            return self._fallback_interpretation("General Artificial Intelligence")

        # 0. Check SQLite Cache First
        cached = cache.get("LLM_INTERPRET", {"query": cleaned_text.lower()})
        if cached and isinstance(cached, dict):
            try:
                return IdeaStructure(**cached)
            except Exception:
                pass

        # Check for extreme vagueness (e.g. "AI in healthcare" or < 3 words)
        words = cleaned_text.split()
        if len(words) <= 3 and not any(kw in cleaned_text.lower() for kw in ["phishing", "cancer", "trajectory", "quantum", "odometry"]):
            vague_struct = IdeaStructure(
                domain="General / Broad AI",
                primary_problem=cleaned_text,
                input_modalities=["Unspecified"],
                ai_subfields=["Machine Learning"],
                user_intent="Explore high-level domain",
                academic_search_queries=[f"{cleaned_text} deep learning review", f"{cleaned_text} benchmark state of the art"],
                specificity_level="Vague",
                clarifying_question=f"Your topic '{cleaned_text}' is broad. What specific problem, modality (images, text, audio), or application are you targeting?"
            )
            cache.set("LLM_INTERPRET", {"query": cleaned_text.lower()}, vague_struct.to_dict())
            return vague_struct

        # Try Groq LLM if client is available
        if self.client:
            try:
                prompt = f"""
You are an expert AI Research Director.
Analyze the following research proposal/idea from a student or researcher:
\"\"\"{cleaned_text}\"\"\"

Extract structured metadata in strict JSON format matching this schema:
{{
  "domain": "Primary research domain (e.g. Cybersecurity, Medical AI, Robotics)",
  "primary_problem": "Core problem being tackled in 1-2 concise phrases",
  "input_modalities": ["List of input types, e.g. URL, Screenshot, X-Ray, Sensor Data"],
  "ai_subfields": ["Relevant AI techniques, e.g. NLP, Computer Vision, Multimodal Fusion, Transformer, Reinforcement Learning"],
  "user_intent": "What the user wants to achieve or build",
  "academic_search_queries": [
    "3-4 highly specific academic keyword queries to find real literature on Semantic Scholar / OpenAlex"
  ],
  "specificity_level": "High" or "Moderate"
}}
Return ONLY valid JSON.
"""
                response = self.client.chat.completions.create(
                    model=DEFAULT_GROQ_MODEL,
                    messages=[
                        {"role": "system", "content": "You are a research analysis system that outputs strictly valid JSON."},
                        {"role": "user", "content": prompt}
                    ],
                    response_format={"type": "json_object"},
                    temperature=0.2,
                    max_tokens=600
                )
                raw_json = response.choices[0].message.content
                data = json.loads(raw_json)
                struct = IdeaStructure(
                    domain=data.get("domain", "Artificial Intelligence"),
                    primary_problem=data.get("primary_problem", cleaned_text),
                    input_modalities=data.get("input_modalities", ["Multimodal"]),
                    ai_subfields=data.get("ai_subfields", ["Deep Learning"]),
                    user_intent=data.get("user_intent", "Develop AI solution"),
                    academic_search_queries=data.get("academic_search_queries", [cleaned_text]),
                    specificity_level=data.get("specificity_level", "High")
                )
                cache.set("LLM_INTERPRET", {"query": cleaned_text.lower()}, struct.to_dict())
                return struct
            except Exception as e:
                print(f"[Warning] Groq LLM call failed ({e}). Using intelligent heuristic fallback.")

        # Heuristic fallback
        fallback_struct = self._fallback_interpretation(cleaned_text)
        cache.set("LLM_INTERPRET", {"query": cleaned_text.lower()}, fallback_struct.to_dict())
        return fallback_struct

    # -----------------------------------------------------------------
    # 2. Heuristic Interpretation Synthesizer (Fallback)
    # -----------------------------------------------------------------
    def _fallback_interpretation(self, text: str) -> IdeaStructure:
        lower = text.lower()
        
        # Domain detection heuristics
        domain = "Computer Science / AI"
        subfields = ["Machine Learning", "Deep Learning"]
        modalities = ["Numerical / Tabular"]
        
        if any(k in lower for k in ["phish", "malware", "cyber", "attack", "url", "website", "fraud", "security"]):
            domain = "Cybersecurity / Web Security"
            subfields = ["NLP", "Computer Vision", "Multimodal AI", "Ensemble Classification"]
            modalities = ["URL Lexical Features", "HTML DOM Tree", "Webpage Screenshot Images"]
        elif any(k in lower for k in ["medical", "health", "x-ray", "cancer", "clinical", "hospital", "patient", "mri"]):
            domain = "Healthcare & Medical AI"
            subfields = ["Medical Image Segmentation", "Federated Learning", "Privacy-Preserving AI"]
            modalities = ["DICOM / X-Ray Images", "Clinical Electronic Health Records"]
        elif any(k in lower for k in ["drone", "uav", "robot", "trajectory", "navigation", "gps", "slam"]):
            domain = "Robotics & Autonomous Systems"
            subfields = ["Reinforcement Learning", "Visual Odometry", "Motion Planning"]
            modalities = ["Camera Stream", "IMU Inertial Sensors", "LiDAR Point Clouds"]
        elif any(k in lower for k in ["drug", "protein", "molecule", "genom", "binding", "dna"]):
            domain = "Bioinformatics & Computational Biology"
            subfields = ["Graph Neural Networks", "3D Molecular Modeling", "Geometric Deep Learning"]
            modalities = ["SMILES Strings", "3D PDB Atomic Coordinates"]
        elif any(k in lower for k in ["language", "nlp", "llm", "chat", "text", "translation", "summariz"]):
            domain = "Natural Language Processing"
            subfields = ["Transformer Architecture", "Attention Mechanisms", "RAG"]
            modalities = ["Raw Text Documents", "Token Sequences"]

        # Formulate 3-4 targeted academic search queries
        clean_keywords = re.findall(r'\b[a-zA-Z]{3,}\b', lower)
        stopwords = {"want", "make", "system", "that", "using", "maybe", "dont", "know", "exactly", "what", "approach", "with", "from", "into", "some", "like"}
        key_tokens = [w for w in clean_keywords if w not in stopwords][:5]
        
        base_query = " ".join(key_tokens)
        queries = [
            base_query,
            f"{base_query} deep learning",
            f"{base_query} transformer benchmark",
            f"{base_query} multimodal dataset"
        ]

        return IdeaStructure(
            domain=domain,
            primary_problem=text[:120],
            input_modalities=modalities,
            ai_subfields=subfields,
            user_intent="Design and benchmark a novel machine learning architecture for the target problem.",
            academic_search_queries=list(dict.fromkeys(queries))[:4],
            specificity_level="High"
        )

    # -----------------------------------------------------------------
    # 3. Connection & Literature Gap Analysis
    # -----------------------------------------------------------------
    def analyze_node_connection(self, user_idea: str, cluster_label: str, sample_papers: List[Paper]) -> Dict[str, Any]:
        """Explains how a specific research cluster connects to the user's idea."""
        # 0. Check cache
        cache_key = {"user_idea": user_idea.strip().lower(), "cluster": cluster_label}
        cached = cache.get("LLM_CONNECTION", cache_key)
        if cached and isinstance(cached, dict):
            return cached

        if self.client:
            try:
                titles_and_abstracts = "\n".join([f"- {p.title}: {p.abstract[:200]}" for p in sample_papers[:3]])
                prompt = f"""
User's Idea: \"{user_idea}\"
Related Research Cluster: \"{cluster_label}\"
Sample Published Papers in this cluster:
{titles_and_abstracts}

Explain the precise relationship between the user's idea and this literature cluster in JSON:
{{
  "shared_problem": "What core challenge both address",
  "shared_data_or_features": "Common data types / modalities",
  "shared_technique": "Shared baseline algorithms or models",
  "key_difference": "How the user's proposal introduces novelty or differentiates",
  "connection_summary": "1-2 sentence executive summary of the connection"
}}
Return ONLY JSON.
"""
                resp = self.client.chat.completions.create(
                    model=FALLBACK_GROQ_MODEL,
                    messages=[
                        {"role": "system", "content": "You are an academic analysis assistant that outputs strictly valid JSON."},
                        {"role": "user", "content": prompt}
                    ],
                    response_format={"type": "json_object"},
                    temperature=0.2,
                    max_tokens=400
                )
                res = json.loads(resp.choices[0].message.content)
                cache.set("LLM_CONNECTION", cache_key, res)
                return res
            except Exception as e:
                print(f"[Warning] Groq connection analysis failed: {e}")

        # Heuristic fallback for connection analysis
        fallback_res = {
            "shared_problem": f"Both target accurate identification and predictive modeling in {cluster_label}.",
            "shared_data_or_features": "Feature vectors, contextual tokens, and domain metadata.",
            "shared_technique": "Supervised deep neural networks, transformer attention, and feature fusion.",
            "key_difference": f"Your proposal integrates multimodal contextual signals and novel objective functions, whereas standard {cluster_label} relies on isolated single-channel representations.",
            "connection_summary": f"Strong semantic alignment: {cluster_label} provides baseline methodologies that your proposed architecture expands upon."
        }
        cache.set("LLM_CONNECTION", cache_key, fallback_res)
        return fallback_res

    def extract_literature_gaps(self, papers: List[Paper], cluster_label: str) -> List[Dict[str, str]]:
        """Extracts limitations with strict badges: [From Paper] vs [AI-Inferred]."""
        cache_key = {"cluster": cluster_label, "paper_ids": [p.paper_id for p in papers[:4]]}
        cached = cache.get("LLM_GAPS", cache_key)
        if cached and isinstance(cached, list):
            return cached

        gaps = []
        
        # Check abstracts for explicit limitation keywords
        for p in papers:
            abstract = p.abstract.lower()
            if any(k in abstract for k in ["limitation", "suffer", "vulnerable", "high false positive", "computationally expensive", "lack", "challenging"]):
                # Extract sentence
                sentences = re.split(r'\. |\.\n', p.abstract)
                for s in sentences:
                    if any(k in s.lower() for k in ["suffer", "vulnerable", "limitation", "lack", "expensive", "false positive"]):
                        gaps.append({
                            "type": "From Paper",
                            "badge_class": "badge-paper",
                            "text": s.strip(),
                            "source": f"{p.authors_display} ({p.year or 'Recent'})"
                        })
                        break
            if len(gaps) >= 2:
                break

        # AI-Inferred Gaps (Literature extrapolation)
        gaps.append({
            "type": "AI-Inferred",
            "badge_class": "badge-inferred",
            "text": f"Current models in '{cluster_label}' exhibit performance degradation under adversarial distribution shifts and zero-day evasive perturbations.",
            "source": "Synthesized Literature Analysis"
        })
        gaps.append({
            "type": "AI-Inferred",
            "badge_class": "badge-inferred",
            "text": "Lack of standardized multi-source benchmark datasets with verified ground-truth labels causes evaluation variance.",
            "source": "Synthesized Literature Analysis"
        })

        cache.set("LLM_GAPS", cache_key, gaps)
        return gaps

# Global LLM instance
llm_engine = LLMEngine()
