import RPi.GPIO as GPIO
import time

# Define the GPIO pin connected to the IR sensor
IR_SENSOR_PIN = 23

# Set up GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)


# print("IR Sensor Test (Ctrl+C to exit)")

while True:
    # Read the state of the IR sensor
    sensor_state = GPIO.input(IR_SENSOR_PIN)

    # If sensor detects an object
    if sensor_state == GPIO.HIGH:
        print("Object detected!")

    # Wait for a short duration before reading again
    time.sleep(0.2)

GPIO.cleanup()

##----------------------------------------------------------------------------------------

# import RPi.GPIO as GPIO
# import time

# # declare the sensor and led pin
# sensor_pin = 23
# led_pin = 26

# # GPIO setup
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(sensor_pin, GPIO.IN)
# GPIO.setup(led_pin, GPIO.OUT)

# try:
#     while True:
#         if GPIO.input(sensor_pin):
#             # If no object is near
#             GPIO.output(led_pin, False)
#             while GPIO.input(sensor_pin):
#                 time.sleep(0.2)
#         else:
#             # If an object is detected
#             GPIO.output(led_pin, True)
# except KeyboardInterrupt:
#     GPIO.cleanup()
