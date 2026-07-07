# 🌤️ Django Weather Dashboard

A responsive, real-time weather dashboard web application built using the Django framework. The application allows users to dynamically search for any city globally and receive up-to-date weather metrics including temperature, current weather conditions, wind speed, humidity, and UV Index via an external API integration.

---

## 🛠️ Tools & Technologies Used

### Backend & Core Frameworks
* **Python**: Core programming language.
* **Django**: High-level Python Web framework used for routing, database management, and architecture.
* **Requests (Python Library)**: Used to make asynchronous HTTP GET requests to fetch live third-party API weather data.

### Frontend & Styling
* **HTML5**: Structured layout for the user interface dashboard.
* **Tailwind CSS (via CDN)**: A utility-first CSS framework utilized for modern, dark-themed UI styling, responsive grid systems, and dashboard components.

### External Services & Tooling
* **WeatherAPI**: A third-party data provider used to pull live, real-time meteorological JSON information.
* **Git & GitHub**: Version control system used for tracking code changes and hosting the repository.
* **Python-dotenv** *(Optional/Best Practice)*: Integrated to store secret credentials (like the API Key) in an isolated `.env` environment file to avoid public exposure.

---

## 📂 Project Architecture: What is Used Where?

The system is configured in a modular pattern layout following standard Django architecture:

```text
weather_project/
│
├── .gitignore           # Specifies files/folders untracked by Git (e.g., env, .env, db.sqlite3)
├── manage.py            # Main Django administrative execution script
├── db.sqlite3           # Core application database storing built-in tables (auth_user)
│
├── weather/             # Root Configuration & Core App Directory
│   ├── settings.py      # Core settings (Registered global app templates array configuration)
│   ├── urls.py          # Application routing; maps the '/weather/' path pattern to the view
│   ├── views.py         # App logic; processes input requests, executes API calls, renders response
│   │
│   └── templates/       # Dedicated User Interface layout directory
│       └── home.html    # The dashboard frontend view constructed with Tailwind CSS components
