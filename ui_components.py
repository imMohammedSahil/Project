"""
Research Scope AI - UI Components & Custom Styling
Defines glassmorphism CSS, card renderers, and HTML templates for Gradio.
Clean, modern enterprise styling with zero emojis.
"""
from typing import Dict, Any, List
from academic_retrieval import Paper
from llm_engine import IdeaStructure

CUSTOM_CSS = """
/* Import Modern Typography */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg-primary: #090D16;
    --bg-secondary: #0F172A;
    --bg-card: rgba(15, 23, 42, 0.75);
    --border-color: rgba(255, 255, 255, 0.08);
    --border-highlight: rgba(99, 102, 241, 0.4);
    --accent-indigo: #6366F1;
    --accent-cyan: #0EA5E9;
    --accent-emerald: #10B981;
    --accent-purple: #8B5CF6;
    --accent-rose: #F43F5E;
    --text-main: #F8FAFC;
    --text-secondary: #94A3B8;
    --text-muted: #64748B;
}

body, .gradio-container {
    background-color: var(--bg-primary) !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    color: var(--text-main) !important;
    max-width: 1440px !important;
    margin: 0 auto !important;
    padding: 16px 20px !important;
}

footer {
    display: none !important;
}

/* Semantic decomposition and knowledge graph tab */
.graph-tab-hero {
    position: relative;
    overflow: hidden;
    margin: 4px 0 16px;
    padding: 22px 26px;
    border: 1px solid rgba(129, 140, 248, 0.22);
    border-radius: 16px;
    background:
        radial-gradient(circle at 88% 20%, rgba(14, 165, 233, 0.16), transparent 28%),
        radial-gradient(circle at 12% 110%, rgba(99, 102, 241, 0.18), transparent 34%),
        linear-gradient(110deg, rgba(15, 23, 42, 0.98), rgba(24, 31, 63, 0.92));
    box-shadow: 0 14px 34px rgba(2, 6, 23, 0.24), inset 0 1px rgba(255, 255, 255, 0.06);
}

.graph-tab-hero::after {
    content: "";
    position: absolute;
    width: 180px;
    height: 180px;
    right: 7%;
    top: -108px;
    border: 1px solid rgba(165, 180, 252, 0.18);
    border-radius: 50%;
    box-shadow: 0 0 0 22px rgba(165, 180, 252, 0.035), 0 0 0 44px rgba(165, 180, 252, 0.025);
}

.graph-tab-kicker {
    position: relative;
    z-index: 1;
    color: #67E8F9;
    font: 700 10px/1.2 'JetBrains Mono', monospace;
    letter-spacing: 1.6px;
}

.graph-tab-kicker span {
    display: inline-block;
    width: 5px;
    height: 5px;
    margin: 0 8px 2px;
    border-radius: 50%;
    background: #34D399;
    box-shadow: 0 0 10px #34D399;
}

.graph-tab-title {
    position: relative;
    z-index: 1;
    margin-top: 9px;
    color: #F8FAFC;
    font: 800 25px/1.15 'Outfit', sans-serif;
    letter-spacing: -0.5px;
}

.graph-tab-title em {
    color: #A5B4FC;
    font-style: normal;
}

.graph-tab-subtitle {
    position: relative;
    z-index: 1;
    max-width: 650px;
    margin-top: 8px;
    color: #94A3B8;
    font-size: 12.5px;
    line-height: 1.55;
}

.graph-tab-grid {
    gap: 16px !important;
}

.graph-tab-panel {
    min-width: 0;
    padding: 0 !important;
}

.graph-tab-panel > .block {
    height: 100%;
}

.graph-visual-panel {
    overflow: hidden;
    border: 1px solid rgba(56, 189, 248, 0.16);
    border-radius: 14px;
    background: linear-gradient(145deg, rgba(15, 23, 42, 0.94), rgba(8, 15, 31, 0.98));
    box-shadow: 0 14px 30px rgba(2, 6, 23, 0.22);
}

.knowledge-graph-plot {
    padding: 6px !important;
}

.knowledge-graph-plot .wrap {
    border-radius: 10px;
}

@media (max-width: 900px) {
    .graph-tab-title {
        font-size: 21px;
    }
}

/* Glassmorphism Containers */
.glass-panel {
    background: var(--bg-card) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 12px !important;
    padding: 20px !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35) !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.glass-panel:hover {
    border-color: rgba(255, 255, 255, 0.14) !important;
}

.hero-header {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.12) 0%, rgba(14, 165, 233, 0.08) 50%, rgba(15, 23, 42, 0.6) 100%);
    border: 1px solid rgba(99, 102, 241, 0.25);
    border-radius: 14px;
    padding: 22px 28px;
    margin-bottom: 20px;
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.3);
}

.hero-title {
    font-family: 'Outfit', sans-serif;
    font-size: 28px;
    font-weight: 800;
    background: linear-gradient(90deg, #FFFFFF 0%, #C7D2FE 40%, #7DD3FC 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    letter-spacing: -0.5px;
    display: flex;
    align-items: center;
    gap: 12px;
}

.hero-subtitle {
    color: #94A3B8;
    font-size: 13.5px;
    margin-top: 6px;
    font-weight: 400;
    letter-spacing: 0.2px;
}

/* System Status Indicator Dots */
.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 5px 12px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.4px;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
}

.status-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    display: inline-block;
}

.status-active {
    background: rgba(16, 185, 129, 0.12);
    color: #34D399;
    border: 1px solid rgba(16, 185, 129, 0.3);
}

.status-active .status-dot {
    background: #10B981;
    box-shadow: 0 0 8px #10B981;
}

.status-llm {
    background: rgba(99, 102, 241, 0.12);
    color: #A5B4FC;
    border: 1px solid rgba(99, 102, 241, 0.3);
}

.status-llm .status-dot {
    background: #6366F1;
    box-shadow: 0 0 8px #6366F1;
}

/* Badges */
.badge-tag {
    display: inline-flex;
    align-items: center;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 600;
    margin: 2px 4px 2px 0;
    letter-spacing: 0.3px;
    font-family: 'Inter', sans-serif;
}

.badge-paper {
    background: rgba(16, 185, 129, 0.15);
    color: #34D399;
    border: 1px solid rgba(16, 185, 129, 0.35);
}

.badge-inferred {
    background: rgba(139, 92, 246, 0.15);
    color: #C084FC;
    border: 1px solid rgba(139, 92, 246, 0.35);
}

.badge-domain {
    background: rgba(99, 102, 241, 0.15);
    color: #A5B4FC;
    border: 1px solid rgba(99, 102, 241, 0.35);
}

.badge-neutral {
    background: rgba(148, 163, 184, 0.12);
    color: #CBD5E1;
    border: 1px solid rgba(148, 163, 184, 0.25);
}

/* Card Styling */
.research-card {
    background: rgba(15, 23, 42, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    padding: 16px 18px;
    margin-bottom: 12px;
    transition: all 0.2s ease-in-out;
}

.research-card:hover {
    border-color: rgba(99, 102, 241, 0.4);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.35);
    transform: translateY(-1px);
}

.card-title {
    font-family: 'Outfit', sans-serif;
    font-size: 15.5px;
    font-weight: 700;
    color: #F8FAFC;
    margin-bottom: 6px;
    line-height: 1.4;
}

.meta-row {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 12px;
    color: #94A3B8;
    font-size: 12px;
    margin-bottom: 8px;
}

.paper-abstract {
    color: #CBD5E1;
    font-size: 12.5px;
    line-height: 1.6;
    margin-top: 6px;
}

.btn-doi {
    display: inline-flex;
    align-items: center;
    background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%);
    color: #FFFFFF !important;
    padding: 5px 12px;
    border-radius: 6px;
    font-size: 11.5px;
    font-weight: 600;
    text-decoration: none;
    margin-top: 8px;
    letter-spacing: 0.2px;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.btn-doi:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.35);
}

/* Refined Form Controls */
textarea, input[type="text"] {
    background: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 8px !important;
    color: #F8FAFC !important;
    font-family: 'Inter', sans-serif !important;
}

textarea:focus, input[type="text"]:focus {
    border-color: #6366F1 !important;
    box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.25) !important;
}

.primary-btn {
    background: linear-gradient(135deg, #4F46E5 0%, #6366F1 50%, #0EA5E9 100%) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    letter-spacing: 0.3px !important;
    border: none !important;
    border-radius: 8px !important;
    box-shadow: 0 4px 16px rgba(99, 102, 241, 0.35) !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
}

.primary-btn:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 22px rgba(99, 102, 241, 0.5) !important;
}

/* Modern Tabs */
.tab-nav {
    background: rgba(15, 23, 42, 0.6) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 10px !important;
    padding: 6px !important;
    gap: 6px !important;
    margin-bottom: 18px !important;
}

.tab-nav button {
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    color: #94A3B8 !important;
    padding: 8px 18px !important;
    border: 1px solid transparent !important;
    transition: all 0.2s ease !important;
    font-family: 'Inter', sans-serif !important;
}

.tab-nav button:hover {
    color: #F8FAFC !important;
    background: rgba(255, 255, 255, 0.05) !important;
}

.tab-nav button.selected {
    background: rgba(99, 102, 241, 0.22) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(99, 102, 241, 0.45) !important;
    box-shadow: 0 4px 14px rgba(99, 102, 241, 0.25) !important;
}

/* Accordion Styling */
.gr-accordion {
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 8px !important;
    background: rgba(15, 23, 42, 0.4) !important;
}
"""

def render_hero_header() -> str:
    return """
    <div class="hero-header">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
            <div>
                <h1 class="hero-title">RESEARCH SCOPE AI</h1>
                <p class="hero-subtitle">Evidence-Backed Research Landscape Explorer & Autonomous Scope Generator</p>
            </div>
            <div style="display:flex; gap:10px; flex-wrap:wrap;">
                <span class="status-pill status-active"><span class="status-dot"></span>Semantic Scholar & OpenAlex Live</span>
                <span class="status-pill status-llm"><span class="status-dot"></span>Groq Neural Synthesizer</span>
            </div>
        </div>
    </div>
    """

def render_concept_breakdown(idea: IdeaStructure) -> str:
    modalities_html = "".join([f'<span class="badge-tag badge-domain" style="font-size:12px; padding:4px 10px;">{m}</span>' for m in idea.input_modalities])
    subfields_html = "".join([f'<span class="badge-tag badge-inferred" style="font-size:12px; padding:4px 10px;">{s}</span>' for s in idea.ai_subfields])
    queries_html = "".join([f'<li style="margin:6px 0; color:#E2E8F0;"><code style="background:rgba(0,0,0,0.35); padding:3px 8px; border-radius:4px; font-size:12px; font-family:\'JetBrains Mono\', monospace; border:1px solid rgba(255,255,255,0.06);">{q}</code></li>' for q in idea.academic_search_queries])

    return f"""
    <div class="glass-panel">
        <!-- Live Execution Pipeline Progress Bar -->
        <div style="display:flex; align-items:center; gap:8px; margin-bottom:14px; padding:8px 12px; background:rgba(99,102,241,0.08); border-radius:8px; border:1px solid rgba(99,102,241,0.25); flex-wrap:wrap;">
            <span style="font-size:11px; font-weight:700; color:#A5B4FC; text-transform:uppercase; letter-spacing:0.5px; font-family:'JetBrains Mono', monospace;">PIPELINE:</span>
            <span class="badge-tag badge-paper">1. SEMANTIC DECOMPOSITION</span>
            <span style="color:#64748B;">&rarr;</span>
            <span class="badge-tag badge-paper">2. ACADEMIC RETRIEVAL</span>
            <span style="color:#64748B;">&rarr;</span>
            <span class="badge-tag badge-paper">3. KNOWLEDGE GRAPH</span>
            <span style="color:#64748B;">&rarr;</span>
            <span class="badge-tag badge-domain">4. GAP DISCOVERY</span>
        </div>

        <!-- AI Interpretation Layer Header -->
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:8px;">
            <span style="font-family:'Outfit', sans-serif; font-size:16px; font-weight:800; color:#F8FAFC; text-transform:uppercase; letter-spacing:0.5px;">AI Interpretation Layer</span>
            <span class="badge-tag {'badge-paper' if idea.specificity_level=='High' else 'badge-inferred'}" style="font-size:12px; padding:4px 12px;">Specificity: {idea.specificity_level}</span>
        </div>
        
        <div style="display:grid; grid-template-columns: 1fr 2fr; gap:10px; margin-bottom:14px;">
            <div style="background:rgba(15,23,42,0.7); padding:10px 14px; border-radius:8px; border:1px solid rgba(255,255,255,0.08);">
                <div style="font-size:10.5px; color:#94A3B8; text-transform:uppercase; font-weight:700; letter-spacing:0.5px;">Primary Domain</div>
                <div style="font-size:14.5px; color:#F1F5F9; font-weight:700; margin-top:2px;">{idea.domain}</div>
            </div>
            <div style="background:rgba(15,23,42,0.7); padding:10px 14px; border-radius:8px; border:1px solid rgba(255,255,255,0.08);">
                <div style="font-size:10.5px; color:#94A3B8; text-transform:uppercase; font-weight:700; letter-spacing:0.5px;">Target Problem</div>
                <div style="font-size:13px; color:#F1F5F9; margin-top:2px; line-height:1.4;">{idea.primary_problem}</div>
            </div>
        </div>

        <div style="margin-bottom:12px;">
            <div style="font-size:10.5px; color:#94A3B8; text-transform:uppercase; font-weight:700; margin-bottom:6px; letter-spacing:0.5px;">Input Modalities:</div>
            {modalities_html}
        </div>

        <div style="margin-bottom:14px;">
            <div style="font-size:10.5px; color:#94A3B8; text-transform:uppercase; font-weight:700; margin-bottom:6px; letter-spacing:0.5px;">AI Subfields & Techniques:</div>
            {subfields_html}
        </div>

        <div style="background:rgba(15,23,42,0.6); padding:12px 14px; border-radius:8px; border:1px solid rgba(255,255,255,0.06);">
            <div style="font-size:10.5px; color:#94A3B8; text-transform:uppercase; font-weight:700; letter-spacing:0.5px; margin-bottom:6px;">Automated Academic Queries (Semantic Scholar / OpenAlex):</div>
            <ul style="margin:4px 0 0 16px; padding:0; font-size:12px;">
                {queries_html}
            </ul>
        </div>
    </div>
    """

def render_node_deep_dive(cluster_name: str, connection_info: Dict[str, Any], gaps: List[Dict[str, str]], papers: List[Paper]) -> str:
    gaps_html = ""
    for g in gaps:
        badge_cls = "badge-paper" if g["type"] == "From Paper" else "badge-inferred"
        gaps_html += f"""
        <div style="margin-bottom:8px; padding:10px 14px; background:rgba(15,23,42,0.6); border-radius:8px; border-left:3px solid {'#10B981' if g['type']=='From Paper' else '#8B5CF6'};">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <span class="badge-tag {badge_cls}">[{'PUBLISHED LITERATURE' if g['type']=='From Paper' else 'AI-SYNTHESIZED'}]</span>
                <span style="font-size:11px; color:#94A3B8;">Anchor: {g.get('source', 'Literature')}</span>
            </div>
            <div style="font-size:12.5px; color:#E2E8F0; line-height:1.5;">{g['text']}</div>
        </div>
        """

    papers_html = ""
    for p in papers:
        papers_html += f"""
        <div class="research-card">
            <div class="card-title">{p.title}</div>
            <div class="meta-row">
                <span>Author: {p.authors_display}</span>
                <span>Year: {p.year or 'Recent'}</span>
                <span>Citations: {p.citation_count}</span>
                <span class="badge-tag badge-paper">{p.source_api}</span>
            </div>
            <div class="paper-abstract">{p.abstract}</div>
            <a href="{p.clean_url}" target="_blank" class="btn-doi">View Verified Source / DOI &rarr;</a>
        </div>
        """

    return f"""
    <div style="margin-top:8px;">
        <div class="glass-panel" style="margin-bottom:14px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                <h2 style="font-family:'Outfit'; font-size:18px; color:#F8FAFC; margin:0; text-transform:uppercase; letter-spacing:0.4px;">Direction: {cluster_name}</h2>
                <span class="badge-tag badge-domain">{len(papers)} Anchor Papers</span>
            </div>
            
            <div style="background:rgba(99,102,241,0.08); border:1px solid rgba(99,102,241,0.25); border-radius:8px; padding:12px; margin-bottom:14px;">
                <div style="font-family:'Outfit'; font-size:12px; font-weight:700; color:#A5B4FC; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.4px;">Connection to Your Proposed Research</div>
                <div style="font-size:12.5px; color:#E2E8F0; margin-bottom:8px; line-height:1.5;">{connection_info.get('connection_summary', '')}</div>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:11.5px; color:#94A3B8;">
                    <div><b>Shared Problem:</b> {connection_info.get('shared_problem', '')}</div>
                    <div><b>Shared Technique:</b> {connection_info.get('shared_technique', '')}</div>
                    <div style="grid-column:1 / -1; color:#38BDF8;"><b>Key Differentiator:</b> {connection_info.get('key_difference', '')}</div>
                </div>
            </div>

            <div style="font-family:'Outfit'; font-size:13.5px; font-weight:700; color:#F8FAFC; margin-bottom:8px; text-transform:uppercase; letter-spacing:0.4px;">Identified Literature Gaps & Limitations</div>
            {gaps_html}
        </div>

        <div style="margin-top:14px;">
            <h3 style="font-family:'Outfit'; font-size:15px; color:#F8FAFC; margin-bottom:10px; text-transform:uppercase; letter-spacing:0.4px;">Peer-Reviewed Papers in this Cluster ({len(papers)})</h3>
            {papers_html}
        </div>
    </div>
    """
