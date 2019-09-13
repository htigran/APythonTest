FROM python:latest

WORKDIR /usr/local/bin

RUN pip install -r requirements.txt

CMD ["/code/", "-OPTIONAL_FLAG"]
