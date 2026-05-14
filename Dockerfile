# Use official Python runtime as a parent image
FROM python:3.11.7-slim

# Install minimal system dependencies
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run gunicorn when the container launches
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
