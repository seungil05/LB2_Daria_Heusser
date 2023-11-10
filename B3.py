from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/b3g', methods=['GET'])
def b3g_page():
    # Beispiel: Lambda-Ausdruck für das Quadrieren einer Zahl
    square = lambda x: x ** 2
    result_square = square(5)  # result_square = 25
    # Lambda-Ausdruck für das Konvertieren eines Strings in Großbuchstaben
    uppercase_converter = lambda s: s.upper()
    result_uppercase = uppercase_converter("hello")  # result_uppercase = "HELLO"
    return jsonify(result_uppercase + str(result_square))


@app.route('/b3f', methods=['GET'])
def b3f_page():
    # Beispiel: Lambda-Ausdruck für die Addition zweier Zahlen
    addition = lambda x, y: x + y
    result_addition = addition(3, 5)  # result_addition = 8
    # Lambda-Ausdruck für die Multiplikation dreier Zahlen
    multiplication = lambda x, y, z: x * y * z
    result_multiplication = multiplication(2, 4, 3)  # result_multiplication = 24
    return jsonify(result_multiplication + result_addition)


@app.route('/b3e', methods=['GET'])
def b3e_page():
    # Beispiel: Sortieren von Wörtern nach ihrer Länge mithilfe eines Lambda-Ausdrucks
    words = ["orange", "banana", "kiwi", "apple"]
    sorted_words = sorted(words, key=lambda x: len(x))

    # Ergebnis: ['kiwi', 'apple', 'banana', 'orange']
    return jsonify(sorted_words)


if __name__ == '__main__':
    app.run(debug=True)