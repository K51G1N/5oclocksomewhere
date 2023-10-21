// fetchRandomLocation.js
const fetchRandomLocation = async (setSelectedLocation, setSelectedTime) => {
  try {
    const response = await fetch('https://frozen-basin-02979-fb503ec913dc.herokuapp.com/api/getRandomLocation');
    if (response.ok) {
      const data = await response.json();
      setSelectedLocation(data.location);
      setSelectedTime(data.time);
    } else {
      // Log the error response
      console.error('API request failed with status:', response.status);
      const text = await response.text();
      console.error('API response:', text);
    }
  } catch (error) {
    console.error('API request failed:', error);
  }
};

export default fetchRandomLocation;