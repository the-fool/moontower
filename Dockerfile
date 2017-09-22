FROM python:3.5

ADD server.py /

CMD ["python3", "/server.py"]

