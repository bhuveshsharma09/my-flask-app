# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 18:59:39 2021

@author: Bhuvesh Kumar
"""

# importing all the required libs
from flask import Flask, jsonify, request, render_template
# to avoid Cross-Origin Resource Sharing error
from flask_cors import CORS, cross_origin

# initialising a flask web server instance
app = Flask(__name__)

# configuring the CORS object
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def fibonacci(n):
    # the function to compute fibonacci sequence
    # logic theory: https://www.mathsisfun.com/numbers/fibonacci-sequence.html
    accumulate = []

    # initialising
    a, b = 0, 1
    accumulate.append(a)
    for i in range(n):
        accumulate.append(b)
        # as next number is sum of last two numbers
        a, b = b, a + b
    return accumulate


def sort_accumulated_numbers(fib_list):
    # the function to sort Fibonacci numbers as per business logic
    even_list = []
    odd_list = []

    for i in range(len(fib_list)):
        # splitting values based on even or odd
        if fib_list[i] % 2 == 0:
            even_list.append(fib_list[i])
        else:
            odd_list.append((fib_list[i]))

    # using python in-build sort function
    even_list.sort(reverse=True)
    odd_list.sort(reverse=True)
    # print(even_list)
    return even_list + odd_list


@app.route('/')
@cross_origin()
def Index():
    # to provide a UI for introduction to the API
    return "hello"
    # return render_template("index.html")


@app.route("/fibonacci", methods=["POST"])
@cross_origin()
def business_logic():
    # get payload from body of request
    data = request.json

    # load the value in a local variable
    num = data['elements']

    # as per the logic
    # the allowed numbers are from 1 to 100
    # other all values will no be processed
    if num < 1 or num > 100:
        return "Wrong value"
    else:
        # get the Fibonacci sequence
        fibonacci_sequence = fibonacci(num)
        # preprocess a bit as there is an additional element in the list
        fibonacci_sequence = fibonacci_sequence[:-1]

        # sort the fibonacci_sequence as per business logic
        sorted_list = sort_accumulated_numbers(fibonacci_sequence)

        # return the required data in JSON format
        return jsonify({
            'fibonacci': fibonacci_sequence,
            'sorted': sorted_list
        })


# to make sure that this code only runs
# if the program is being run directly
# and not being called by other program
if __name__ == "__main__":
   # to run the program at flask web server
    app.run(host="0.0.0.0", port=80)
