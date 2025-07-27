
# TODO: import your module
import paho.mqtt.client as paho 
import requests
import os
import sys
import send_to_openai
from time import sleep

# Get the folder where the script is located, done for you
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "../frontend/src/downloaded_image.jpg")

url = "http://172.20.10.6/1024x768.jpg"             # You will have to change the IP Address

# Function to download the image from esp32, given to you
"""def download_image():
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Image saved to: {filename}")
    else:
        print("Failed to download image. Status code:", response.status_code)
"""
# TODO: Download the image and get a response from openai
def load_env(filepath="../backend/.env"):
    env_vars = {}
    try:
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    env_vars[key.strip()] = value.strip()
    except Exception as e:
        print("Error loading .env file:", e)
    return env_vars
env = load_env()

client = paho.Client(paho.CallbackAPIVersion.VERSION2)
client.tls_set()
client.username_pw_set(env.get("MQTT_USER"), env.get("MQTT_PASS"))



def on_message(client, userdata, message):
    print("message recieved")
    if(message.topic == "take picture"):
        #download_image()
        description = send_to_openai.getResponse("testDog.jpg")
        client.publish("picture description", description)
    else:
        print("invalid topic")

def on_connect(client, userdata, flags, reason_code,properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    

def on_subscribe(client, userdata, mid, reason_code_list,properties):
    # Since we subscribed only for a single channel, reason_code_list contains
    # a single entry
    if reason_code_list[0].is_failure:
        print(f"Broker rejected you subscription: {reason_code_list[0]}")
    else:
        print(f"Broker granted the following QoS: {reason_code_list[0].value}")
    
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.connect("c43e5a2a499a43779f30850aeb202a3f.s1.eu.hivemq.cloud", 8883)
client.subscribe("take picture")
print("Waiting for messages")
client.loop_forever()


# TODO: How to control when to take photo?

