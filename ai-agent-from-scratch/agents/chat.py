from .weather import WeatherAgent

class ChatAgent:
    def __init__(self, weather_api_key):
        self.memory = []
        self.weather_agent = WeatherAgent(weather_api_key)

    def respond(self, user_input):
        self.memory.append(f"You: {user_input}")
        user_input = user_input.lower().strip()
        if user_input.startswith("weather in "):
            city = user_input[11:]
            temp = self.weather_agent.get_weather(city)
            return f"It’s {temp}°C in {city}!" if temp else "Weather unavailable."
        return "Ask me about the weather or something else!"