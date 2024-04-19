import paho.mqtt.client as mqtt

# MQTT broker settings
broker_address = "mqtt.eclipse.org"
broker_port = 1883

# Callback function for when the client receives a CONNACK response from the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe("test/topic")  # Subscribe to the topic
    else:
        print(f"Failed to connect to MQTT broker with return code {rc}")

# Callback function for when the client receives a message from the broker
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

# Create a MQTT client instance
client = mqtt.Client()

# Set up callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
try:
    client.connect(broker_address, broker_port)
except Exception as e:
    print(f"Error connecting to MQTT broker: {e}")
    exit(1)

# Start the MQTT client loop
client.loop_start()

# Publish data to the topic
try:
    while True:
        message = input("Enter message to publish: ")
        client.publish("test/topic", message)
except KeyboardInterrupt:
    pass

# Disconnect from the broker
client.loop_stop()
client.disconnect()
