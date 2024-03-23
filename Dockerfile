# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y ;\
    apt install -y \
    build-essential \
    libmemcached-dev zlib1g-dev

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /code
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Django runs on
EXPOSE 8000

# Run Django migrations when the container starts
CMD ["python", "manage.py", "migrate"]

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
