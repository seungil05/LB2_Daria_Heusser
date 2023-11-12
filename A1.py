from flask import Flask, render_template, jsonify

app = Flask(__name__)


# Beispiel für eine Pure Function
def add_numbers(a, b):
    return a + b


# Beispiel für eine Prozedur
def add_and_print(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is: {result}")


@app.route('/a1g', methods=['GET'])
def a1g_page():
    result = add_numbers(3, 5)
    add_and_print(3, 4)

    return jsonify(result)


@app.route('/a1e', methods=['GET'])
def a1e_page():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    from NumberList import NumberList
    number_list = NumberList(numbers)

    even_numbers_prozedurale = number_list.filter_even_prozedurale()
    even_numbers_funktionale = number_list.filter_even_funktionale()

    return jsonify(str(even_numbers_prozedurale), str(even_numbers_funktionale))


# Beispiel für Immutable values in Python
immutable_list = (1, 2, 3)

# Beispiel für referenzierte Objekte in Python
mutable_list = [1, 2, 3]


@app.route('/a1f')
def a1f_page():
    mutable_list[0] = 5
    return jsonify(mutable_list)


if __name__ == '__main__':
    app.run(debug=True)