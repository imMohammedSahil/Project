"""
Research Scope AI - Global Configuration & Settings
"""
import os
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).parent.resolve()
CACHE_DIR = BASE_DIR / ".cache"
CACHE_DIR.mkdir(exist_ok=True)
CACHE_DB_PATH = CACHE_DIR / "academic_cache.db"
EXPORT_DIR = BASE_DIR / "exports"
EXPORT_DIR.mkdir(exist_ok=True)

# API Keys (Loaded from environment or fallback)
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
SEMANTIC_SCHOLAR_API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY", "")

# Academic APIs Endpoints
SEMANTIC_SCHOLAR_SEARCH_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
SEMANTIC_SCHOLAR_RECOMMEND_URL = "https://api.semanticscholar.org/recommendations/v1/papers/forpaper"
OPENALEX_SEARCH_URL = "https://api.openalex.org/works"
CROSSREF_SEARCH_URL = "https://api.crossref.org/works"

# Retrieval Settings
DEFAULT_PAPERS_PER_QUERY = 8
MAX_PAPERS_TOTAL = 35
API_TIMEOUT_SECONDS = 12
CACHE_TTL_DAYS = 14

# User-Agent for Academic APIs (OpenAlex & Semantic Scholar appreciate identification)
USER_AGENT = "ResearchScopeAI/1.0 (academic-research-tool; contact@researchscope.ai)"

# Groq LLM Defaults
DEFAULT_GROQ_MODEL = "openai/gpt-oss-120b"
FALLBACK_GROQ_MODEL = "qwen/qwen3.8-27b"

# Default Sample Research Ideas for Instant Demo
SAMPLE_IDEAS = [
    {
        "title": "Multimodal Phishing & Fake Website Detection",
        "domain": "Cybersecurity / Multimodal AI",
        "description": "I want to make an AI system that can detect fake websites and phishing attacks using URL lexical semantics, HTML structural elements, and webpage screenshots with explainable attention maps."
    },
    {
        "title": "Federated Learning for Medical Imaging with Privacy Guarantees",
        "domain": "Healthcare / Distributed AI",
        "description": "Developing a privacy-preserving federated learning framework for multi-hospital chest X-ray disease classification without sharing patient data, focusing on non-IID data distribution and differential privacy."
    },
    {
        "title": "Autonomous Drone Trajectory Planning in GPS-Denied Environments",
        "domain": "Robotics / Computer Vision",
        "description": "Visual-inertial odometry and reinforcement learning for real-time collision-free drone trajectory planning in indoor, GPS-denied, cluttered environments."
    },
    {
        "title": "Graph Neural Networks for Drug-Target Interaction Prediction",
        "domain": "Bioinformatics / Graph AI",
        "description": "Using geometric deep learning and graph neural networks to predict drug-target binding affinity with 3D molecular conformation graphs and interpret binding site residues."
    }
]
