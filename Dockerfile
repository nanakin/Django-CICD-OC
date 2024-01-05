# base image : an official Python runtime as a parent image
FROM python:3.11
# sets the working directory inside the Docker container to /app (creates the directory if it doesn’t exist)
WORKDIR /app
# install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
# copy whole project to your Docker CWD directory.
COPY . .
# port where the Django app runs
EXPOSE 8000
# for testing deployment setup purposes (and because we use sqlite) : run DB migrations
RUN python manage.py migrate
# command to run when the Docker container is launched (start the Django app)
CMD ["python3","manage.py", "runserver", "0.0.0.0:8000"]
