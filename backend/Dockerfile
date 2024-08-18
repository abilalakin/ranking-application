FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire content of the current directory into the container
COPY . .

# Expose port 5000
EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
