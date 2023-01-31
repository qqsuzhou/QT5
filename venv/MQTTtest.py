"""
    MQTT 发布测试
    Pip 安装 Paho MQTT 客户端：pip3 install -i https://pypi.doubanio.com/simple paho-mqtt
    导入 Paho MQTT客户端: from paho.mqtt import client as mqtt_client
"""

import random
import time

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic = "/python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    print(client_id)

    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# 发布MQTT信息
def publish(client):
    msg_count = 0
    while True:
        time.sleep(5)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 100

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    client.loop_start()
    # 发布信息
    publish(client)
    # 订阅信息
    # subscribe(client)
    # client.loop_forever()

if __name__ == '__main__':
    run()
