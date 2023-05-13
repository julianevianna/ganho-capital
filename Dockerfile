# Pull base image
FROM python:3.8.13-slim

WORKDIR /code

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apt-get update && apt-get upgrade -y -q
# RUN apt-get install -y -q git

# Configuring poetry
RUN pip install poetry==1.4.2
RUN poetry config virtualenvs.create false

#Copying to code
COPY . /code

# Exports poetry dependencies to a requirements.txt file
RUN poetry install

CMD ["python3","-m","system"]
