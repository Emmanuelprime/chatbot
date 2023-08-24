import speech_recognition as sr
import subprocess
import io
from pydub import AudioSegment
from pydub.playback import play


def say(text):
    voice="en_US/m-ailabs_low"
    mimic_path = "/home/prime/.local/bin/mimic3"  # Replace with the actual path to mimic3_tts
    completed_process = subprocess.run([mimic_path, "--stdout","--voice",voice,text], stdout=subprocess.PIPE)
    audio_data = completed_process.stdout
    audio_segment = AudioSegment.from_wav(io.BytesIO(audio_data))
    play(audio_segment)
    #return audio_segment

def take_CMD_MIC():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening......")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing......")
            query = recognizer.recognize_google(audio,language="en-NG")
            print(query)
            say(query)
        except Exception as e:
            print(e)
            say("say that again please...")
            return "None"
        return query
    

if __name__ == "__main__":
    take_CMD_MIC()