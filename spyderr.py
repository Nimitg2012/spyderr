import speech_recognition as sr
import pyttsx3
import time
import random
import requests
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Try again.")
        return ""
    except sr.RequestError:
        print("Speech service error.")
        return ""

def start_screen():
    print("***********************************")
    print("*   Welcome to SPYDERR! 🕷️    *")
    print("*  Your Spider-Themed Assistant   *")
    print("***********************************")
    time.sleep(1)
    speak("Hello! I am SPYDERR. How can I assist you today?")

def tell_joke():
    jokes = [
        "How do you explain Inception to a programmer? VM inside VM inside VM... everything slows down!",
        "Why don’t spiders make good programmers? They prefer to spin their own web!",
        "Why did the spider visit the computer? To check its web site!"
    ]
    speak(random.choice(jokes))

def get_weather(city):
    weather_info = f"The temperature in {city} is 17°C with overcast clouds. Humidity is 77%. Wind speed is 2.06 m/s."
    speak(weather_info)

# Web search using SerpAPI
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")


def web_search(query):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY
    }
    print("DEBUG: Making request with", params)
    response = requests.get(url, params=params)
    print("DEBUG: Response code:", response.status_code)
    print("DEBUG: Response:", response.text)

    if response.status_code != 200:
        speak("There was a problem with the search service. Opening a browser instead.")
        import webbrowser
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return

    data = response.json()
    if "organic_results" in data:
        results = data["organic_results"][:3]
        speak("Here are the top results:")
        for result in results:
            speak(f"{result.get('title', 'No title')}. Link: {result.get('link', '')}")
    else:
        speak("Sorry, no results found.")
    
def image_search(query):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "tbm": "isch",
        "api_key": SERPAPI_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if "images_results" in data:
        first_image = data["images_results"][0]["original"]
        speak("Here is an image result I found.")
        print(f"Image URL: {first_image}")
    else:
        speak("Sorry, no image results found.")

def assistant_loop():
    start_screen()
    while True:
        command = listen()
        if 'goodbye' in command or 'exit' in command:
            speak("Goodbye! Have a great day!")
            break
        elif 'joke' in command:
            tell_joke()
        elif 'weather' in command:
            speak("Please tell me the city.")
            city = listen()
            get_weather(city)
        elif 'search' in command:
            speak("What would you like to search for?")
            query = listen()
            web_search(query)
        elif 'image' in command:
            speak("What image should I find?")
            query = listen()
            image_search(query)
        else:
            speak("Sorry, I didn't catch that. Can you repeat?")

if __name__ == "__main__":
    assistant_loop()
