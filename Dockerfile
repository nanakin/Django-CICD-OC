# syntax=docker/dockerfile:1
# base image : an official Python runtime on a small Linux distribution
FROM python:3.11-slim
# prevents Python from writing pyc files to disc and from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install poetry Python package and dependency manager
RUN pip install poetry
# sets the working directory inside the Docker container to /app (creates the directory if it doesn’t exist)
WORKDIR /app
# copy whole project to your Docker CWD directory.
COPY . .
# install dependencies
RUN poetry install --no-root
# port where the Django app runs
EXPOSE 8000
# run DB migrations (probably temporary)
# for testing deployment setup purposes (and because we use sqlite)
RUN poetry run python manage.py migrate
# command to run when the Docker container is launched (start the Django app)
CMD ["poetry", "run", "python","manage.py", "runserver", "0.0.0.0:8000"]
