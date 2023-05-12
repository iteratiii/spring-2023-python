# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# Adapted from simple demo of printer functionality by Tony DiCola
import time
import csv
import board
import busio
import adafruit_mpr121
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

touched = mpr121.touched_pins

import adafruit_thermal_printer

print("Be patient. Cursing will commence.")

# Load up CSV 
with open('curserinfo.csv') as curserinfo:
    info = list(csv.reader(curserinfo, delimiter=','))

# Printer firmware version (find on test page)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.68)

# For a computer, use the pyserial library for uart access.
import serial
uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)

# Create the printer instance.
printer = ThermalPrinter(uart, auto_warm_up=False)

# Initialize the printer.  Note this will take a few seconds for the printer
# to warm up and be ready to accept commands (hence calling it explicitly vs.
# automatically in the initializer with the default auto_warm_up=True).
printer.warm_up()

# Processor load is heavy at startup; 
# this delays starting the loop for a bit 
time.sleep(15)

# Check if the printer has paper.
if printer.has_paper():
    print("Printer has paper! Ready to be touched.")
else:
    print("Printer might be out of paper, or RX is disconnected!")

idx = 0

while True:
    for i in range(12):
        if mpr121[0].value and mpr121[1].value and mpr121[2].value and mpr121[3].value and mpr121[4].value:
            print("Touched. Wait 5 seconds.")

            # Move the paper forward two lines:
            printer.feed(1)

            printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
            printer.bold = True
            printer.print(f"AS OF 4/10/2023,\n{info[idx][0].upper()} OF {info[idx][1].upper()}\nINTRODUCED\n{info[idx][2]} TRANSPHOBIC LAWS\n")
            printer.print("I INVITE YOU TO READ\nTHIS CURSE ALOUD")
            printer.bold = False

            printer.feed(2)

            printer.justify = adafruit_thermal_printer.JUSTIFY_LEFT
            printer.size = adafruit_thermal_printer.SIZE_SMALL
            printer.print("A curse upon you,")
            printer.size = adafruit_thermal_printer.SIZE_MEDIUM
            printer.print(f"{info[idx][0]}.")
            printer.size=adafruit_thermal_printer.SIZE_SMALL
            printer.print("A curse upon your allies, and\nupon all who turn their faces\nfrom your works and close their\neyes to your deeds.\nMay we live untouched by the\nharm you seek to visit upon us.\nMay we flourish as you wither.\nMay we grow and change as your\nways of life are forgotten and\nground into dust by our dancing.\nMay future generations look on\nyou with disgust.\nMay your name be scorned until\nit's forgotten.\nMay you become powerless.")

            printer.feed(2)

            printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
            printer.bold = True
            printer.size = adafruit_thermal_printer.SIZE_SMALL
            printer.print("WHEN YOU HAVE FINISHED,\nIMPALE THIS PAPER")
            printer.bold = False

            printer.feed(4)
            idx = idx + 1
            time.sleep(5)
            print("Ready to print.")
