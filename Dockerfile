FROM python:3.5

RUN pip install requests

ADD server.py /

CMD ["python3", "/server.py"]

