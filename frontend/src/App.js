import React, { useState, useEffect } from "react";
import io from 'socket.io-client';
import './App.css';

const socket = io('http://localhost:8000');

function App() {
  const [pictureStatus, setPictureStatus] = useState("");
  const [currTemp, setCurrTemp] = useState("");
  const [currHumidity, setCurrHumidity] = useState("");
  const [currLumens, setCurrLumens] = useState("");
  const [currDistance, setCurrDistance] = useState("");
  const [picDescription, setPicDescription] = useState("");





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

    return () => {
      socket.off('picture_taken');
      socket.off('temp');
      socket.off('humidity');
      socket.off('light');
      socket.off('ultrasonic');
    };
  }, []);

  function takePhoto(){
    socket.emit('picture request');
    socket.on('picture taken',description => {setPicDescription(description)});
    
  }

  return (
    <div className="App">
      <br></br>
      <br></br>
      <br></br>
      <h className = "App-title">Welcome to the Operator's Control Panel</h>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <button /*onClick = {takePhoto}*/>Click to Take a Photo</button>
      <br></br>
      <h>Description: {picDescription}</h>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <h>Temperature: {currTemp}</h>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <h>Humidity: {currHumidity}</h>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <h>Light: {currLumens}</h>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <h>Distance: {currDistance}</h>
    </div>
  );
}

export default App;
