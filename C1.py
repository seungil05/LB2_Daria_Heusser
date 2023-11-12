from functools import reduce
from flask import Flask, jsonify

app = Flask(__name__)


def calculate_c1g_result():
    data = [1, 2, 3, 4, 5]

    def multiply_numbers(x, y):
        return x * y

    result = reduce(multiply_numbers, data)

    return result


@app.route('/c1g', methods=['GET'])
def c1g_page():
    result = calculate_c1g_result()

    response = jsonify({'c1g_result': result})

    return response


def calculate_total_price_before_refactoring(quantity, price):
    subtotal = quantity * price
    if quantity > 100:
        subtotal *= 0.9
    return subtotal


def calculate_subtotal(quantity, price):
    subtotal = quantity * price
    if quantity > 100:
        subtotal *= 0.9
    return subtotal


def calculate_invoice_total(items):
    return sum(calculate_subtotal(item['quantity'], item['price']) for item in items)


items = [
    {'quantity': 50, 'price': 10},
    {'quantity': 120, 'price': 8},
    {'quantity': 75, 'price': 12}
]


@app.route('/c1f', methods=['GET'])
def c1f_page():
    invoice_total_before_refactoring = sum(calculate_total_price_before_refactoring(item['quantity'], item['price']) for item in items)
    invoice_total = calculate_invoice_total(items)
    return jsonify({'before_refactoring': invoice_total_before_refactoring, 'after_refactoring': invoice_total})


if __name__ == '__main__':
    app.run(debug=True)
