from flask import Flask, render_template, jsonify

app = Flask(__name__)


def greet(name):
    return f"Hello, {name}!"


# Funktion als Objekt speichern
greeting_function = greet


# Funktion als Parameter übergeben
def apply_and_print(func, value):
    result = func(value)
    return result


@app.route('/b2g', methods=['GET'])
def b2g_page():
    result = apply_and_print(greeting_function, 'Elina')
    return jsonify(result)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def apply_operation(x, y, operation):
    return operation(x, y)


@app.route('/b2f', methods=['GET'])
def b2f_page():
    result_add = apply_operation(5, 3, add)
    result_subtract = apply_operation(5, 3, subtract)
    return jsonify(result_add, result_subtract)


def outer_function(base):
    def inner_function(x):
        return base + x
    return inner_function


@app.route('/b2e', methods=['GET'])
def b2e_page():
    add_five = outer_function(5)
    result = add_five(3)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)