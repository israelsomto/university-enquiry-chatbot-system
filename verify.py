# -*- coding: utf-8 -*-
"""
Verification script for testing the NLP matcher.
Run: python verify.py
"""
import sys
from nlp_matcher import NLPQueryMatcher

def run_tests():
    print("Initializing NLPQueryMatcher...")
    matcher = NLPQueryMatcher()
    print("Initialization successful. Knowledge Base contains", len(matcher.knowledge_base), "articles.\n")
    
    test_cases = [
        {
            "query": "What are the requirements for computer science?",
            "expected_id": "adm_requirements_cs"
        },
        {
            "query": "tell me about the hostel cost",
            "expected_id": "faq_hostel_fee"
        },
        {
            "query": "when does the school resume classes?",
            "expected_id": "gen_semester_start"
        },
        {
            "query": "is there any dress code rule?",
            "expected_id": "pol_dress_code"
        },
        {
            "query": "how do I pay my school fees?",
            "expected_id": "fee_procedures"
        },
        {
            "query": "who can I call for help or problems?",
            "expected_id": "con_help_problem"
        }
    ]
    
    failed = 0
    for idx, tc in enumerate(test_cases):
        query = tc["query"]
        expected_id = tc["expected_id"]
        
        print(f"Test case {idx + 1}: Query = '{query}'")
        res = matcher.find_match(query)
        
        if res["type"] == "exact_match":
            matched_id = res["data"]["id"]
            question = res["data"]["question"]
            score = res["score"]
            
            if matched_id == expected_id:
                print(f"  ✅ PASS: Matched expected '{matched_id}' with score {score:.2f} ('{question}')")
            else:
                print(f"  ❌ FAIL: Expected '{expected_id}' but got '{matched_id}' with score {score:.2f} ('{question}')")
                failed += 1
        else:
            print(f"  ❌ FAIL: Expected exact match but got response type '{res['type']}'")
            failed += 1
        print()
        
    if failed == 0:
        print("🎉 ALL TESTS PASSED SUCCESSFULLY! The NLP matcher is working beautifully.")
        sys.exit(0)
    else:
        print(f"💥 {failed} TESTS FAILED. Please review similarity matching thresholds or synonyms.")
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
