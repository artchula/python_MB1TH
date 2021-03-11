import minimalmodbus
import serial 

# serial line
instrument = minimalmodbus.Instrument('/dev/ttyUSB0',1)
instrument.serial.baudrate= 9600
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 0.05 # seconds

# modbus reading register,device,input register function
temp = instrument.read_registers(1,1,4)
humid =instrument.read_registers(0,1,4)
print("temp")
print(temp)

print("humid")
print(humid)
