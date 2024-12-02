const button = document.getElementById("search-btn");

button.addEventListener("click", async () => {

    // Get the value of the input field
    const input = document.getElementById('city').value.trim();
    if (!input) {
        alert("Please enter a city name");
    } else {

        checkWeather(input);
    }
    // Display the input in the result div
});

async function checkWeather(city) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/weather?city=${city}`);
        console.log(`Response status: ${response.status}`);

        if (!response.ok) throw new Error(`Error: ${response.status}`);

        const data = await response.json();
        console.log("Fetched data:", data);

        // Correctly updating DOM elements with the fetched data
        document.getElementById("country-name").textContent = data.country_name;
        document.getElementById("city-name").textContent = `Weather in ${data.city_name}`;
        document.getElementById("weather-condition").textContent = data.weather_condition;
        document.getElementById("temperature").textContent = `${data.temp}°C`;
        document.getElementById("pressure").textContent = `${data.pressure} hPa`;
        document.getElementById("humidity").textContent = `${data.humidity}%`;
        document.getElementById("wind-speed").textContent = `${data.wind_speed} m/s`;
        document.getElementById("wind-degree").textContent = `${data.wind_degree}°`;

    } catch (error) {
        console.error("Error:", error);
        document.getElementById("info-title").textContent = "Error fetching data";
    }
}