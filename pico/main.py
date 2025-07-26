from connections import connect_mqtt, connect_internet
from time import sleep
import temperature
import humidity
import light
import distance

def main():
    try:
        with open('creds.txt', 'r') as file:
            ID = file.read()
            myPass = file.read()
        connect_internet(ID,password = myPass) #ssid (wifi name), pass
        client = connect_mqtt("c43e5a2a499a43779f30850aeb202a3f.s1.eu.hivemq.cloud", "doug_ellery", "HaCK_2025") # url, user, pass
        client.subscribe("temp request")
        client.subscribe("humidity request")
        client.subscribe("light request")
        client.subscribe("distance request")
        def cb(topic, message):
            if(topic == "temp request"):
                client.publish("temp",temperature.getTemp())
            elif(topic == "humidity request"):
                client.publish("humidity",humidity.getHumidity())
            elif(topic == "light request", light.getLight()):
                client.publish("light", light.getLight)
            elif(topic == "distance request"):
                client.publish("distance", distance.getDistance())
        while True:
            client.check_msg()
            sleep(0.1)

    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()



