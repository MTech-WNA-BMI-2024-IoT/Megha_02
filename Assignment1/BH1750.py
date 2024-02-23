import time
import board
import busio
import adafruit_bh1750

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create sensor object
sensor = adafruit_bh1750.BH1750(i2c)

# Main loop
try:
    while True:
        # Read the light level
        light_level = sensor.lux

        # Print the light level
        print("Light: {} lux".format(light_level))

        # Wait for a moment
        time.sleep(1)

# Exit cleanly
except KeyboardInterrupt:
    pass
