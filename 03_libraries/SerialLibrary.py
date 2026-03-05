import serial
import time

class SerialLibrary:
    def __init__(self,  port="COM7", baudrate=9600, timeout=1):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        time.sleep(2)  # Wait for the connection to establish (especially for Arduino resets)
        print(f"Serial port {port} opened successfully.")

    def write_data(self, data):
        # --- Writing data ---
        # Data must be encoded to bytes before writing
        data_to_send = data.encode("utf-8")
        self.ser.write(data_to_send)
        print(f"Sent: {data_to_send.decode().strip()}")

    def read_data(self):
        #data_to_send = b'\n'
        #self.ser.write(data_to_send)
        received_bytes = self.ser.readline()
        if received_bytes:
            # Data must be decoded from bytes to a string
            received_string = received_bytes.decode('utf-8').strip()
            print(f"Received: {received_string}")
        else:
            print("No data received within the timeout period.")
        return received_string

    def close_serial(self):
        self.ser.close()

'''
import serial

class SerialLibrary:
    def __init__(self, port="COM7", baudrate=9600, timeout=1):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)

    def write_data(self, data):
        self.ser.write(data.encode())

    def read_data(self):
        return self.ser.readline().decode().strip()

    def close_serial(self):
        self.ser.close()
    '''
'''
import serial
import time

# --- Configuration ---
# Replace 'COM4' with your port name (e.g., '/dev/ttyUSB0' on Linux, 'COMx' on Windows)
# Ensure the baud rate matches the device you are communicating with (e.g., Arduino)
SERIAL_PORT = 'COM7'
BAUD_RATE = 9600
TIMEOUT = 1  # Set a read timeout to prevent the program from blocking forever

# --- Open the serial port ---
try:
    # Use a context manager to ensure the port is closed automatically
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=TIMEOUT) as ser:
        time.sleep(2)  # Wait for the connection to establish (especially for Arduino resets)
        print(f"Serial port {SERIAL_PORT} opened successfully.")

        # --- Writing data ---
        # Data must be encoded to bytes before writing
        data_to_send = b'Hello from Python\n'
        ser.write(data_to_send)
        print(f"Sent: {data_to_send.decode().strip()}")

        # --- Reading data ---
        # Read a line from the serial port (up to a newline character)
        received_bytes = ser.readline()

        if received_bytes:
            # Data must be decoded from bytes to a string
            received_string = received_bytes.decode('utf-8').strip()
            print(f"Received: {received_string}")
        else:
            print("No data received within the timeout period.")

except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    '''