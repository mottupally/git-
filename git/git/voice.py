import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import os
import random

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set speech rate (optional)
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
            command = recognizer.recognize_google(audio, timeout=10)
            print(f"You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

        return command.lower()

# Function to handle commands
def respond(command):
    if 'hello' in command:
        speak("Hello, how can I assist you today?")
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {time}")
    
    elif 'search' in command:
        search_query = command.replace("search", "").strip()
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
    
    elif 'play music' in command:
        speak("Playing some music for you.")
        play_music()

    elif 'exit' in command or 'quit' in command:
        speak("Goodbye! Have a great day.")
        exit()

# Function to play music
def play_music():
    # Music file paths (you can replace this with actual paths to local music files)
    music_folder = "C:/Users/Dell/Music"  # Update with the path to your music folder
    music_files = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]
    
    if music_files:
        music_file = random.choice(music_files)
        music_path = os.path.join(music_folder, music_file)
        os.startfile(music_path)  # Open the music file with the default music player
        speak(f"Now playing {music_file}")
    else:
        speak("Sorry, I couldn't find any music in your folder.")

# Main loop for continuous listening and responding
def main():
    speak("I am your voice assistant. How can I help you?")
    
    while True:
        command = listen()
        respond(command)

# Start the assistant
if __name__ == "__main__":
    main()
