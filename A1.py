from flask import Flask, render_template, jsonify

app = Flask(__name__)


# Beispiel für eine Pure Function
def add_numbers(a, b):
    return a + b


# Beispiel für eine Prozedur
def print_greeting(name):
    return f"Hello, {name}!"


@app.route('/a1g', methods=['GET'])
def a1g_page():
    result = add_numbers(3, 5)
    name = print_greeting('Vanesa')

    text = name + str(result)
    return jsonify(text)


@app.route('/a1e', methods=['GET'])
def a2e_page():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    from NumberList import NumberList
    number_list = NumberList(numbers)

    even_numbers_prozedurale = number_list.filter_even_prozedurale()
    even_numbers_funktionale = number_list.filter_even_funktionale()

    return jsonify(str(even_numbers_prozedurale), str(even_numbers_funktionale))


# Beispiel für Immutable values in Python
immutable_list = (1, 2, 3)  # Tuple ist unveränderlich

# Versuch, den Tuple zu ändern, führt zu einem Fehler
# immutable_list[0] = 5  # TypeError: 'tuple' object does not support item assignment

# Beispiel für referenzierte Objekte (mutable) in Python
mutable_list = [1, 2, 3]  # Liste ist veränderlich


@app.route('/a1f')
def a1f_page():
    mutable_list[0] = 5
    return jsonify(mutable_list)


if __name__ == '__main__':
    app.run(debug=True)