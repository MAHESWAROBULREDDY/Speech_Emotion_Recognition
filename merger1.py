from os import path
from pydub import AudioSegment
sound1 = AudioSegment.from_wav("D:\Speech_Emotion_Recognition\Project\TESS Toronto emotional speech set data\OAF_happy\OAF_back_happy.wav")
sound2 = AudioSegment.from_wav("D:\Speech_Emotion_Recognition\Project\TESS Toronto emotional speech set data\OAF_happy\OAF_back_happy.wav")

combined_sounds = sound1 + sound2

combined_sounds.export("D:/Speech_Emotion_Recognition/Project/App_SpeechEmotionRecognition/Audio1.mp3", format="mp3")