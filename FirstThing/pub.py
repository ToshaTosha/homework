import time
import paho.mqtt.client as paho
import random


broker = "broker.hivemq.com"


client = paho.Client("client-isu-228")


print("Connecting to broker", broker)
client.connect(broker)
client.loop_start()
print("Publishing")


for _ in range(10):
    state = "Атеисты такие: научная коровка" if random.randint(0, 1) else "off"
    print(f'Атеисты такие: научная коровка')
    client.publish("house/bulb1", state)
    time.sleep(random.randint(4, 10))


client.disconnect()
client.loop_stop()