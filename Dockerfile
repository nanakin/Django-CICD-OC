# base image : an official Python runtime as a parent image
FROM python:3.11
# sets the working directory inside the Docker container to /app (creates the directory if it doesn’t exist)
WORKDIR /app 
# copies the file from the project dir on your machine to the CWD inside the container (/app)
COPY requirements.txt .
# install dependencies  
RUN pip3 install --upgrade pip  
RUN pip3 install -r requirements.txt --no-cache-dir
# copy whole project to your docker home directory.
COPY . .
# port where the Django app runs  
EXPOSE 8000  
# command to run when the Docker container is launched (sart the Django app)
CMD ["python3","manage.py", "runserver", "0.0.0.0:8000"]  
