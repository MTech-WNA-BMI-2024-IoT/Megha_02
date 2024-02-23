import time
import adafruit_BH1750

# Initialize the BH1750 sensor with the default I2C address (0x23)
sensor = BH1750.BH1750()

# Set the measurement mode to continuous high-resolution mode
sensor.set_mode(BH1750.BH1750.ONCE_HIRES_1)

while True:
    # Read the light level
    lux = sensor.read()

    # Print the light level to the terminal
    print("Light level: {:.2f} lx".format(lux))

    # Wait for one second
    time.sleep(1)
