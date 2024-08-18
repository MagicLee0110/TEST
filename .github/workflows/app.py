from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "This is a sample API response"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
