from connections import connect_mqtt, connect_internet
from time import sleep
import temperature
import humidity
import light
import distance
import oled

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
    env = load_env()
    try: 
        connect_internet(env.get("WIFI_NAME"),password = env.get("WIFI_PASS")) #ssid (wifi name), pass
        client = connect_mqtt("c43e5a2a499a43779f30850aeb202a3f.s1.eu.hivemq.cloud", env.get("MQTT_USER"), env.get("MQTT_PASS")) # url, user, pass

        def cb(topic,message):
            message = message.decode()
            print("topic:" + str(topic) + "Message: " + str(message))
            if(topic == b"temp request"):
                outTemp = str(temperature.getTemp())
                client.publish("temp",outTemp)
                #print("Sending temp: " + outTemp)
            elif(topic == b"humidity request"):
                outHumidity = str(humidity.getHumidity())
                client.publish("humidity",outHumidity)
                #print("Sending humidity: " + outHumidity)
            elif(topic == b"light request"):
                outLight = str(light.getLight())
                client.publish("light",outLight)
                #print("Sending light: " + outLight)
            elif(topic == b"distance request"):
                outDistance = str(distance.measure_distance())
                client.publish("ultrasonic", outDistance)
                #print("Sending distancet: " + outDistance)
            elif(topic == b"display request"):
                print("recieved display request: " + message)
                oled.display(message)
        client.set_callback(cb)
        client.subscribe("text")
        
        client.subscribe("temp request")
        client.subscribe("humidity request")
        client.subscribe("light request")
        client.subscribe("distance request")
        client.subscribe("display request")
        while True:
            client.check_msg()
            sleep(0.1)

    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()
