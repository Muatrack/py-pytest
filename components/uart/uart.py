import serial

class UART:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(port, baudrate, 8, 'N', 1, xonxoff=False)

    def open(self):
        try:
            self.ser.open()
        except serial.SerialException as e:
            print("Fail to open serial:", self.port, 'Exceptions: {e}')
        else:
            print("Succ to open serial:", self.port)
        finally:
            print("Final ...")
            return self.ser

    def cbSet(self, cb ):
        self.cb = cb
    
    def write(self, data):
        self.ser.write(data)

    def close(self):
        self.ser.close()
    
    