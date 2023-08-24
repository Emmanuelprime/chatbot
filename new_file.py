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
    return audio_segment

if __name__ == "__main__":
    input_text = "My name is prime how can i help you?"

    audio_segment = say(input_text)
    play(audio_segment)
