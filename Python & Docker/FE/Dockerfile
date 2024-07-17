# Pull the image
FROM python:alpine

# Set working directory
WORKDIR /tasks

# Copy project files into the image
COPY requirements.txt .
COPY tasks_fe.py .
COPY tasks_ai.py .
RUN mkdir -p /tasks/static
RUN mkdir -p /tasks/templates
COPY static/styles.css /tasks/static/
COPY templates/index.html /tasks/templates/

# Install required packages
RUN pip install -r requirements.txt

# Configure the container to run
CMD ["python3", "tasks_fe.py"]
EXPOSE 80
