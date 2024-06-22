FROM python

RUN mkdir -p /home/connect

COPY . /home/connect

RUN pip install -r /home/connect/requirements.txt

CMD ["python", "/home/connect/database.py"]

EXPOSE 4002