FROM python:2.7
MAINTAINER Kinnari Jasoliya "kinnarijasoliya2606@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
