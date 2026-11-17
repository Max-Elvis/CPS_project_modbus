FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir pymodbus==3.6.9

COPY modbus_client.py .

CMD ["python", "-u", "modbus_client.py"]