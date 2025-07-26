from connections import connect_mqtt, connect_internet
from time import sleep
import temperature
import humidity
import light
import distance

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
        connect_internet(env.get("WIFI_NAME"),password = env.get("WIFI_PASS")) #ssid (wifi name), pass
        client = connect_mqtt("c43e5a2a499a43779f30850aeb202a3f.s1.eu.hivemq.cloud", env.get("MQTT_USER"), env.get("MQTT_PASS")) # url, user, pass

        def cb(topic,message):
            print("topic:" + str(topic))
            if(topic == b"temp request"):
                print("recieved temp request")
                client.publish("temp",str(temperature.getTemp()))
            elif(topic == b"humidity request"):
                client.publish("humidity",str(humidity.getHumidity()))
            elif(topic == b"light request"):
                client.publish("light", str(light.getLight()))
            elif(topic == b"distance request"):
                client.publish("ultrasonic", str(distance.measure_distance()))
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
