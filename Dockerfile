FROM python:3.5

ADD server.py /

RUN pip install requests

CMD ["python3", "/server.py"]

