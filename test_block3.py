"""
Test Suite for Block 3: Embeddings & Research Graph Engine
"""
from academic_retrieval import Paper
from embeddings_graph import graph_engine, SimilarityEngine

def run_tests():
    print("=" * 60)
    print("Testing Block 3: Embeddings & Research Graph Engine")
    print("=" * 60)

    sim = SimilarityEngine()
    
    # 1. Test Cosine Similarity
    text_user = "Multimodal phishing detection with URL semantics and webpage screenshots"
    text_related = "Deep learning architecture for visual website screenshot phishing detection"
    text_unrelated = "Quantum chemistry simulation of molecular orbital transitions"

    sim_high = sim.compute_similarity(text_user, text_related)
    sim_low = sim.compute_similarity(text_user, text_unrelated)

    print(f"[1] Similarity User vs Related:   {sim_high:.2f}")
    print(f"[1] Similarity User vs Unrelated: {sim_low:.2f}")
    assert sim_high > sim_low, "Related text must have higher similarity score than unrelated text"

    # 2. Test Graph Construction
    sample_papers = [
        Paper(
            paper_id="p1",
            title="Screenshot-based Phishing Detection using Vision Transformers",
            authors=["J. Doe"],
            year=2024,
            abstract="We analyze website screenshots to identify brand impersonation.",
            citation_count=45
        ),
        Paper(
            paper_id="p2",
            title="URL Token Embedding for Malicious Domain Classification",
            authors=["A. Smith"],
            year=2023,
            abstract="Extracting lexical n-grams from URLs using fastText embeddings.",
            citation_count=120
        ),
        Paper(
            paper_id="p3",
            title="Multimodal Fusion of Text and Visual Artifacts for Security",
            authors=["C. Lee"],
            year=2025,
            abstract="Joint representations across image and text modalities.",
            citation_count=15
        )
    ]

    print(f"\n[2] Building NetworkX Graph for {len(sample_papers)} papers...")
    G, cluster_summaries = graph_engine.build_graph(text_user, sample_papers)
    
    print(f"Total Graph Nodes: {G.number_of_nodes()}")
    print(f"Total Graph Edges: {G.number_of_edges()}")
    print(f"Discovered Clusters: {list(cluster_summaries.keys())}")

    for c_name, c_info in cluster_summaries.items():
        print(f"  • Cluster '{c_name}': Similarity={c_info['similarity']:.2f}, Papers={c_info['paper_count']}")

    # 3. Test Vis-Network HTML Generation
    html_output = graph_engine.generate_vis_network_html(G)
    assert len(html_output) > 200, "HTML string must be populated"
    assert "vis.Network" in html_output, "HTML must contain vis.Network initialization"
    print("\n[3] Vis-Network HTML generated successfully!")

    print("\n" + "=" * 60)
    print("BLOCK 3 VERIFICATION PASSED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
