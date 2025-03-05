
from playsound import playsound
import os
import eel

@eel.expose 
def playAssistantSound():
    music_dir = "www/assests/audio/start_sound.mp3"


    if not os.path.exists(music_dir):
        print("Error: Audio file not found:", music_dir)
    else:
        print("Playing:", music_dir)
        playsound(music_dir)


