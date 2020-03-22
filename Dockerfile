FROM python:3.7-alpine
# this is optional & tells who ones Maintainers
MAINTAINER London App Developer Ltd

# tell python set python unbuffered set 1
# this tells python don't buffered docker
# just print directly
ENV PYTHONUNBUFFERED 1

# copy requiremnts from project directory to docker requirements
COPY ./requirements.txt /requirements.txt
# install of list of command on requirements
RUN pip install -r requirements.txt

# create empty folder app directory
RUN mkdir /app
# set default
WORKDIR /app
# add app file to the app file on docker
COPY ./app /app

# create user
# -D: to be used for running applications only
RUN adduser -D user