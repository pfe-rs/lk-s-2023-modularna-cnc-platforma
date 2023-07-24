import serial
from pynput import keyboard
import time

# Serial port configuration
port = "/dev/ttyUSB0"  # Replace with the appropriate port name
baud_rate = 115200
# Open the serial port
ser = serial.Serial(port, baud_rate)
time.sleep(2) # wait for serial port

def send_gcode(command):
    cmd = command.strip()  
    ser.write((cmd+'\n').encode())
    time.sleep(0.1)  

def on_press(key):
    if key == keyboard.Key.esc:
        # Stop the listener and close the serial port
        ser.close()
        return False
    elif key.char == 'w':
        # Move forward
        command = "G1 Y10\n" 
        send_gcode(command)
    elif key.char == 'a':
        # Move left
        command = "G1 X-10\n"  
        send_gcode(command)
    elif key.char == 's':
        # Move backward
        command = "G1 Y-10\n"  
        send_gcode(command)
    elif key.char == 'd':
        # Move right
        command = "G1 X10\n"  
        send_gcode(command)

send_gcode("G21\n")
send_gcode("G91\n")
# Create a listener for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

ser.close()
