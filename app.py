# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 18:59:39 2021

@author: Bhuvesh Kumar
"""

from flask import Flask,jsonify,request
app = Flask(__name__)

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))



def sort_fib_list(fib_list):
    #print(fib_list)
    even_list=[]
    odd_list=[]
    for i in range(len(fib_list)):
        if(fib_list[i]%2==0):
            even_list.append(fib_list[i])
        else:
            odd_list.append((fib_list[i]))

    even_list.sort(reverse=True)
    odd_list.sort(reverse=True)
    #print(even_list)
    return even_list+odd_list


@app.route("/fibonacci", methods=["POST"])
def starting_url():
    print(request.json)
    data = request.json
    print(data['elements'])
    
    num = data['elements']
    fib_list = []
    
    
    if(num < 1 or num >100 ):
        return "Wrong value"
    else:
        #calculate
        for i in range(num):
            fib_list.append(recur_fibo(i))

        sorted_list = sort_fib_list(fib_list)
        return jsonify({'fibonacci':fib_list,
                        'sorted':sorted_list})


@app.route('/')
def Index():
    return "Welcome to the demo app"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
