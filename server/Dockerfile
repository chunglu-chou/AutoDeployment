FROM ubuntu:18.04
FROM python:3.8.5
COPY . /server
WORKDIR /server
RUN apt-get update && apt-get install -y npm
RUN npm install
RUN pip3 install -r requirements.txt
RUN apt-get remove -y npm
EXPOSE 3001
CMD ["node", "inference.js"]
