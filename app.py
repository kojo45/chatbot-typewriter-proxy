from flask import Flask, request, jsonify
import json
import difflib

app = Flask(__name__)

with open('corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

def find_best_answer(user_question):
    questions = [item['q'] for item in corpus['questions']]
    matches = difflib.get_close_matches(user_question.lower(), [q.lower() for q in questions], n=1, cutoff=0.5)
    if matches:
        idx = [q.lower() for q in questions].index(matches[0])
        return corpus['questions'][idx]['a']
    return None

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_question = data.get('question', '')
    answer = find_best_answer(user_question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)