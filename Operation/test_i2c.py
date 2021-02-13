# To test the I2C communication protocol of the Raspberry Pi Zero



import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

kit.servo[0].angle = 10;
time.sleep(1)
kit.servo[0].angle = 140;
time.sleep(1)
kit.servo[0].angle = 90;

print("done!")
