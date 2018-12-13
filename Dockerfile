FROM python:3-slim
RUN pip3 install flask flask_cors requests
ADD . /webserver
WORKDIR /webserver
EXPOSE 8088
CMD ["python3", "Main.py"]