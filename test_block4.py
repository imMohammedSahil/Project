"""
Test Suite for Block 4: Saturation Engine & Visual Matrix
"""
from academic_retrieval import Paper
from saturation_engine import saturation_engine

def run_tests():
    print("=" * 60)
    print("Testing Block 4: Saturation Engine & Visual Matrix")
    print("=" * 60)

    # 1. Create simulated clusters with realistic metadata
    cluster_a_papers = [
        Paper("p1", "URL Phishing", ["A. Author"], 2021, "Abstract...", 280),
        Paper("p2", "Lexical URL Detection", ["B. Author"], 2022, "Abstract...", 190),
        Paper("p3", "Domain Classifier", ["C. Author"], 2020, "Abstract...", 310),
        Paper("p4", "URL Blacklist Analysis", ["D. Author"], 2019, "Abstract...", 450),
    ]

    cluster_b_papers = [
        Paper("p5", "Multimodal Agent for Phishing", ["E. Author"], 2025, "Abstract...", 18),
        Paper("p6", "Cross-Attention Webpage Vision", ["F. Author"], 2024, "Abstract...", 35),
    ]

    metrics_a = saturation_engine.compute_cluster_saturation("Lexical URL Detection", cluster_a_papers, 0.65)
    metrics_b = saturation_engine.compute_cluster_saturation("Multimodal Fusion", cluster_b_papers, 0.88)

    print(f"\n[1] Cluster A (URL Detection):")
    print(f"    Saturation Score: {metrics_a.saturation_score:.2f} ({metrics_a.saturation_level})")
    print(f"    Scope Potential:  {metrics_a.scope_potential:.2f}")
    print(f"    Rationale:        {metrics_a.saturation_rationale}")

    print(f"\n[2] Cluster B (Multimodal Fusion):")
    print(f"    Saturation Score: {metrics_b.saturation_score:.2f} ({metrics_b.saturation_level})")
    print(f"    Scope Potential:  {metrics_b.scope_potential:.2f}")
    print(f"    Rationale:        {metrics_b.saturation_rationale}")

    assert metrics_a.saturation_score > metrics_b.saturation_score, "Older heavily-cited cluster should have higher saturation"
    assert metrics_b.scope_potential >= metrics_a.scope_potential, "Multimodal high-similarity cluster should have high scope potential"

    # 2. Test Plotly 2D Matrix generation
    print("\n[3] Generating 2D Saturation Matrix Plot...")
    fig_matrix = saturation_engine.generate_saturation_matrix_plot([metrics_a, metrics_b])
    assert fig_matrix is not None, "Plotly matrix figure should be generated"

    # 3. Test Plotly Timeline generation
    print("[4] Generating Timeline Velocity Plot...")
    fig_timeline = saturation_engine.generate_timeline_plot([metrics_a, metrics_b])
    assert fig_timeline is not None, "Plotly timeline figure should be generated"

    print("\n" + "=" * 60)
    print("BLOCK 4 VERIFICATION PASSED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
