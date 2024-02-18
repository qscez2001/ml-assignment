FROM arm64v8/python:3.8-slim

COPY . /app
WORKDIR /app

RUN pip install torch torchvision torchaudio

RUN pip install -r requirements.txt

EXPOSE 9527

CMD uvicorn main:app --host 127.0.0.1 --port 9527 --reload
