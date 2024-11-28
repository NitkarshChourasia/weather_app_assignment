const apiUrl = "/weather"; // Flask endpoint

const searchBox = document.querySelector(".search input");
const searchBtn = document.querySelector(".search button");
const weatherIcon = document.querySelector(".weather-icon");
let currentCity = ""; // Track current city for auto-refresh

async function checkWeather(city) {
    try {
        const response = await fetch(`${apiUrl}?city=${city}`);
        console.log(`Response status: ${response.status}`);

        if (!response.ok) throw new Error("City not found");

        const data = await response.json();
        console.log("Fetched data:", data);

        // Update weather UI
        document.querySelector(".city").innerHTML = data.name;
        document.querySelector(".temp").innerHTML = Math.round(data.main.temp) + "°C";
        document.querySelector(".humidity").innerHTML = data.main.humidity + "%";
        document.querySelector(".wind").innerHTML = data.wind.speed + " km/h";

        const weatherIcon = document.querySelector(".weather-icon");

        // Dynamically change the weather icon
        const weatherCondition = data.weather[0].main;

        let iconSrc = "/static/images/search.png"; // Default icon

        switch (weatherCondition) {
            case "Clouds":
                iconSrc = "/static/images/clouds.png";
                break;
            case "Clear":
                iconSrc = "/static/images/clear.png";
                break;
            case "Rain":
                iconSrc = "/static/images/rain.png";
                break;
            case "Drizzle":
                iconSrc = "/static/images/drizzle.png";
                break;
            case "Mist":
                iconSrc = "/static/images/mist.png";
                break;
            case "Snow":
                iconSrc = "/static/images/snow.png";
                break;
            case "Thunderstorm":
                iconSrc = "/static/images/thunder.png";
                break;
            default:
                iconSrc = "/static/images/search.png"; // If no match
                break;
        }

        // Set the correct icon
        weatherIcon.src = iconSrc;

    } catch (error) {
        console.error("Error fetching weather:", error);
        document.querySelector(".error").style.display = "block";
        document.querySelector(".weather").style.display = "none";
    }
}


// Search button event
searchBtn.addEventListener("click", () => {
    const city = searchBox.value.trim();
    if (city) {
        currentCity = city;
        checkWeather(city);
    } else {
        alert("Please enter a city name.");
    }
});

// Auto-refresh every 10 minutes
setInterval(() => {
    if (currentCity) {
        checkWeather(currentCity);
    }
}, 600000);

// Log weather event
document.getElementById("log-btn").addEventListener("click", async () => {
    const place = document.getElementById("place-input").value.trim();
    if (!place) {
        alert("Please enter a place name.");
        return;
    }

    // Create the weather data object
    const weatherData = {
        city: place,
        temperature: 25, // You can dynamically fetch this or use a placeholder
        pressure: 1013, // Example data
        humidity: 60,  // Example data
        wind_speed: 5, // Example data
        wind_degree: 180 // Example data
    };
    try {
        const response = await fetch('/add_log_weather', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(weatherData)
        });
        const data = await response.json();
        if (response.ok) {
            alert(data.message || "Weather data logged successfully");
        } else {
            alert(data.error || "Error logging weather data");
        }
    } catch (error) {
        console.error("Error:", error);
        alert("There was an error processing your request.");
    }


});