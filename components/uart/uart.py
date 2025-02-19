import serial

class UART:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(port, baudrate)

    def cbSet(self, cb:function ):
        self.cb = cb
    
    def write(self, data):
        self.ser.write(data)
    
    