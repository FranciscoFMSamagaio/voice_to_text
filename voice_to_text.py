# pip install deep-translator
# pip install SpeechRecognition
# pip install sounddevice
# pip install numpy
# pip install scipy

import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from deep_translator import GoogleTranslator

FILENAME_FROM_MIC = "recording.WAV"
VOICE_TEXT_FILENAME = "voice_to_text_english.txt"
VOICE_TEXT_FILENAME_TRANSLATED = "voice_to_text_translated.txt"

# initialize the recognizer
r = sr.Recognizer()

def recognize_from_file(filename):
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return "Could not understand audio"
        
def recognize_from_microphone(file_to_write):
    SAMPLE_RATE=44100
    duration = 5  # seconds
    audio_recording = sd.rec(duration * SAMPLE_RATE, samplerate=SAMPLE_RATE, channels=1, dtype='int32')
    print("Recording Audio")
    sd.wait()
    print(audio_recording)
    print("Audio recording complete , Play Audio")
    sd.play(audio_recording, SAMPLE_RATE)
    sd.wait()
    print("Play Audio Complete")
    wav.write(file_to_write, SAMPLE_RATE, audio_recording)

def save_text_to_file(text, filename):
    with open(filename, 'w') as f:
        f.write(text)

def translate_file(text_from_voice, filename):
    translate = GoogleTranslator(source='english', target='french').translate_file(text_from_voice)
    with open(filename, 'w') as f:
        f.write(translate)


if __name__ == "__main__":
    recognize_from_microphone(FILENAME_FROM_MIC)
    text_from_voice = recognize_from_file(FILENAME_FROM_MIC)
    save_text_to_file(text_from_voice, VOICE_TEXT_FILENAME)
    translate_file(VOICE_TEXT_FILENAME, VOICE_TEXT_FILENAME_TRANSLATED)
