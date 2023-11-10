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


if __name__ == '__main__':
    app.run(debug=True)
