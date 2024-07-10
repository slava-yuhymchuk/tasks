# Pull the image
FROM python:alpine

# Set working directory
WORKDIR /tasks

# Copy project files into the image
COPY requirements.txt .
COPY tasks.json .
COPY tasks_be.py .

# Install required packages
RUN pip install -r requirements.txt

# Configure the container to run
CMD ["python3", "tasks_be.py"]
EXPOSE 5000
