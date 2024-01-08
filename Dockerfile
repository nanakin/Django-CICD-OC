# syntax=docker/dockerfile:1
# base image : an official Python runtime on a small Linux distribution
FROM python:3.11-alpine
# prevents Python from writing pyc files to disc and from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# sets the working directory inside the Docker container to /app (creates the directory if it doesn’t exist)
WORKDIR /app
# install dependencies
COPY requirements.txt .
RUN pip install pip==23.3.2 --no-cache-dir && pip install -r requirements.txt --no-cache-dir
# copy whole project to your Docker CWD directory.
COPY . .
# port where the Django app runs
EXPOSE 8000
# run DB migrations (probably temporary)
# for testing deployment setup purposes (and because we use sqlite)
RUN python manage.py migrate
# command to run when the Docker container is launched (start the Django app)
CMD ["python3","manage.py", "runserver", "0.0.0.0:8000"]
