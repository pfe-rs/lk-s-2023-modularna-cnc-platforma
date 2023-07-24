import serial
from pynput import keyboard
import time

# Serial port configuration
port = "/dev/ttyUSB1"  # Replace with the appropriate port name
baud_rate = 250000
# Open the serial port
ser = serial.Serial(port, baud_rate)
time.sleep(5) # wait for serial port

def send_gcode(command):
    cmd = command.strip()  
    ser.write(cmd.encode())
    time.sleep(0.1)
send_gcode("G91\r\n")
send_gcode("G21\r\n")
send_gcode("G00 X-10 Y-20 Z5\r\n")    
ser.close()