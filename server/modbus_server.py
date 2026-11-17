"""
Basic Modbus TCP server (the simulated field device / slave).
"""
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.server import StartTcpServer

def main():
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [0] * 100),
        co=ModbusSequentialDataBlock(0, [0] * 100),
        hr=ModbusSequentialDataBlock(0, [0] * 100),
        ir=ModbusSequentialDataBlock(0, [0] * 100),
    )
    context = ModbusServerContext(slaves=store, single=True)
    print("Starting Modbus TCP server on 0.0.0.0:502 ...")
    StartTcpServer(context=context, address=("0.0.0.0", 502))

if __name__ == "__main__":
    main()