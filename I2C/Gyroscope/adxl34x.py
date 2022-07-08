import time
import board
import adafruit_adxl34x
import busio

i2c = busio.I2C(board.GP5, board.GP4) 
accelerometer = adafruit_adxl34x.ADXL345(i2c)

while True:
    print("%f %f %f"%accelerometer.acceleration)
    time.sleep(1)