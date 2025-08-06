from flask import Flask, request, jsonify
from flask_cors import CORS
from tikz_generator import generate_tikz_code

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    description = data.get('description', '')
    tikz_code = generate_tikz_code(description)
    return jsonify({'tikz_code': tikz_code})

if __name__ == '__main__':
    app.run(debug=True)
