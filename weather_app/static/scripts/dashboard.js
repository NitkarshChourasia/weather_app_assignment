const button = document.getElementById("search-btn");
document.getElementById("weather-info").style.display = "none";

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

const add_log = document.getElementById("log-btn");
add_log.addEventListener("click", async () => {
    const log_city = document.getElementById('city').value.trim();
    if (!log_city) {
        alert("Please enter a city name");
    } else {
        postLog(log_city);
    }
})

async function postLog(city) {
    const response = await fetch(`http://127.0.0.1:5000/add_log_weather?city=${city}`);
alert("Log added successfully");
    console.log(`Response status: ${response.status}`);
}


async function checkWeather(city) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/weather?city=${city}`);
        console.log(`Response status: ${response.status}`);

        if (!response.ok) throw new Error(`Error: ${response.status}`);

        const data = await response.json();
        console.log("Fetched data:", data);

        // Correctly updating DOM elements with the fetched data
        document.getElementById("country-name").textContent = data.country_name;
        document.getElementById("city-name").textContent = data.city_name;
        document.getElementById("weather-condition").textContent = data.weather_condition;
        document.getElementById("temperature").textContent = `${data.temp}°C`;
        document.getElementById("pressure").textContent = `${data.pressure} hPa`;
        document.getElementById("humidity").textContent = `${data.humidity}%`;
        document.getElementById("wind-speed").textContent = `${data.wind_speed} m/s`;
        document.getElementById("wind-degree").textContent = `${data.wind_degree}°`;
        document.getElementById("weather-info").style.display = "block";

    } catch (error) {
        console.error("Error:", error);
        document.getElementById("info-title").textContent = "Error fetching data";
    }
}