# Python and Flask REST web service
### Functionality
The web service takes in a numerical value between 1 to 100, and returns the Fibonacci sequence, as well as a sequence that is sorted using the following conditions:
* Even numbers first, in descending order
* Odd numbers, in descending order


### Example: 
If user does a http get to http://myserver:8000/fibonacci with the following json payload:
```json

{
 "elements": 10
} 
```

it will return me the following JSON:
```json
{
 "fibonacci": [0,1,1,2,3,5,8,13,21,34],
 "sorted": [34,8,2,0,21,13,5,3,1,1]
}
```





# How to use 
### clone the repo
```
$ git clone https://github.com/bhuveshsharma09/my-flask-app.git
```
### change the working directory to resumeit
```
$ cd my-flask-app
```
### install the requirements
```
$ python3 -m pip install -r requirements.txt
```
### run
```
python3 app.py
```

# Configuration
Current configuration for host is '0.0.0.0' and port is 80

# Functional prototype deployed at OCI
Link: http://168.138.176.208/


# Testing
Step 1: Go to  http://168.138.176.208/ and enter a number in input field and hit 'compute' button


Step 2: The web app will send request to http://168.138.176.208/fibonacci/ 


Step 3: The web app will show the reponse in the page
