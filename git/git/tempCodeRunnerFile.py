import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set up the rate of speech (optional)
engine.setProperty('rate', 150)

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for a command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        command = ""
        
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand that.")
        except sr.RequestError:
            print("Sorry, the service is down.")
        
        return command.lower()

# Function to handle commands
def respond(command):
    if 'hello' in command:
        speak("Hello, how can I assist you today?")
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {time}")
    
    elif 'search' in command:
        search_query = command.replace("search", "")
        try:
            results = wikipedia.summary(search_query, sentences=2)
            speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("There are multiple results. Can you be more specific?")
        except wikipedia.exceptions.HTTPTimeoutError:
            speak("Sorry, I couldn't retrieve the information.")
    
    elif 'open' in command:
        website = command.split("open")[-1].strip()
        speak(f"Opening {website}")
        webbrowser.open(f"https://{website}")
    
    elif 'exit' in command or 'quit' in command:
        speak("Goodbye! Have a great day.")
        exit()

# Main loop for continuous listening and responding
def main():
    speak("I am your voice assistant. How can I help you?")
    
    while True:
        command = listen()
        respond(command)

# Start the assistant
if __name__ == "__main__":
    main()
