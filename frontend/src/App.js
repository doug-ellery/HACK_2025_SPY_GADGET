import React, { useState, useEffect } from "react";
import io from 'socket.io-client';
import './App.css';
import downloaded_image from './downloaded_image'

const socket = io('http://localhost:8000');

function App() {
  const [pictureStatus, setPictureStatus] = useState("");
  const [currTemp, setCurrTemp] = useState("");
  const [currHumidity, setCurrHumidity] = useState("");
  const [currLumens, setCurrLumens] = useState("");
  const [currDistance, setCurrDistance] = useState("");
  const [picDescription, setPicDescription] = useState("");
  const [displayMessage, setDisplayMessage] = useState("");





  useEffect(() => {
    socket.on('connect', () => console.log('Connected:', socket.id));
    socket.on('picture_taken', data => {
      setPictureStatus(data.message);
      setTimeout(() => setPictureStatus(""), 3000); // Clear status after 3 seconds
    });
    socket.on('temp', temp => {setCurrTemp(temp)});
    socket.on('humidity', humidity => {setCurrHumidity(humidity)});
    socket.on('light', light => {setCurrLumens(light)});
    socket.on('ultrasonic', distance => {setCurrDistance(distance)});
    socket.on('picture description',description => {setPicDescription(description)});

    return () => {
      socket.off('picture_taken');
      socket.off('temp');
      socket.off('humidity');
      socket.off('light');
      socket.off('ultrasonic');
    };
  }, []);

  function takePhoto(){
    socket.emit('take picture');
  }

  function playAudio(){
    const audio = new Audio('/description.wav?ts=${Date.now()}');
    audio.play();
  }
  function handleMessage(message){
    setDisplayMessage(message);
    socket.emit('display request', displayMessage);
  }

  return (
    <div className="App">
      <h1 className="App-title">Welcome to the Operator's Control Panel</h1>
      <img src={downloaded_image} alt="My Logo" style={{ width: '200px' }} />
      <button onClick={takePhoto}>Click to Take a Photo</button>
      <h2>Description: {picDescription}</h2>
      <button onClick={playAudio}>Audio Description</button>
       <div style={{ padding: '1rem' }}>
        <textarea
          placeholder="Type something here..."
          value={displayMessage}
          onChange={(e) => setDisplayMessage(e.target.value)}
          rows={4}
          cols={50}
          style={{ marginBottom: '1rem' }}
        />
        <button onClick = {handleMessage}>Submit</button>
        </div>
    
      {/* Floating Info Boxes */}
      <div
        className="info-box"
        style={{ top: "100px", left: "50px" }}
      >
         Temperature: {currTemp}
      </div>

      <div
        className="info-box"
        style={{ top: "100px", right: "50px" }}
      >
         Light: {currLumens}
      </div>

      <div
        className="info-box"
        style={{ bottom: "100px", left: "50px" }}
      >
        Humidity: {currHumidity}
      </div>

      <div
        className="info-box"
        style={{ bottom: "100px", right: "50px" }}
      >
         Distance: {currDistance}
      </div>
    </div>
    );
}

export default App;
