FROM python3:8

RUN mkdir /app

COPY main.py /app/main.py

ENTRYPOINT ["python3", "/app/main.py"]