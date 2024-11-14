from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message='hello')

@app.route('/exp', methods=['POST'])
def create_expense():
    pass

@app.route('/exp', methods=['GET'])
def get_expenses():
    pass

@app.route('/exp/<int:id>', methods=['GET'])
def get_expense(id):
    pass

@app.route('/exp/<int:id>', methods=['PATCH'])   
def update_expense(id):
    pass

@app.route('/exp/<int:id>', methods=['DELETE'])
def delete_expense(id):
    pass

if __name__ == '__main__':
    app.run(debug=True)

