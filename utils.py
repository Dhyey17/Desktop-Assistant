import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)


def speak(prompt):
    engine.say(prompt)
    engine.runAndWait()


def get_prompt():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic, duration=1)
        audio = r.listen(mic)
        try:
            query = r.recognize_google(audio)
            print(f"user said: {query}")
            return query
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand the audio. Please try again."
        except sr.RequestError:
            return "Could not request results, check your internet connection."
