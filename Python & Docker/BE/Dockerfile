# Pull the image
FROM python:alpine

# Set working directory
WORKDIR /tasks

# Install required packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files into the image
COPY tasks.json .
COPY tasks_be.py .

# Configure the container to run
CMD ["python3", "tasks_be.py"]
EXPOSE 5000
