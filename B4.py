from functools import reduce
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/b4g', methods=['GET'])
def b4g_page():
    # Beispiel: Anwendung von Map, Filter und Reduce auf eine Liste von Zahlen
    numbers = [1, 2, 3, 4, 5]

    # Map: Quadrieren jeder Zahl
    squared_numbers = list(map(lambda x: x ** 2, numbers))

    # Filter: Auswahl nur der geraden Zahlen
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    # Reduce: Berechnung der Summe aller Zahlen
    sum_all = reduce(lambda x, y: x + y, numbers)

    return jsonify({
        'numbers': numbers,
        'squared_numbers': squared_numbers,
        'even_numbers': even_numbers,
        'sum_all': sum_all
    })


@app.route('/b4f', methods=['GET'])
def b4f_page():
    # Beispiel: Verarbeitung von Wörtern in einer Liste

    words = ["apple", "banana", "kiwi", "orange"]

    # Map: Konvertierung zu Großbuchstaben
    uppercase_words = list(map(lambda x: x.upper(), words))

    # Filter: Auswahl von Wörtern mit mehr als fünf Buchstaben
    long_words = list(filter(lambda x: len(x) > 5, uppercase_words))

    # Reduce: Konkatenation der ausgewählten Wörter
    concatenated_string = reduce(lambda x, y: x + y, long_words)

    return jsonify({
        'words': words,
        'uppercase_words': uppercase_words,
        'long_words': long_words,
        'concatenated_string': concatenated_string
    })


@app.route('/b4e', methods=['GET'])
def b4e_page():
    # Beispiel: Verarbeitung von Studentendaten
    students = [
        {"name": "Alice", "grades": [85, 90, 78]},
        {"name": "Bob", "grades": [92, 88, 95]},
        {"name": "Charlie", "grades": [78, 80, 85]}
    ]

    # Map: Durchschnittsnote für jeden Studenten berechnen
    average_grades = list(map(lambda student: sum(student["grades"]) / len(student["grades"]), students))

    # Filter: Auswahl von Studenten mit Durchschnittsnote über 85
    top_students = list(filter(lambda avg: avg > 85, average_grades))

    # Reduce: Berechnung des Gesamtdurchschnitts der Top-Studenten
    total_average = reduce(lambda x, y: x + y, top_students) / len(top_students)

    return jsonify({
        'students': students,
        'average_grades': average_grades,
        'top_students': top_students,
        'total_average': total_average
    })


if __name__ == '__main__':
    app.run(debug=True)
