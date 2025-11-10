# Start from a lightweight Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency file and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY FlaskApp/ .

# Inform Docker that the container listens on port 5000
EXPOSE 5000

RUN python init_db.py

# Define the command to run the application when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]