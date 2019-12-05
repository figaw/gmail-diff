FROM python:3.8.0-alpine3.10

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY list.py /usr/src/app/

CMD ["python3", "/usr/src/app/list.py"]
