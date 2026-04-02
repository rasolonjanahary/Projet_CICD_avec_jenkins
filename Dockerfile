FROM python:3.12-slim

WORKDIR /app

COPY require.txt .
 
RUN pip install -r require.txt

COPY . .

CMD ["uvicorn", "app:app"]

CMD ["mlflow", "ui"]
