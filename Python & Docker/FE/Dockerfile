# Pull the image
FROM python:alpine

# Set working directory
WORKDIR /tasks

# Install required packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files into the image
COPY tasks_fe.py .
COPY tasks_ai.py .
RUN mkdir -p /tasks/static
RUN mkdir -p /tasks/static/images
RUN mkdir -p /tasks/templates
COPY static/styles.css /tasks/static/
COPY static/images/logo.png /tasks/static/images/
COPY static/images/photo.png /tasks/static/images/
COPY templates/index.html /tasks/templates/

# Configure the container to run
CMD ["python3", "tasks_fe.py"]
EXPOSE 443
