FROM python:3
COPY count_connections.py /usr/src/app/count_connections.py
WORKDIR /usr/src/app
CMD ["python", "count_connections.py"]