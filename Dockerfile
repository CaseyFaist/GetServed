FROM python:3.12

EXPOSE 8080

WORKDIR /home/app

COPY . .
RUN pip install -U pip
RUN pip install -U --no-cache-dir . --compile

CMD ["uvicorn", "getserved.app:app", "--host", "0.0.0.0", "--port", "8080"]