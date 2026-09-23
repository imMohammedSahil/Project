"""
Test Suite for Block 6: Gradio Interactive UI Dashboard & End-to-End Pipeline
"""
import os
from app import analyze_and_explore_research, inspect_cluster_node, generate_scope_proposal, build_app

def run_tests():
    print("=" * 60)
    print("Testing Block 6: Full End-to-End Pipeline & UI Construction")
    print("=" * 60)

    # 1. Test UI Construction
    print("[1] Building Gradio App...")
    demo = build_app()
    assert demo is not None, "Gradio Blocks demo must be constructed"
    print("Gradio App built successfully!")

    # 2. Test End-to-End Analysis Pipeline
    test_idea = "I want to make an AI system that can detect fake websites and phishing attacks using URL information and maybe screenshots."
    print(f"\n[2] Running End-to-End Pipeline on:\n\"{test_idea}\"")
    
    (
        dashboard_visibility_update,
        concept_html,
        fig_graph,
        cluster_dropdown_update,
        initial_deep_dive,
        fig_matrix,
        fig_timeline,
        session_state,
        papers,
        metrics_list
    ) = analyze_and_explore_research(test_idea, "")

    print(f"Total Papers Retrieved: {len(papers)}")
    print(f"Discovered Clusters: {list(session_state.get('cluster_summaries', {}).keys())}")
    assert len(papers) > 0, "Papers must be retrieved"
    assert fig_graph is not None, "Plotly graph must be generated"
    assert fig_matrix is not None, "Matrix plot must be generated"

    # 3. Test Cluster Inspection
    clusters = list(session_state.get('cluster_summaries', {}).keys())
    if clusters:
        chosen_cluster = clusters[0]
        print(f"\n[3] Testing Deep-Dive on Cluster: '{chosen_cluster}'")
        deep_dive_html = inspect_cluster_node(chosen_cluster, session_state, papers)
        assert len(deep_dive_html) > 100, "Deep-dive HTML must be populated"
        print("Deep-Dive Card rendered successfully!")

        # 4. Test Scope Proposal Generation
        print(f"\n[4] Generating Scope Proposal for: '{chosen_cluster}'")
        md_text, md_path, json_path = generate_scope_proposal(chosen_cluster, session_state, papers)
        assert os.path.exists(md_path), "Markdown export file must exist"
        assert os.path.exists(json_path), "JSON export file must exist"
        print(f"Scope Proposal successfully created: {md_path}")

    print("\n" + "=" * 60)
    print("BLOCK 6 VERIFICATION PASSED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
