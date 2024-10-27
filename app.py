from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    question = data.get('question')
    reponse = data.get('reponse')

    # Écrire dans le fichier .txt
    with open('data.txt', 'a') as f:
        f.write(f"{question}\t{reponse}\n")

    return jsonify({'status': 'success'}), 200

@app.route('/convert', methods=['GET'])
def convert_to_json():
    entries = []
    with open('data.txt', 'r') as f:
        for line in f:
            question, reponse = line.strip().split('\t')
            entries.append({'question': question, 'reponse': reponse})

    with open('data.json', 'w') as json_file:
        json.dump({'entries': entries}, json_file, ensure_ascii=False, indent=2)

    return jsonify({'status': 'converted to JSON'}), 200

if __name__ == '__main__':
    app.run(debug=True)
