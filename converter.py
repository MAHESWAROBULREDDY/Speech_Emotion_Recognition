from os import path
from pydub import AudioSegment

# files                                                                         
'''src = "transcript.mp3"
dst = "test.wav"'''
filewav = '03-01-01-01-01-01-01.wav'
filemp3 = 'Audio1.mp3'
# convert wav to mp3                                                            
sound = AudioSegment.from_wav(filewav)
sound.export(filemp3, format="mp3")


























'''import wave
import keras
import pyaudio
import pandas as pd
import numpy as np

import IPython.display as ipd
CHUNK = 1024 
FORMAT = pyaudio.paInt16 #paInt8
CHANNELS = 5
RATE = 44100 #sample rate
RECORD_SECONDS = 7
WAVE_OUTPUT_FILENAME = "audio1.wav"
#emotions=["Anger","disgust","fear","happy","Neutral", "sad", "surprise"]

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK) #buffer

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data) # 2 bytes(16 bits) per channel

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()'''