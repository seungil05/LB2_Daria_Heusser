from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/b3g', methods=['GET'])
def b3g_page():
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    return jsonify(squared_numbers + even_numbers)


@app.route('/b3f', methods=['GET'])
def b3f_page():
    addition = lambda x, y: x + y
    result_addition = addition(3, 5)
    multiplication = lambda x, y, z: x * y * z
    result_multiplication = multiplication(2, 4, 3)
    return jsonify(result_multiplication + result_addition)


@app.route('/b3e', methods=['GET'])
def b3e_page():
    words = ["orange", "banana", "kiwi", "apple"]
    sorted_words = sorted(words, key=lambda x: len(x))
    data = [5, 12, 8, 3, 15]
    maximum_value = max(data, key=lambda x: x % 10)
    return jsonify(sorted_words + [maximum_value])


if __name__ == '__main__':
    app.run(debug=True)