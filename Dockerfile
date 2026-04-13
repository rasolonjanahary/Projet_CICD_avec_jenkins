FROM python:3.12-slim

WORKDIR /app

COPY require.txt .

RUN pip install -r require.txt

COPY . .

EXPOSE 8000

EXPOSE 5000

RUN chmod +x start.sh

CMD ["./start.sh"]
