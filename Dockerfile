# Start from a lightweight Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code into the container
COPY . .

# Expose port 5000 so you can reach the Flask app
EXPOSE 5000

# When the container starts, run the Flask app
CMD ["python", "app.py"]
