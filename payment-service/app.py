from flask import Flask, jsonify, request
app = Flask(__name__)

payments = []  # In-memory list
id_counter = 1
port = 8083

# GET /payments - Return all payments
@app.route('/payments', methods=['GET'])
def get_payments():
    return jsonify(payments)

# POST /payments/process - Process a payment (expects { "orderId": 1, "amount": 1299.99, "method": "CARD" })
@app.route('/payments/process', methods=['POST'])
def process_payment():
    global id_counter
    payment = request.json
    if not payment:
        return 'Missing body', 400
    payment['id'] = id_counter
    id_counter += 1
    payment['status'] = 'SUCCESS'
    payments.append(payment)
    return jsonify(payment), 201

# GET /payments/{id} - Get payment by ID
@app.route('/payments/<int:id>', methods=['GET'])
def get_payment(id):
    for p in payments:
        if p['id'] == id:
            return jsonify(p)
    return 'Payment not found', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)