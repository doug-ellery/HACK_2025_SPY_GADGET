from connections import connect_mqtt, connect_internet
from time import sleep
import temperature
import humidity
import light
import distance

#Using the .env file to hole my wifi info as well
def load_env(filepath=".env"):
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


def main():
    try: 
        env = load_env()
        connect_internet(str(env.get("WIFI_NAME")),password = str(env.get("WIFI_PASS"))) #ssid (wifi name), pass
        client = connect_mqtt("c43e5a2a499a43779f30850aeb202a3f.s1.eu.hivemq.cloud", str(env.get("MQTT_USER")), str(env.get("MQTT_PASS"))) # url, user, pass

        def cb(topic,message):
            if(topic == "temp request"):
                client.publish("temp",temperature.getTemp())
            elif(topic == "humidity request"):
                client.publish("humidity",humidity.getHumidity())
            elif(topic == "light request"):
                client.publish("light", light.getLight)
            elif(topic == "distance request"):
                client.publish("distance", distance.getDistance())
        client.set_callback(cb)
        client.subscribe("text")
        client.subscribe("temp request")
        client.subscribe("humidity request")
        client.subscribe("light request")
        client.subscribe("distance request")
        while True:
            client.check_msg()
            sleep(0.1)

    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()




