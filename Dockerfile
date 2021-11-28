# Alpine is  Linux distro
FROM python:3.9-alpine
# the present working directory
WORKDIR /my-flask-app
# copy the contents into the working dir and add for image
ADD . /my-flask-app
# run pip to install the dependencies of the app
RUN pip3 install -r requirements.txt
#  the command to start the container
CMD ["python3","app.py"]
