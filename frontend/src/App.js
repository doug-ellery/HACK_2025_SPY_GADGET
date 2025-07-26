import React, { useState, useEffect } from "react";
import io from 'socket.io-client';
import './App.css';

const socket = io('http://localhost:8000');

function App() {
  const [pictureStatus, setPictureStatus] = useState("");
  const [currTemp, setCurrTemp] = useState(0);
  const [currHumidity, setCurrHumidity] = useState(0);
  const [currLumens, setCurrLumens] = useState(0);
  const [currDistance, setCurrDistance] = useState(0);
  const [picDescription, setPicDescription] = useState("");





  useEffect(() => {
    socket.on('connect', () => console.log('Connected:', socket.id));
    socket.on('picture_taken', data => {
      setPictureStatus(data.message);
      setTimeout(() => setPictureStatus(""), 3000); // Clear status after 3 seconds
    });
    return () => {
      socket.off('picture_taken');
    };
  }, []);

  function takePhoto(){
    socket.emit('picture request');
    socket.on('picture taken',description => {setPicDescription(description)});
  }

  function getTemp(){
    socket.emit('temp request')
    socket.on('temp', temp => {setCurrTemp(temp) });
  }

  function getHumidity(){
    socket.emit('humidity request');
    socket.on('humidity', humidity => {setCurrHumidity(humidity)});
  }

  function getLight(){
    socket.emit('light request');
    socket.on('light', light => {setCurrLumens(light)});
  }

  function getDistance(){
    socket.emit('distance request');
    socket.on('distance', distance => {setCurrDistance(distance)});
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
      <button onClick = {getTemp}>Click to Get the Temperature</button>
      <br></br>
      <h>Temperature: {currTemp}</h>
      <br></br>
      <br></br>
      <br></br>
      <button onClick = {getHumidity}>Click to Get the Humidity</button>
      <br></br>
      <h>Humidity: {currHumidity}</h>
      <br></br>
      <br></br>
      <br></br>
      <button onClick = {getLight}>Click to Get the Light</button>
      <br></br>
      <h>Light: {currLumens}</h>
      <br></br>
      <br></br>
      <br></br>
      <button onClick = {getDistance}>Click to Get the Distance</button>
      <br></br>
      <h>Distance: {currDistance}</h>
    </div>
  );
}

export default App;
