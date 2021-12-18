FROM python:3.8-slim

COPY ./* /

RUN pip install requests

CMD ["python", "."]
