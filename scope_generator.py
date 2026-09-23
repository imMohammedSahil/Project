"""
Research Scope AI - Research Scope Generator
Synthesizes literature gaps, paper metadata, and user intent into a publication-grade research scope.
"""
import json
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional
from config import DEFAULT_GROQ_MODEL
from llm_engine import llm_engine
from academic_retrieval import Paper
from cache_manager import cache

@dataclass
class ResearchScope:
    title: str
    problem_statement: str
    research_questions: List[str]
    objectives: List[str]
    proposed_methodology: str
    suggested_datasets: List[str]
    evaluation_metrics: List[str]
    expected_contributions: List[str]
    cluster_source: str
    baseline_papers: List[Dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_markdown(self) -> str:
        md = f"# Research Scope Proposal: {self.title}\n\n"
        md += f"**Target Literature Cluster:** `{self.cluster_source}`\n\n"
        md += "## 1. Problem Statement\n"
        md += f"{self.problem_statement}\n\n"
        
        md += "## 2. Core Research Questions\n"
        for i, rq in enumerate(self.research_questions, 1):
            md += f"- **RQ{i}:** {rq}\n"
        md += "\n"

        md += "## 3. Step-by-Step Research Objectives\n"
        for i, obj in enumerate(self.objectives, 1):
            md += f"- **RO{i}:** {obj}\n"
        md += "\n"

        md += "## 4. Proposed Methodology & Architecture\n"
        md += f"{self.proposed_methodology}\n\n"

        md += "## 5. Target Datasets & Benchmarks\n"
        for ds in self.suggested_datasets:
            md += f"- {ds}\n"
        md += "\n"

        md += "## 6. Evaluation Metrics & Baselines\n"
        for metric in self.evaluation_metrics:
            md += f"- {metric}\n"
        md += "\n"

        md += "## 7. Expected Scientific Contributions\n"
        for i, contrib in enumerate(self.expected_contributions, 1):
            md += f"{i}. {contrib}\n"
        md += "\n"

        if self.baseline_papers:
            md += "## 8. Real Literature Anchor Papers\n"
            for p in self.baseline_papers:
                md += f"- **{p.get('title')}** ({p.get('year', 'Recent')})\n"
                md += f"  *Authors:* {p.get('authors_display', 'N/A')} | *Citations:* {p.get('citation_count', 0)}\n"
                md += f"  *Link:* [{p.get('clean_url', p.get('url', 'DOI link'))}]({p.get('clean_url', p.get('url', '#'))})\n\n"

        return md


class ScopeGeneratorEngine:
    """Generates structured research scopes using Groq LLM or high-fidelity template synthesis."""

    def generate_scope(
        self,
        user_idea: str,
        cluster_name: str,
        papers: List[Paper],
        gaps: List[Dict[str, str]]
    ) -> ResearchScope:
        """Generates comprehensive academic research scope."""
        # 0. Check cache
        cache_key = {"user_idea": user_idea.strip().lower(), "cluster": cluster_name}
        cached = cache.get("LLM_SCOPE", cache_key)
        if cached and isinstance(cached, dict):
            try:
                return ResearchScope(**cached)
            except Exception:
                pass
        
        # Prepare context
        papers_context = "\n".join([f"- {p.title} ({p.year or 'Recent'}): {p.abstract[:180]}" for p in papers[:4]])
        gaps_context = "\n".join([f"- [{g['type']}] {g['text']}" for g in gaps[:3]])

        # 1. Try Groq LLM
        if llm_engine.client:
            try:
                prompt = f"""
You are an expert AI Research Advisor drafting a rigorous formal research proposal.
User's Idea: \"{user_idea}\"
Literature Cluster: \"{cluster_name}\"

Evidence-backed Gaps:
{gaps_context}

Relevant Literature Papers:
{papers_context}

Draft a complete, academic-grade research proposal scope in valid JSON:
{{
  "title": "Academic, formal working title",
  "problem_statement": "2-3 paragraphs defining the challenge, why existing solutions fail, and the critical motivation",
  "research_questions": [
    "RQ1: Empirical question regarding feature representation / data modality",
    "RQ2: Methodological question on model fusion / loss design",
    "RQ3: Comparative question on robustness and explainability"
  ],
  "objectives": [
    "RO1: Formulate curated dataset benchmark with multimodal inputs",
    "RO2: Design cross-attention alignment architecture",
    "RO3: Implement explainability / attention attribution mechanism",
    "RO4: Empirically validate against SOTA baselines"
  ],
  "proposed_methodology": "Detailed description of the architectural pipeline, feature extraction, multimodal fusion, and training objective.",
  "suggested_datasets": ["List of 2-3 standard or proposed benchmark datasets"],
  "evaluation_metrics": ["Precision", "Recall", "Macro-F1", "ROC-AUC", "Inference Latency (ms)"],
  "expected_contributions": [
    "Novel multimodal fusion architecture bridging text and visual signals",
    "First benchmark study evaluating zero-day evasion robustness",
    "Open-source reproducible implementation and model weights"
  ]
}}
Return ONLY strict JSON.
"""
                resp = llm_engine.client.chat.completions.create(
                    model=DEFAULT_GROQ_MODEL,
                    messages=[
                        {"role": "system", "content": "You are a research proposal generator that strictly outputs valid JSON."},
                        {"role": "user", "content": prompt}
                    ],
                    response_format={"type": "json_object"},
                    temperature=0.3,
                    max_tokens=2500
                )
                data = json.loads(resp.choices[0].message.content)
                scope = ResearchScope(
                    title=data.get("title", f"Advanced {cluster_name} for Robust Prediction"),
                    problem_statement=data.get("problem_statement", f"Investigation of {cluster_name} to address {user_idea}."),
                    research_questions=data.get("research_questions", ["How to improve multimodal detection?"]),
                    objectives=data.get("objectives", ["Develop novel fusion architecture"]),
                    proposed_methodology=data.get("proposed_methodology", "End-to-end deep neural network pipeline with cross-modal attention."),
                    suggested_datasets=data.get("suggested_datasets", ["Standard Domain Benchmark Dataset"]),
                    evaluation_metrics=data.get("evaluation_metrics", ["Precision", "Recall", "F1-Score", "ROC-AUC"]),
                    expected_contributions=data.get("expected_contributions", ["Novel architectural paradigm", "Benchmark evaluation"]),
                    cluster_source=cluster_name,
                    baseline_papers=[p.to_dict() for p in papers[:4]]
                )
                cache.set("LLM_SCOPE", cache_key, scope.to_dict())
                return scope
            except Exception as e:
                print(f"[Warning] Groq Scope generation failed ({e}). Using template synthesizer.")

        # 2. Heuristic Academic Template Synthesizer (Fallback)
        fallback_scope = self._synthesize_fallback_scope(user_idea, cluster_name, papers, gaps)
        cache.set("LLM_SCOPE", cache_key, fallback_scope.to_dict())
        return fallback_scope

    def _synthesize_fallback_scope(
        self,
        user_idea: str,
        cluster_name: str,
        papers: List[Paper],
        gaps: List[Dict[str, str]]
    ) -> ResearchScope:
        title = f"Multimodal Deep Learning Framework for {cluster_name}: An Explainable and Robust Architecture"
        
        problem = (
            f"Current automated detection systems in '{cluster_name}' predominantly rely on isolated unimodal "
            f"features, creating severe blind spots against sophisticated evasion tactics and distribution shifts. "
            f"While existing literature establishes foundational baseline models, they exhibit elevated false-positive "
            f"rates in real-world deployments. This research addresses this gap by synthesizing '{user_idea}' into a "
            f"unified, end-to-end differentiable framework that fuses complementary contextual and visual signals."
        )

        rqs = [
            f"RQ1: How do cross-modal attention mechanisms between textual semantics and visual features impact detection accuracy compared to unimodal baselines?",
            f"RQ2: What is the optimal joint representation strategy to preserve spatial layout context without incurring prohibitive computational overhead?",
            f"RQ3: How effectively does the proposed framework withstand adversarial perturbations and zero-day distribution shifts in real-time scenarios?"
        ]

        objs = [
            f"RO1: Construct and curate a standardized multimodal dataset incorporating verified ground-truth labels and diverse domain variations.",
            f"RO2: Formulate a lightweight cross-attention fusion transformer that dynamically weights feature modalities based on signal confidence.",
            f"RO3: Integrate post-hoc feature attribution (Grad-CAM and Integrated Gradients) to deliver human-interpretable prediction rationales.",
            f"RO4: Perform extensive ablation studies and benchmark against top contemporary models across precision, recall, and inference latency."
        ]

        methodology = (
            "The proposed architecture consists of three integrated stages:\n"
            "1. Feature Extraction: Dual-branch encoder utilizing fine-tuned transformer tokenizers for lexical semantics and convolutional/vision-transformer backbones for visual artifacts.\n"
            "2. Multimodal Fusion: Cross-attention fusion layer with residual gating to prioritize informative signals and suppress noisy modalities.\n"
            "3. Classification & Explainability: Joint classification head optimized via Focal Cross-Entropy Loss with integrated attention weight visualization for auditability."
        )

        datasets = [
            "Curated Multimodal Benchmark Corpus (2024-2025)",
            "Standard Public Domain Repository (Verified DOIs)",
            "Augmented Adversarial Evaluation Suite"
        ]

        metrics = [
            "Macro-Precision, Recall, and F1-Score",
            "Area Under the ROC Curve (ROC-AUC)",
            "Mean Inference Latency per Sample (milliseconds)",
            "Attention Map IoU (Explainability Fidelity)"
        ]

        contributions = [
            "A novel cross-modal fusion architecture bridging disparate feature modalities for robust classification.",
            "Comprehensive empirical benchmarking demonstrating state-of-the-art performance against zero-day evasions.",
            "Integrated explainability module providing token-level and visual-level verification for domain practitioners.",
            "Open-source benchmark pipeline and pre-trained model checkpoints to facilitate reproducible future research."
        ]

        return ResearchScope(
            title=title,
            problem_statement=problem,
            research_questions=rqs,
            objectives=objs,
            proposed_methodology=methodology,
            suggested_datasets=datasets,
            evaluation_metrics=metrics,
            expected_contributions=contributions,
            cluster_source=cluster_name,
            baseline_papers=[p.to_dict() for p in papers[:4]]
        )

# Global scope engine instance
scope_generator = ScopeGeneratorEngine()
