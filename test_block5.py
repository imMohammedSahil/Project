"""
Test Suite for Block 5: Research Scope Generator & Report Exporter
"""
import os
from academic_retrieval import Paper
from scope_generator import scope_generator
from export_utils import export_manager

def run_tests():
    print("=" * 60)
    print("Testing Block 5: Research Scope Generator & Exporter")
    print("=" * 60)

    user_idea = "Multimodal phishing detection combining URL lexical tokens and screenshot visual layouts."
    cluster_name = "Multimodal Fusion Architectures"
    sample_papers = [
        Paper("p1", "Cross-Modal Webpage Transformer", ["A. Author"], 2024, "Abstract...", 45),
        Paper("p2", "Visual Phishing Detection", ["B. Author"], 2023, "Abstract...", 90),
    ]
    gaps = [
        {"type": "From Paper", "text": "High inference latency in heavy vision backbones.", "source": "A. Author (2024)"},
        {"type": "AI-Inferred", "text": "Vulnerable to zero-day adversarial perturbations.", "source": "Literature Synthesis"}
    ]

    print("\n[1] Generating Research Scope Proposal...")
    scope = scope_generator.generate_scope(user_idea, cluster_name, sample_papers, gaps)
    
    print("\n--- Scope Generation Output ---")
    print(f"Title:                 {scope.title}")
    print(f"Research Questions:    {len(scope.research_questions)} questions")
    for rq in scope.research_questions:
        print(f"  • {rq}")
    print(f"Research Objectives:   {len(scope.objectives)} objectives")
    print(f"Suggested Datasets:    {scope.suggested_datasets}")
    print(f"Evaluation Metrics:    {scope.evaluation_metrics}")

    # 2. Test Markdown Export
    print("\n[2] Exporting to Markdown...")
    md_path = export_manager.export_scope_markdown(scope, "test_scope_output.md")
    assert os.path.exists(md_path), "Markdown export file must exist"
    print(f"Markdown successfully exported to: {md_path}")

    # 3. Test JSON Export
    print("\n[3] Exporting to JSON...")
    json_path = export_manager.export_scope_json(scope, "test_scope_output.json")
    assert os.path.exists(json_path), "JSON export file must exist"
    print(f"JSON successfully exported to: {json_path}")

    print("\n" + "=" * 60)
    print("BLOCK 5 VERIFICATION PASSED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
