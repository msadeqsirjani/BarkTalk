# set base image
FROM python:3.9-slim-buster

# set working directory
WORKDIR /

# copy requirements file
COPY requirements.txt .

# install requirements
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update -y
RUN apt-get install -y libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    wget \
    zip \
    unzip \
    gnupg2

RUN apt-get install -y libxcb-randr0-dev libxcb-xtest0-dev libxcb-xinerama0-dev libxcb-shape0-dev libxcb-xkb-dev

# copy application code
COPY . .

# set environment variables
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# expose the port
EXPOSE 5000

# start the flask application
CMD ["flask", "run", "--host=0.0.0.0"]