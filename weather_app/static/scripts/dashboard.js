const apiUrl = "/weather"; // Flask endpoint to fetch weather data

// alert('JavaScript is working!');


const searchBox = document.querySelector(".search input");
const searchBtn = document.querySelector(".search button");
const weatherIcon = document.querySelector(".weather-icon");
let currentCity = ""; // To track the current city for auto-refresh

// Function to check weather and update UI
async function checkWeather(city) {
    try {

        const response = await fetch(`${apiUrl}?city=${city}`);
        if (!response.ok) {
            throw new Error("City not found");
        }

        const data = await response.json();

        // Update weather information in the UI
        document.querySelector(".city").innerHTML = data.name;
        document.querySelector(".temp").innerHTML = Math.round(data.main.temp) + "°C";
        document.querySelector(".humidity").innerHTML = data.main.humidity + "%";
        document.querySelector(".wind").innerHTML = data.wind.speed + " km/hr";

        // Dynamically change weather icon based on weather condition
        const weatherIcons = {
            Clouds: "{{ url_for('static', filename='images/clouds.png') }}",
            Clear: "{{ url_for('static', filename='images/clear.png') }}",
            Rain: "{{ url_for('static', filename='images/rain.png') }}",
            Drizzle: "{{ url_for('static', filename='images/drizzle.png') }}",
            Mist: "{{ url_for('static', filename='images/mist.png') }}",
            Snow: "{{ url_for('static', filename='images/snow.png') }}",
            Thunderstorm: "{{ url_for('static', filename='images/thunder.png') }}",
            default: "{{ url_for('static', filename='images/search.png') }}",
        };

        weatherIcon.src = weatherIcons[data.weather[-1].main] || weatherIcons.default;

        // Display weather card and hide error
        document.querySelector(".weather").style.display = "block";
        document.querySelector(".error").style.display = "none";
    } catch (error) {
        // Display error message
        document.querySelector(".error").style.display = "block";
        document.querySelector(".weather").style.display = "none";
    }
}

// Event listener for search button
searchBtn.addEventListener("click", () => {
    const city = searchBox.value.trim();
    if (city) {
        currentCity = city; // Update current city for auto-refresh
        checkWeather(city); // Fetch weather immediately
    } else {
        alert("Please enter a city name.");
    }
});

// Auto-refresh weather data every 1 seconds
setInterval(() => {
    if (currentCity) {
        checkWeather(currentCity);
    }
}, 10000);

// setInterval(checkWeather(city), 1999);



searchBtn.addEventListener("click", () => {
    const city = searchBox.value.trim();
    if (city) {
        currentCity = city; // Update current city for auto-refresh
        checkWeather(city); // Fetch weather immediately
    } else {
        alert("Please enter a city name.");
    }
});
document.getElementById('log-btn').addEventListener('click', function () {
    const place = document.getElementById('place-input').value;

    if (place.trim() === "") {
        alert("Please enter a place name.");
        return;
    }

    // Replace with the actual weather data (for demo purposes)
    const weatherData = {
        city: place,
        temperature: 24.0, // Example data
        timestamp: new Date().toISOString(),
    };

    // Send the weather data to the backend
    fetch('/log_weather', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(weatherData),
    })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert(data.message); // Display success message
            } else {
                alert("Error logging weather data.");
            }
        })
        .catch(error => console.error('Error:', error));
});