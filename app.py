"""
Research Scope AI - Main Gradio Application
AI-Based Research Scope Generator & Research Landscape Explorer
True Two-Stage Stepped Interface:
Stage 1: Hero Hypothesis Command Studio (Initial View)
Stage 2: Tabbed Intelligence Dashboard (Revealed upon clicking 'EXPLORE RESEARCH LANDSCAPE')
"""
import os
import json
import gradio as gr
import pandas as pd

from config import SAMPLE_IDEAS, GROQ_API_KEY
from cache_manager import cache
from academic_retrieval import retrieval_engine, Paper
from llm_engine import llm_engine, IdeaStructure
from embeddings_graph import graph_engine
from saturation_engine import saturation_engine, SaturationMetrics
from scope_generator import scope_generator, ResearchScope
from export_utils import export_manager
from ui_components import (
    CUSTOM_CSS,
    render_hero_header,
    render_concept_breakdown,
    render_node_deep_dive
)

# ---------------------------------------------------------------------------
# Core Workflow Controllers
# ---------------------------------------------------------------------------

def inspect_cluster_node(selected_cluster: str, session_state: dict, all_papers_list: list):
    """Deep-dives into a specific research direction node."""
    if not selected_cluster or not all_papers_list:
        return "<div style='color:#94A3B8; padding:16px; font-size:13px;'>Select a research direction from the dropdown above to view connection analysis and anchor papers.</div>"

    user_idea = session_state.get("user_idea", "")
    cluster_papers = [p for p in all_papers_list if getattr(p, "cluster_label", "") == selected_cluster or selected_cluster in p.fields_of_study]
    if not cluster_papers:
        cluster_papers = all_papers_list[:4]

    # Connection analysis
    connection_info = llm_engine.analyze_node_connection(user_idea, selected_cluster, cluster_papers)

    # Extract literature gaps with [From Paper] vs [AI-Inferred] badging
    gaps = llm_engine.extract_literature_gaps(cluster_papers, selected_cluster)

    deep_dive_html = render_node_deep_dive(selected_cluster, connection_info, gaps, cluster_papers)
    return deep_dive_html

def analyze_and_explore_research(user_idea: str):
    """Primary pipeline: AI Interpretation -> Academic Search -> Graph & Saturation."""
    full_text = user_idea.strip()

    if not full_text:
        return (
            gr.update(visible=False),
            "<div style='color:#F87171; padding:12px;'>Please enter a research idea or select a preset to begin.</div>",
            None,
            gr.update(choices=[]),
            "<div style='color:#94A3B8; padding:12px;'>No active literature direction selected.</div>",
            None,
            None,
            {},
            [],
            []
        )

    # 1. AI Interpretation
    idea_struct = llm_engine.interpret_idea(full_text)
    concept_html = render_concept_breakdown(idea_struct)

    # 2. Academic Retrieval
    papers = retrieval_engine.retrieve_for_queries(idea_struct.academic_search_queries, papers_per_query=5)

    # 3. Graph Construction & Plotly Force-Directed Network
    G, cluster_summaries = graph_engine.build_graph(full_text, papers)
    fig_graph = graph_engine.generate_plotly_network_figure(G)

    # 4. Saturation Metrics & Charts
    metrics_list = []
    for c_name, c_info in cluster_summaries.items():
        m = saturation_engine.compute_cluster_saturation(c_name, c_info["papers"], c_info["similarity"])
        metrics_list.append(m)

    fig_matrix = saturation_engine.generate_saturation_matrix_plot(metrics_list)
    fig_timeline = saturation_engine.generate_timeline_plot(metrics_list)

    cluster_names = list(cluster_summaries.keys())
    first_choice = cluster_names[0] if cluster_names else ""

    session_state = {
        "user_idea": full_text,
        "idea_struct": idea_struct.to_dict(),
        "cluster_summaries": {k: {"similarity": v["similarity"], "paper_count": v["paper_count"]} for k, v in cluster_summaries.items()},
        "papers": [p.to_dict() for p in papers]
    }

    # Initial deep-dive for the primary cluster
    initial_deep_dive = inspect_cluster_node(first_choice, session_state, papers) if first_choice else ""

    return (
        gr.update(visible=True),  # Reveal Stage 2 Dashboard
        concept_html,
        fig_graph,
        gr.update(choices=cluster_names, value=first_choice),
        initial_deep_dive,
        fig_matrix,
        fig_timeline,
        session_state,
        papers,
        metrics_list
    )

def generate_scope_proposal(selected_cluster: str, session_state: dict, all_papers_list: list):
    """Generates formal research scope proposal."""
    if not selected_cluster or not all_papers_list:
        return "### Notice\nPlease run 'EXPLORE RESEARCH LANDSCAPE' first to generate scope proposals.", None, None

    user_idea = session_state.get("user_idea", "")
    cluster_papers = [p for p in all_papers_list if getattr(p, "cluster_label", "") == selected_cluster or selected_cluster in p.fields_of_study]
    if not cluster_papers:
        cluster_papers = all_papers_list[:4]

    gaps = llm_engine.extract_literature_gaps(cluster_papers, selected_cluster)
    scope = scope_generator.generate_scope(user_idea, selected_cluster, cluster_papers, gaps)

    # Export files
    md_path = export_manager.export_scope_markdown(scope)
    json_path = export_manager.export_scope_json(scope)

    md_content = scope.to_markdown()
    return md_content, md_path, json_path

def update_groq_key(api_key: str):
    if not api_key or len(api_key.strip()) < 10:
        return "Please enter a valid Groq API Key."
    llm_engine.update_api_key(api_key.strip())
    return "Groq API Key successfully updated and online."

def clear_system_cache():
    cache.clear()
    stats = cache.get_stats()
    return f"Cache cleared. Active cached entries: {stats['cached_queries']} queries, {stats['cached_papers']} papers."

# ---------------------------------------------------------------------------
# Gradio UI Layout (Blocks API)
# ---------------------------------------------------------------------------

def build_app():
    with gr.Blocks(title="Research Scope AI - Academic Landscape & Scope Synthesizer", css=CUSTOM_CSS) as demo:
        # State stores
        session_state = gr.State({})
        all_papers_state = gr.State([])
        metrics_state = gr.State([])

        # Header Hero
        gr.HTML(render_hero_header())

        # ===================================================================
        # STAGE 1: HERO RESEARCH HYPOTHESIS COMMAND STUDIO
        # ===================================================================
        with gr.Group():
            gr.Markdown("<div style='font-size:14px; font-weight:800; color:#F8FAFC; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:6px;'>Describe Your Research Idea or Hypothesis</div>")
            idea_input = gr.Textbox(
                label="Describe Your Proposed Research Area",
                placeholder="e.g. I want to make an AI system that can detect fake websites and phishing attacks using URL lexical semantics, HTML structural elements, and webpage screenshots with explainable attention maps.",
                lines=5,
                value=SAMPLE_IDEAS[0]["description"],
                show_label=False
            )

            explore_btn = gr.Button("EXPLORE RESEARCH LANDSCAPE", variant="primary", elem_classes=["primary-btn"], size="lg")

        # ===================================================================
        # STAGE 2: TABBED INTELLIGENCE DASHBOARD (REVEALED ON EXPLORE)
        # ===================================================================
        with gr.Column(visible=False) as dashboard_section:
            gr.HTML("<hr style='border:0; border-top:1px solid rgba(255,255,255,0.08); margin:24px 0;'>")

            with gr.Tabs() as main_tabs:
                # -----------------------------------------------------------
                # TAB 1: SEMANTIC DECOMPOSITION & KNOWLEDGE GRAPH
                # -----------------------------------------------------------
                with gr.TabItem("Semantic Decomposition & Knowledge Graph", id="tab_graph"):
                    with gr.Row(equal_height=False):
                        with gr.Column(scale=6):
                            concept_output = gr.HTML()

                        with gr.Column(scale=6):
                            graph_output = gr.Plot(label="Semantic Literature Knowledge Network")

                # -----------------------------------------------------------
                # TAB 2: DIRECTION DEEP-DIVE & PEER-REVIEWED LITERATURE
                # -----------------------------------------------------------
                with gr.TabItem("Direction Deep-Dive & Peer-Reviewed Literature", id="tab_deepdive"):
                    with gr.Row():
                        with gr.Column(scale=4):
                            cluster_selector = gr.Dropdown(
                                label="Select Research Direction Cluster",
                                choices=[],
                                interactive=True
                            )
                            inspect_btn = gr.Button("Inspect Direction", variant="secondary")
                            gr.Markdown(
                                """
                                <div style='background:rgba(15,23,42,0.6); padding:14px; border-radius:8px; border:1px solid rgba(255,255,255,0.08); margin-top:12px;'>
                                    <div style='font-size:11px; font-weight:700; color:#94A3B8; text-transform:uppercase; margin-bottom:6px;'>Evidence Badging Criteria:</div>
                                    <div style='margin-bottom:6px;'><span class='badge-tag badge-paper'>[PUBLISHED LITERATURE]</span> <span style='font-size:12px; color:#CBD5E1;'>Direct limitation extracted from published literature abstract.</span></div>
                                    <div><span class='badge-tag badge-inferred'>[AI-SYNTHESIZED]</span> <span style='font-size:12px; color:#CBD5E1;'>High-confidence gap extrapolated across retrieved corpus.</span></div>
                                </div>
                                """
                            )
                        with gr.Column(scale=8):
                            deep_dive_output = gr.HTML()

                # -----------------------------------------------------------
                # TAB 3: SATURATION MATRIX & TIMELINE
                # -----------------------------------------------------------
                with gr.TabItem("Saturation Matrix & Activity Timeline", id="tab_saturation"):
                    with gr.Row():
                        with gr.Column(scale=6):
                            matrix_plot = gr.Plot(label="Scope Potential vs Literature Saturation Index")
                        with gr.Column(scale=6):
                            timeline_plot = gr.Plot(label="Publication Activity Timeline (2019-2026)")

                # -----------------------------------------------------------
                # TAB 4: AUTONOMOUS RESEARCH SCOPE PROPOSAL
                # -----------------------------------------------------------
                with gr.TabItem("Autonomous Research Scope Proposal & Exports", id="tab_scope"):
                    with gr.Row():
                        with gr.Column(scale=4):
                            gr.Markdown("<div style='font-size:13px; font-weight:700; color:#F8FAFC; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:6px;'>Formulate Proposal Scope</div>")
                            gr.Markdown("<span style='font-size:12.5px; color:#94A3B8; line-height:1.5;'>Synthesizes identified literature gaps, domain methodologies, and target novelty into a publication-grade research proposal with milestone roadmap.</span>")
                            generate_scope_btn = gr.Button("SYNTHESIZE FORMAL RESEARCH SCOPE", variant="primary", elem_classes=["primary-btn"], size="lg")
                            
                            gr.Markdown("<div style='font-size:12px; font-weight:700; color:#94A3B8; text-transform:uppercase; letter-spacing:0.4px; margin-top:16px;'>Export Proposal Assets</div>")
                            md_download = gr.File(label="Download Formatted Markdown (.md)")
                            json_download = gr.File(label="Download Structured JSON (.json)")

                        with gr.Column(scale=8):
                            gr.Markdown("<div style='font-size:13px; font-weight:700; color:#F8FAFC; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:6px;'>Executive Proposal Preview</div>")
                            scope_preview = gr.Markdown("```\nProposal preview will appear here upon clicking 'SYNTHESIZE FORMAL RESEARCH SCOPE'...\n```")

                # -----------------------------------------------------------
                # TAB 5: SYSTEM CONFIGURATION & CACHE
                # -----------------------------------------------------------
                with gr.TabItem("System Settings & Cache", id="tab_settings"):
                    with gr.Row():
                        with gr.Column(scale=6):
                            groq_key_input = gr.Textbox(
                                label="Groq API Key (Optional Override)",
                                type="password",
                                placeholder="gsk_...",
                                value=GROQ_API_KEY
                            )
                            save_key_btn = gr.Button("Update API Key", variant="secondary")
                            key_status = gr.Markdown("")
                        with gr.Column(scale=6):
                            gr.Markdown("**System Cache Status**<br><span style='font-size:12px; color:#94A3B8;'>Caches academic query responses and paper metadata locally in SQLite to ensure high speed and zero redundant API calls.</span>")
                            clear_cache_btn = gr.Button("Clear Cache Database", variant="secondary")
                            cache_status = gr.Markdown("")

        # -------------------------------------------------------------------
        # Event Wire-ups
        # -------------------------------------------------------------------
        explore_btn.click(
            fn=analyze_and_explore_research,
            inputs=[idea_input],
            outputs=[
                dashboard_section,
                concept_output,
                graph_output,
                cluster_selector,
                deep_dive_output,
                matrix_plot,
                timeline_plot,
                session_state,
                all_papers_state,
                metrics_state
            ]
        )

        inspect_btn.click(
            fn=inspect_cluster_node,
            inputs=[cluster_selector, session_state, all_papers_state],
            outputs=[deep_dive_output]
        )

        cluster_selector.change(
            fn=inspect_cluster_node,
            inputs=[cluster_selector, session_state, all_papers_state],
            outputs=[deep_dive_output]
        )

        generate_scope_btn.click(
            fn=generate_scope_proposal,
            inputs=[cluster_selector, session_state, all_papers_state],
            outputs=[scope_preview, md_download, json_download]
        )

        save_key_btn.click(
            fn=update_groq_key,
            inputs=[groq_key_input],
            outputs=[key_status]
        )

        clear_cache_btn.click(
            fn=clear_system_cache,
            inputs=[],
            outputs=[cache_status]
        )

    return demo

demo = build_app()

if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False,
        footer_links=[],
    )
