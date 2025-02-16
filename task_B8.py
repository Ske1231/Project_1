import speech_recognition as sr
from pydub import AudioSegment
import os

# Paths
mp3_file = "C:\\data\\audio.mp3"
wav_file = "C:\\data\\audio.wav"

# Convert MP3 to WAV
audio = AudioSegment.from_mp3(mp3_file)
audio.export(wav_file, format="wav")

# Initialize recognizer
recognizer = sr.Recognizer()

# Process WAV file
with sr.AudioFile(wav_file) as source:
    audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        print("Transcription:", text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")

# Optional: Delete WAV file after processing
os.remove(wav_file)

