FROM python:3-alpine
COPY count_connections.py /usr/src/app/count_connections.py
WORKDIR /usr/src/app
CMD ["python", "-u", "count_connections.py"]
