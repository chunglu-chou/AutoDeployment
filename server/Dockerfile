FROM python:3.8.5
COPY . /server
WORKDIR /server
RUN pip3 install -r requirements.txt
EXPOSE 3001
CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "3001"]