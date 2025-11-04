FROM python:3.9

# Use official Python image as base
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy application files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the required port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
