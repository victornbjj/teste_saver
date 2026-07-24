FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY  . .


ENV FLASK_APP=app.py 

EXPOSE 5000

ENTRYPOINT [ "sh", "-c", "python seed.py && python app.py" ]