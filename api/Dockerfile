FROM python

RUN mkdir -p /home/api

COPY . /home/api

RUN pip install -r /home/api/requirements.txt

CMD ["python", "/home/api/api.py"]

EXPOSE 4001