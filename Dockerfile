# Using an official Python runtime as the base image
FROM python:3.9-slim

# Setting the working directory in the container to /app
WORKDIR /app

# Copying the current directory contents into the container at /app
COPY . /app

# Installing needed dependencies specified in requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Exposing the port on which the application runs within the Docker container
EXPOSE 8080

# Defining environment variable
ENV GREETINGS Hello

# Run app.py when the container launches
CMD ["python", "web-server.py"]
