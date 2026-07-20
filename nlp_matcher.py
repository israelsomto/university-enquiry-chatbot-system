# -*- coding: utf-8 -*-
import re
import math
from knowledge import KNOWLEDGE_BASE, CATEGORIES, SYNONYMS, STOPWORDS

class NLPQueryMatcher:
    def __init__(self):
        self.knowledge_base = KNOWLEDGE_BASE
        self.categories = CATEGORIES
        self.synonyms = SYNONYMS
        self.stopwords = STOPWORDS
        
        # Precompute vocabulary and document frequencies for questions
        self.vocab = set()
        self.doc_frequencies = {}
        self.idf = {}
        self.doc_vectors = []  # List of (qa_id, tf-idf_vector_dict, magnitude)
        
        self._initialize_tfidf()

    def _normalize_text(self, text):
        """Clean, tokenize, remove stopwords, and apply synonym mapping."""
        if not text:
            return []
        
        # Lowercase and strip non-alphanumeric characters
        text = text.lower().strip()
        text = re.sub(r'[^\w\s]', ' ', text)
        
        # Tokenize by whitespace
        tokens = text.split()
        
        normalized_tokens = []
        for token in tokens:
            if token in self.stopwords:
                continue
            
            # Map synonym if available
            mapped_token = self.synonyms.get(token, token)
            normalized_tokens.append(mapped_token)
            
        return normalized_tokens

    def _initialize_tfidf(self):
        """Prepare vocabulary, calculate IDF, and pre-vectorize knowledge base questions."""
        # Clean and tokenize all questions in the knowledge base
        cleaned_docs = []
        for idx, qa in enumerate(self.knowledge_base):
            # Combine question and keywords for a richer document representation
            doc_text = qa["question"] + " " + " ".join(qa.get("keywords", []))
            tokens = self._normalize_text(doc_text)
            cleaned_docs.append((qa["id"], tokens))
            
            # Record vocabulary and update document frequencies
            unique_tokens = set(tokens)
            for token in unique_tokens:
                self.vocab.add(token)
                self.doc_frequencies[token] = self.doc_frequencies.get(token, 0) + 1
        
        # Calculate IDF for each word in vocabulary
        # Formula: idf = ln(1 + N / (1 + df))
        num_docs = len(self.knowledge_base)
        for word in self.vocab:
            df = self.doc_frequencies.get(word, 0)
            self.idf[word] = math.log(1 + (num_docs / (1 + df)))
            
        # Build TF-IDF vectors for each document
        for qa_id, tokens in cleaned_docs:
            if not tokens:
                self.doc_vectors.append((qa_id, {}, 0.0))
                continue
                
            # Compute TF (term frequency)
            tf_vector = {}
            for token in tokens:
                tf_vector[token] = tf_vector.get(token, 0) + 1
                
            # Compute TF-IDF
            tfidf_vector = {}
            sum_squares = 0.0
            for token, tf in tf_vector.items():
                tfidf_val = tf * self.idf.get(token, 0.0)
                tfidf_vector[token] = tfidf_val
                sum_squares += tfidf_val ** 2
                
            magnitude = math.sqrt(sum_squares)
            self.doc_vectors.append((qa_id, tfidf_vector, magnitude))

    def _cosine_similarity(self, vec1, vec2, mag1, mag2):
        """Calculate cosine similarity between two sparse vectors."""
        if mag1 == 0.0 or mag2 == 0.0:
            return 0.0
            
        dot_product = 0.0
        # Iterate over smaller vector to speed up
        small_vec = vec1 if len(vec1) < len(vec2) else vec2
        large_vec = vec2 if len(vec1) < len(vec2) else vec1
        
        for key, val in small_vec.items():
            if key in large_vec:
                dot_product += val * large_vec[key]
                
        return dot_product / (mag1 * mag2)

    def find_match(self, user_query):
        """Find the best matching question in the knowledge base."""
        # 1. Check for exact category index number selection (1-6)
        cleaned_query = user_query.strip()
        if cleaned_query in ['1', '2', '3', '4', '5', '6']:
            category_keys = ['admissions', 'general_info', 'student_faqs', 'fees_payments', 'policies', 'contact']
            cat_key = category_keys[int(cleaned_query) - 1]
            return {
                "type": "category_selected",
                "category": cat_key,
                "category_info": self.categories[cat_key],
                "questions": [qa["question"] for qa in self.knowledge_base if qa["category"] == cat_key]
            }

        # 2. Normalize user query
        query_tokens = self._normalize_text(user_query)
        if not query_tokens:
            return {
                "type": "no_match",
                "reason": "empty_query"
            }
            
        # 3. Calculate query TF-IDF vector
        query_tf = {}
        for token in query_tokens:
            query_tf[token] = query_tf.get(token, 0) + 1
            
        query_tfidf = {}
        sum_squares = 0.0
        for token, tf in query_tf.items():
            # If word is not in vocab, its IDF is 0 (ignored for similarity but keep structure)
            idf_val = self.idf.get(token, 0.0)
            if idf_val > 0.0:
                tfidf_val = tf * idf_val
                query_tfidf[token] = tfidf_val
                sum_squares += tfidf_val ** 2
                
        query_magnitude = math.sqrt(sum_squares)
        
        # 4. Compare with all document vectors
        best_match_id = None
        highest_score = -1.0
        
        # Lowercase raw query for helper checks
        raw_query_lower = user_query.lower()
        
        for qa_id, doc_vector, doc_magnitude in self.doc_vectors:
            similarity = self._cosine_similarity(query_tfidf, doc_vector, query_magnitude, doc_magnitude)
            
            # Find the corresponding Q&A item
            qa_item = next(item for item in self.knowledge_base if item["id"] == qa_id)
            
            # NLP Boosting Rules:
            boost = 0.0
            
            # Rule A: Exact keyword boost (+0.15 for each custom keyword matched in query)
            for kw in qa_item.get("keywords", []):
                if kw in raw_query_lower:
                    boost += 0.15
                    
            # Rule B: Exact question title string contains part of query (+0.10)
            clean_question = re.sub(r'[^\w\s]', '', qa_item["question"].lower())
            clean_query_str = re.sub(r'[^\w\s]', '', raw_query_lower)
            if clean_query_str in clean_question or clean_question in clean_query_str:
                boost += 0.10
                
            # Rule C: Specific token overlap bonus (Jaccard-like score boost)
            doc_tokens = set(self._normalize_text(qa_item["question"]))
            matched_tokens = set(query_tokens).intersection(doc_tokens)
            if len(doc_tokens) > 0:
                jaccard_overlap = len(matched_tokens) / len(doc_tokens)
                boost += jaccard_overlap * 0.15
                
            final_score = similarity + boost
            
            if final_score > highest_score:
                highest_score = final_score
                best_match_id = qa_id
                
        # 5. Return high confidence match (threshold = 0.35)
        # Note: final_score can exceed 1.0 due to boosting, which is fine
        if highest_score >= 0.35 and best_match_id:
            matched_qa = next(item for item in self.knowledge_base if item["id"] == best_match_id)
            return {
                "type": "exact_match",
                "score": highest_score,
                "data": matched_qa
            }
            
        # 6. Fallback: Category-level keyword matching
        # If similarity was low, check if any category keys or category keywords exist in raw query
        for cat_key, cat_data in self.categories.items():
            # Check if category name matches
            if cat_data["name"].lower() in raw_query_lower or cat_key.replace('_', ' ') in raw_query_lower:
                return {
                    "type": "category_selected",
                    "category": cat_key,
                    "category_info": cat_data,
                    "questions": [qa["question"] for qa in self.knowledge_base if qa["category"] == cat_key]
                }
                
            # Check custom category keywords (like "admission" for admissions, "money" or "school fees" for fees)
            cat_kws = {
                "admissions": ["admission", "apply", "application", "enroll", "qualification", "deadline"],
                "general_info": ["location", "address", "map", "faculty", "faculties", "department", "departments", "calendar", "resumption"],
                "student_faqs": ["hostel", "accommodation", "dorm", "registration", "defer", "timetable", "result", "results"],
                "fees_payments": ["fee", "fees", "tuition", "payment", "bank", "pay", "cost", "price", "installment"],
                "policies": ["policy", "policies", "rule", "rules", "attendance", "dress", "clothing", "cheating", "conduct", "malpractice"],
                "contact": ["contact", "phone", "email", "support", "help", "problem", "complain", "call", "office"]
            }
            
            for kw in cat_kws.get(cat_key, []):
                if kw in raw_query_lower:
                    return {
                        "type": "category_selected",
                        "category": cat_key,
                        "category_info": cat_data,
                        "questions": [qa["question"] for qa in self.knowledge_base if qa["category"] == cat_key]
                    }
                    
        # 7. No match at all
        return {
            "type": "no_match",
            "reason": "low_confidence",
            "score": highest_score
        }

if __name__ == "__main__":
    # Quick CLI test
    matcher = NLPQueryMatcher()
    
    test_queries = [
        "requirements for computer science",
        "how do i apply for hostel?",
        "what is tuition fee for nursing",
        "where is the campus?",
        "tell me about exam rules",
        "something random that will not match"
    ]
    
    for q in test_queries:
        res = matcher.find_match(q)
        print(f"Query: '{q}'")
        print(f"Match Type: {res['type']}")
        if res['type'] == 'exact_match':
            print(f"Question: {res['data']['question']} (Score: {res['score']:.2f})")
        elif res['type'] == 'category_selected':
            print(f"Category: {res['category']} ({len(res['questions'])} questions)")
        print("-" * 50)
