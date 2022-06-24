FROM python:3.8.7-slim-buster

COPY ./web /web

WORKDIR /web

EXPOSE 8080

RUN pip install --upgrade pip && pip install -r requirments.txt

CMD ["python", "app"]
