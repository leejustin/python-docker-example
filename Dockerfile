FROM python:3.9.4-slim-buster

RUN python3 -m pip install requests

COPY . .

CMD ["python3", "app.py"]
