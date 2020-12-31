# Atlantis ROV Project
# Developed by Ryan Oroke during the COVID-19 Pandemic

# You can't sue me for ANYTHING if you use this in any capacity!!!

# Basic Project Layout
"""
    Main
        -Introduction
        -Launch Web Server
        -Loop
            -Get Sensor Data (I2C)
            -Get Control Inputs (HTML)
            -Compute PID Loop Responses
            -Write PWM Values (I2C)
            -Update Webpage (HTML)

"""


# Libraries
import time
import os
import smbus

#Global Variables
webpage_filename = "./runpage.html"

acc_x = 0
acc_y = 0
acc_z = 0
gyro_x = 0
gyro_y = 0
gyro_z = 0
mag_x = 0
mag_y = 0 
mag_z = 0

# Main Function
def main():

    print("Orobotics Atlantis Project");
    print("Developed by Ryan");

    #Launch the web server
    os.system("python -m" + webpage_filename)

# Helper Functions
def updateWebpage():

    #Update the physical HTML file, which will refresh every second
    f = open(webpage_filename, 'wb');
    message = """<html>
                    <head>
                        <title>Orobotics Atlantis ROV</title>
                        <meta http-equiv="refresh" content="1">
                    </head>
                    <body>
                        <p>
                            This is kinda cool
                            and look it updates too!
                        </p>
                    </body>
                </html>"""
    f.write(message);
    f.close;


# Allows for custom rearrangement of main function within the file
if __name__ == "__main__":
    main()
