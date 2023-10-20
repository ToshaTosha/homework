import time
import paho.mqtt.client as paho
import led as led
import random


broker = 'broker.emqx.io'


def on_message(client, userdata, message):
    time.sleep(1)
    data = str(message.payload.decode("utf-8"))
    print("received message =", data)

    if data == "u":
        led.send_command("u", 6)
    elif data == "d":
        led.send_command("d", 7)


client = paho.Client('client-isu-38')
client.on_message = on_message


print("Connecting to broker", broker)
client.connect(broker)
client.loop_start()
print("Subscribing")
client.subscribe("abobus/abobus")
time.sleep(200)
client.disconnect()
client.loop_stop()