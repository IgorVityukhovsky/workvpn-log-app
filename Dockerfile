FROM python:3.6-alpine
RUN pip install watchdog
COPY count_connections.py /usr/src/app/count_connections.py
WORKDIR /usr/src/app
CMD ["python", "-u", "count_connections.py"]
