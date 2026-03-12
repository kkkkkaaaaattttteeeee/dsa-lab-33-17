from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/number/', methods=['GET'])
def get_number():
    """GET эндпоинт с параметром запроса param"""
    param = float(request.args.get('param', 1))
    random_num = random.randint(1, 100)
    result = random_num * param
    
    return jsonify({
        'number': result,
        'operation': random.choice(['sum', 'sub', 'mul', 'div'])
    })

@app.route('/number/', methods=['POST'])
def post_number():
    """POST эндпоинт с JSON телом"""
    data = request.get_json()
    json_param = float(data['jsonParam'])
    random_num = random.randint(1, 100)
    result = random_num * json_param
    
    return jsonify({
        'number': result,
        'operation': random.choice(['sum', 'sub', 'mul', 'div'])
    })

@app.route('/number/', methods=['DELETE'])
def delete_number():
    """DELETE эндпоинт"""
    return jsonify({
        'number': random.randint(1, 100),
        'operation': random.choice(['sum', 'sub', 'mul', 'div'])
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)