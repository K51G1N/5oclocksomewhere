import React, { useState, useEffect, useRef } from 'react';
import fetchRandomLocation from './fetchRandomLocation'; // Adjust the import path as needed
import './App.css';

function App() {
  const [selectedLocation, setSelectedLocation] = useState('');
  const [selectedTime, setSelectedTime] = useState('');
  const isInitialRender = useRef(true);

  const handleFetchRandomLocation = () => {
    fetchRandomLocation(setSelectedLocation, setSelectedTime);
  };

  useEffect(() => {
    if (isInitialRender.current) {
      isInitialRender.current = false;
    } else {
      handleFetchRandomLocation();
    }
  }, []);

  return (
    <div className="App">
      <h1>It's 5 o'clock Somewhere in the World!</h1>
      <div>
        <p>{selectedLocation}</p>
        <p>Time: {selectedTime}</p>
      </div>
      <button onClick={handleFetchRandomLocation}>Get Random Location</button>
    </div>
  );
}

export default App;
