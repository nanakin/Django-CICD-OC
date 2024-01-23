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
# redefine container entrypoint
ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]