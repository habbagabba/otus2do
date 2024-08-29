#docker build -t homework_03:prebeta .
#docker run -p 8000:8000 homework_03:prebeta


FROM python:3.12.2-bookworm

WORKDIR /opt/homework_03

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY main.py ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

