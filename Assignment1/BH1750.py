import time
import adafruit_bh1750

# Initialize the BH1750 sensor with the default I2C address (0x23)
i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)

# Set the measurement mode to continuous high-resolution mode
sensor.mode = adafruit_bh1750.BH1750.ONCE_HIRES_1

while True:
    # Read the light level
    lux = sensor.luminance

    # Print the light level to the terminal
    print("Light level: {:.2f} lx".format(lux))

    # Wait for one second
    time.sleep(1)
