# FROM ubuntu:latest
FROM python:3.8.1
COPY ./*.py /exp/
COPY ./requirements.txt /exp/requirements.txt
COPY ./api/* /exp/api/
COPY ./api/static/* /exp/api/static/
COPY ./api/templates/* /exp/api/templates
COPY ./*.joblib /exp/api/
COPY ./*.joblib /exp/
RUN pip3 install --no-cache-dir -r /exp/requirements.txt
WORKDIR /exp
# CMD ["python", "./plot_digits_classification.py"]
WORKDIR /exp/api
CMD ["python", "./app.py"]
EXPOSE 5000

