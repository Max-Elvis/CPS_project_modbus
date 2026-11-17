"""
Basic Modbus TCP client 
Polls the field device in a constant loop
"""
import time
from pymodbus.client import ModbusTcpClient

SERVER_HOST = "modbus-server"
SERVER_PORT = 502

def main():
    client = ModbusTcpClient(SERVER_HOST, port=SERVER_PORT)
    while True:
        if client.connect():
            rr = client.read_holding_registers(0, 10)
            if not rr.isError():
                print(f"Holding registers: {rr.registers}")
            else:
                print(f"Read error: {rr}")
        else:
            print("Connection failed, retrying...")
        time.sleep(5)

if __name__ == "__main__":
    main()