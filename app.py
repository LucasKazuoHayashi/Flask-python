from flask import Flask, jsonify, request
from imc.controllers.ImcController import ImcController

app = Flask(__name__)

@app.route('/imc/calculate', methods=['POST'])
def calculateImc():
    data = request.get_json()
    height = data['height']
    weight = data['weight']

    imc_controller = ImcController()
    result = imc_controller.calculate_imc(height, weight)

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)