from speech_recognition import AudioFile, Recognizer
from nltk.sentiment import SentimentIntensityAnalyzer

rec = Recognizer()

with AudioFile("input/chile.wav") as audio_file:
    audio = rec.record(audio_file)

text = rec.recognize_google(audio)

analyzer = SentimentIntensityAnalyzer()
score = analyzer.polarity_scores(text)

if score["compound"] > 0:
    print("Positive")
else:
    print("Negative")
