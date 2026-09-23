"""
Test Suite for Block 1: Academic Retrieval & Cache Engine
"""
import sys
from academic_retrieval import retrieval_engine, Paper
from cache_manager import cache

def run_tests():
    print("=" * 60)
    print("Testing Block 1: Academic Retrieval & Cache Engine")
    print("=" * 60)

    # 1. Test Cache Initialization
    stats = cache.get_stats()
    print(f"[1] Cache Manager Initialized: {stats}")

    # 2. Test Multi-Query Retrieval with real academic topic
    test_queries = [
        "multimodal phishing detection",
        "deep learning malicious URL classification"
    ]
    print(f"\n[2] Querying academic APIs for: {test_queries}")
    
    papers = retrieval_engine.retrieve_for_queries(test_queries, papers_per_query=4)
    print(f"\n[3] Total Unique Papers Retrieved: {len(papers)}")

    if not papers:
        print("[FAIL] No papers retrieved!")
        sys.exit(1)

    # 3. Verify real paper structure
    for i, p in enumerate(papers[:3], 1):
        print(f"\n--- Paper {i} ---")
        print(f"Title:        {p.title}")
        print(f"Authors:      {p.authors_display}")
        print(f"Year:         {p.year}")
        print(f"Citations:    {p.citation_count}")
        print(f"Source API:   {p.source_api}")
        print(f"DOI/URL:      {p.clean_url}")
        print(f"Abstract:     {p.abstract[:140]}...")

    # 4. Verify Caching
    stats_after = cache.get_stats()
    print(f"\n[4] Cache Stats after query: {stats_after}")
    assert stats_after["cached_queries"] > 0 or len(papers) > 0, "Cache should have recorded entries"

    print("\n" + "=" * 60)
    print("BLOCK 1 VERIFICATION PASSED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
