FROM python:3.8
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 9095
CMD ["python3", "app.py"]