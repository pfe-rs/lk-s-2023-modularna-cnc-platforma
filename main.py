import serial
import time

# Serial port configuration
port = "/dev/ttyUSB0"  # Replace with the appropriate port name
baud_rate = 115200

# Open the serial port
ser = serial.Serial(port, baud_rate)

# Delay to allow time for the serial port to be ready
time.sleep(2)

# Read G-code commands from file
with open("slika.gcode", "r") as file:
    gcode_program = file.readlines()

# Send G-code commands to the CNC machine
for command in gcode_program:
    cmd = command.strip()  # Remove leading/trailing whitespaces and newlines
    ser.write(cmd.encode())  # Send the G-code command
    ser.write(b"\n")  # Send a newline character
    time.sleep(0.1)  # Add a small delay between commands

# Close the serial port
ser.close()
