# Use an official Python runtime as a parent image
FROM python:3.12.3-slim

# Set environment variables to avoid Python buffering (useful for logs)
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files (avoid env and other unwanted files)
COPY requirements.txt /app/
COPY . /app/

# Install the required dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expose the port that the app will run on (typically 8000 for Django)
EXPOSE 8000

# Run Django's migrate and start the application (or your preferred start command)
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
