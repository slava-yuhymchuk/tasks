# start by pulling the python image
FROM python:alpine

# switch working directory
WORKDIR /tasks

# copy the project files into the image
COPY requirements.txt .
COPY tasks.json .
COPY tasks_be.py .
COPY tasks_fe.py .

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# configure the container to run in an executed manner
#ENTRYPOINT ["python3"]
CMD ["python3", "tasks_fe.py"]
EXPOSE 5000
