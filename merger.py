from os import path
from pydub import AudioSegment

sound1 = AudioSegment.from_wav("D:/Speech_Emotion_Recognition/Project/TESS Toronto emotional speech set data/OAF_happy/OAF_puff_happy.wav")
sound2 = AudioSegment.from_wav("D:/Speech_Emotion_Recognition/Project/TESS Toronto emotional speech set data/OAF_happy/OAF_calm_happy.wav")
sound3 = AudioSegment.from_wav("D:/Speech_Emotion_Recognition/Project/TESS Toronto emotional speech set data/OAF_happy/OAF_yearn_happy.wav")
sound4 = AudioSegment.from_wav("D:/Speech_Emotion_Recognition/Project/TESS Toronto emotional speech set data/OAF_happy/OAF_witch_happy.wav") 
sound5 = AudioSegment.from_wav("D:/Speech_Emotion_Recognition/Project/TESS Toronto emotional speech set data/OAF_happy/OAF_soap_happy.wav")
sound6 = AudioSegment.from_wav("D:/Speech_Emotion_Recognition/Project/TESS Toronto emotional speech set data/OAF_happy/OAF_red_happy.wav")
sound7 = AudioSegment.from_wav("D:/Speech_Emotion_Recognition/Project/TESS Toronto emotional speech set data/OAF_happy/OAF_back_happy.wav")
sound8 = AudioSegment.from_wav("D:/Speech_Emotion_Recognition/Project/TESS Toronto emotional speech set data/OAF_happy/OAF_beg_happy.wav")
sound9 = AudioSegment.from_wav("D:/Speech_Emotion_Recognition/Project/TESS Toronto emotional speech set data/OAF_happy/OAF_puff_happy.wav")
sound10 = AudioSegment.from_wav("D:/Speech_Emotion_Recognition/Project/TESS Toronto emotional speech set data/OAF_happy/OAF_calm_happy.wav")
sound11= AudioSegment.from_wav("D:/Speech_Emotion_Recognition/Project/TESS Toronto emotional speech set data/OAF_happy/OAF_yearn_happy.wav")
sound12 = AudioSegment.from_wav("D:/Speech_Emotion_Recognition/Project/TESS Toronto emotional speech set data/OAF_happy/OAF_witch_happy.wav") 
sound13 = AudioSegment.from_wav("D:/Speech_Emotion_Recognition/Project/TESS Toronto emotional speech set data/OAF_happy/OAF_soap_happy.wav")
sound14 = AudioSegment.from_wav("D:/Speech_Emotion_Recognition/Project/TESS Toronto emotional speech set data/OAF_happy/OAF_red_happy.wav")
sound15 = AudioSegment.from_wav("D:/Speech_Emotion_Recognition/Project/TESS Toronto emotional speech set data/OAF_happy/OAF_back_happy.wav")
sound16 = AudioSegment.from_wav("D:/Speech_Emotion_Recognition/Project/TESS Toronto emotional speech set data/OAF_happy/OAF_beg_happy.wav")
combined_sounds = sound1 + sound2 + sound3 +  sound4 +sound5 +sound6 +sound7 +sound8 +sound9 + sound10 + sound11 +  sound12 +sound13 +sound14 +sound15 +sound16
#combined_sounds = sound1 + sound2 
combined_sounds.export("D:/Speech_Emotion_Recognition/Project/App_SpeechEmotionRecognition/Audio1.mp3", format="mp3")