# import subprocess
# def speak(text):
#     subprocess.run(["espeak", text])

# speak("Hello, can you hear me?")

import pyttsx3

engine = pyttsx3.init('espeak')  # Ensure espeak is used
engine.setProperty('rate', 150)   # Adjust speed
engine.setProperty('volume', 1.0) # Set volume
voices = engine.getProperty('voices')

# Select English (Great Britain) voice
engine.setProperty('voice', voices[28].id)  # English (America)
  # Try 'english' directly

engine.say("Hello, testing voice output.")
engine.runAndWait()

