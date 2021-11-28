# Python and Flask REST web service  http://168.138.176.208/ 
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



# Deployed on OCI (Oracle Cloud Infrastructure)
The web service has been deployed on OCI and can we accessed using 

Link of the global API (hosted on OCI): http://168.138.176.208/ ;

Link to call API in your program: http://168.138.176.208/fibonacci

# Build and Run Docker image using Dockerfile
the docker file helps to build an image of program which can later be run in a container.
To do so, please follow the commands
```
$ git clone https://github.com/bhuveshsharma09/my-flask-app.git

### build docker image

$ docker image build -t my-flask-app .

### check if the image has been build successfully

$ docker image ls

### run the image in a container

$ docker run -d -p 80:80 my-flask-app

```


# How to use 
### clone the repo
```
$ git clone https://github.com/bhuveshsharma09/my-flask-app.git
```
### change the working directory to my-flask-app
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
* **Step 1:** Go to  http://168.138.176.208/ and enter a number in input field and hit 'compute' button
![image](https://user-images.githubusercontent.com/62707309/143731935-b338e16d-d7cb-416c-8ddb-c1740eeef6c0.png)


* **Step 2:** The web app will send request to http://168.138.176.208/fibonacci/ 
![image](https://user-images.githubusercontent.com/62707309/143731996-d7643ab6-0fca-4389-a480-a54cf71d77a8.png)

![image](https://user-images.githubusercontent.com/62707309/143732009-153fa761-82d9-481e-b8c6-7fd7dbb11ca9.png)

* **Step 3:** The web app will show the reponse in the page


# Note
The API request url is http://168.138.176.208/fibonacci/ . Only for the demo purpose I developed the page where user can easily enter value and computer fib sequence (using API).
Although the API and webpage resides in the same program, the function calls API link to fullfil the requirment.
