"""
Test Suite for Block 2: AI Interpretation & Query Engine
"""
from llm_engine import llm_engine, IdeaStructure
from academic_retrieval import Paper

def run_tests():
    print("=" * 60)
    print("Testing Block 2: AI Interpretation & Query Engine")
    print("=" * 60)

    # 1. Test Detailed Research Idea
    sample_idea = (
        "I want to make an AI system that can detect fake websites and phishing attacks "
        "using URL information and maybe screenshots. I don't know exactly what approach to use."
    )
    print(f"\n[1] Interpreting raw research idea:\n\"{sample_idea}\"")
    structured = llm_engine.interpret_idea(sample_idea)
    
    print("\n--- Structured Extraction Result ---")
    print(f"Domain:             {structured.domain}")
    print(f"Primary Problem:    {structured.primary_problem}")
    print(f"Input Modalities:   {structured.input_modalities}")
    print(f"AI Subfields:       {structured.ai_subfields}")
    print(f"Academic Queries:   {structured.academic_search_queries}")
    print(f"Specificity:        {structured.specificity_level}")

    assert len(structured.academic_search_queries) > 0, "Should generate academic search queries"

    # 2. Test Vague Input Detection
    vague_idea = "AI in cybersecurity"
    print(f"\n[2] Testing vague idea detection for: \"{vague_idea}\"")
    vague_res = llm_engine.interpret_idea(vague_idea)
    print(f"Specificity Level:   {vague_res.specificity_level}")
    print(f"Clarifying Question: {vague_res.clarifying_question}")

    # 3. Test Literature Gaps & Badging
    test_papers = [
        Paper(
            paper_id="test1",
            title="Adversarial Phishing Detection",
            authors=["A. Smith", "B. Doe"],
            year=2023,
            abstract="Traditional classifiers suffer from high false positive rates when faced with obfuscated JavaScript.",
            source_api="Semantic Scholar"
        )
    ]
    print("\n[3] Testing Literature Gap Extraction & Evidence Badging:")
    gaps = llm_engine.extract_literature_gaps(test_papers, "Multimodal Phishing Detection")
    for g in gaps:
        print(f"  • [{g['type']}] {g['text'][:100]}... (Source: {g['source']})")

    print("\n" + "=" * 60)
    print("BLOCK 2 VERIFICATION PASSED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
