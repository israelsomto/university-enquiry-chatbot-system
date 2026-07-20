# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
import os
from nlp_matcher import NLPQueryMatcher

app = Flask(__name__)

# Initialize the custom NLP matcher
matcher = NLPQueryMatcher()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'type': 'no_match',
                'response': 'Please ask a question.',
                'follow_ups': []
            })
            
        # Match using NLP Matcher
        match_res = matcher.find_match(user_message)
        
        if match_res['type'] == 'exact_match':
            qa_data = match_res['data']
            return jsonify({
                'type': 'exact_match',
                'response': qa_data['answer'],
                'follow_ups': qa_data.get('follow_ups', []),
                'category': qa_data['category'],
                'question': qa_data['question']
            })
            
        elif match_res['type'] == 'category_selected':
            cat_key = match_res['category']
            cat_info = match_res['category_info']
            questions = match_res['questions']
            
            response_text = f"<b>{cat_info['icon']} {cat_info['name']}</b><br>{cat_info['description']}<br><br>Here are some common topics in this category. Click on any of them to learn more:"
            
            return jsonify({
                'type': 'category_selected',
                'response': response_text,
                'follow_ups': questions,
                'category': cat_key
            })
            
            # Fallback/No match response
            response_text = (
                '<b><i data-lucide="graduation-cap" class="cat-title-icon"></i> Academic Assistant</b><br><br>'
                "I couldn't find a direct match for your question in my database. "
                "Try asking in a different way, or select one of the core categories below:"
            )
            category_options = [
                '<i data-lucide="file-text"></i> Admissions',
                '<i data-lucide="landmark"></i> General Info',
                '<i data-lucide="help-circle"></i> Student FAQs',
                '<i data-lucide="credit-card"></i> Fees & Payments',
                '<i data-lucide="scroll"></i> Policies',
                '<i data-lucide="phone"></i> Contact & Help'
            ]
            return jsonify({
                'type': 'no_match',
                'response': response_text,
                'follow_ups': category_options
            })
            
    except Exception as e:
        print(f"Error in /chat: {e}")
        return jsonify({
            'type': 'error',
            'response': 'Sorry, an error occurred. Please try again.',
            'follow_ups': []
        })

if __name__ == '__main__':
    # Render and Railway pass the port dynamically via environmental variables
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)