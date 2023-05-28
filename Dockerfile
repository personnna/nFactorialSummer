FROM python:3-alpine
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
ENV FLASK_APP=my_flask.py
CMD [ "python3", "."]
