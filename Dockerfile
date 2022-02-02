FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3.8 \
    python3-pip

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "src/main.py"]