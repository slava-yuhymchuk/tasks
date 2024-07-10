# Pull the image
FROM python:alpine

# Set working directory
WORKDIR /tasks

# Copy project files into the image
COPY requirements.txt .
COPY tasks_fe.py .
COPY tasks_ai.py .

# Install required packages
RUN pip install -r requirements.txt

# Configure the container to run
CMD ["python3", "tasks_fe.py"]
EXPOSE 80
