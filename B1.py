from flask import Flask, jsonify

app = Flask(__name__)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


@app.route('/b1g', methods=['GET'])
def b1g_page():
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(unsorted_list)
    return jsonify({"sorted_list": unsorted_list})


def bubble_sort2(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def filter_even(arr):
    return list(filter(lambda num: num % 2 == 0, arr))


def algorithm_pipeline(numbers):
    bubble_sort(numbers)
    even_numbers = filter_even(numbers)
    return even_numbers


@app.route('/b1f', methods=['GET'])
def b1f_page():
    numbers = [9, 2, 7, 4, 5, 6, 1, 8, 3]
    b1f_list = algorithm_pipeline(numbers)
    return jsonify({"list": b1f_list})


def load_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data


def process_data(data):
    processed_data = [int(item) * 2 for item in data.split()]
    return processed_data


def update_inventory(processed_data):
    inventory = sum(processed_data)
    return f"Updated inventory: {inventory}"


def main_algorithm(file_path):
    data = load_data_from_file(file_path)
    processed_data = process_data(data)
    return update_inventory(processed_data)


@app.route('/b1e', methods=['GET'])
def b1e_page():
    file_path = "example_data.txt"
    value = main_algorithm(file_path)
    return jsonify({"value": value})


if __name__ == '__main__':
    app.run(debug=True)
