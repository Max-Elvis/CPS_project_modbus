FROM python:3.11-slim

WORKDIR /app

# everything the attacker might need
RUN apt-get update && apt-get install -y --no-install-recommends \
    iputils-ping \
    hping3 \
    tcpreplay \
    mbpoll \
    tshark \
    nmap \
    iproute2 \
    net-tools \
    tcpdump \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    scapy==2.5.0 \
    pymodbus==3.6.9

COPY attacks/ ./attacks/

# Keep the container running
CMD ["sleep", "infinity"]