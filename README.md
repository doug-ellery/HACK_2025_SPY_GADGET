# SPY GADGET for UCLA HaCK 2025

**Frontend Directory**: Responsible for the dashboard we created using React. This dashboard displays all of the sensor data as well as what the camera is seeing.

**Backend Directory**: Responsible for taking in requests from the React interface, and then passing these requests on to either the rasberry pi (for sensor data) or the AI folder which makes the API calls. 

**Pico Directory**: Micropython programs for the Rasberry Pi pico 2 that is used. This pico is hooked up to a circuit with all of the sensors in it, and there are various programs in this directory for getting different sensor data. Everything runs in main.py, which is automatically booted when the rasberry pi is started.

**AI Directory**: Python files in charge of recieving a photo taken by the camera, and then using this photo to make an API call that gets a photo to text description, and then convert that description to an audio recording as well. 


    
