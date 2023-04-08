import speech_recognition as sr

# create a recognizer object
r = sr.Recognizer()

# open the microphone and start recording
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# use Google Speech Recognition to convert the audio to text
try:
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
