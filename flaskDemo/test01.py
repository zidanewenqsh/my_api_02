from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'
@app.route('/a')
def helloa():
    return 'Hello World a!'
@app.route('/b')
def hellob():
    b = request.args.get("name")
    print(b)
    return 'Hello World b!'
# @app.route('/predict', methods=['POST'])
# def predict():
#     return 'Hello World!'

@app.route('/predict', methods=['POST'])
def predict():
    return jsonify({'class_id': 'IMAGE_NET_XXX', 'class_name': 'Cat'})
if __name__ == '__main__':
    app.run()