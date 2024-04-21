# start by pulling the python image
FROM python:alpine

# switch working directory
WORKDIR /tasks

# copy the project files into the image
COPY requirements.txt requirements.txt
COPY tasks_be.py tasks_be.py
COPY tasks_fe.py tasks_fe.py
COPY tasks.json tasks.json

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# configure the container to run in an executed manner

#ENTRYPOINT ["python3"]

CMD ["python3", "tasks_fe.py"]
