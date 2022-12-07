import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Jarvis Asistanı: Merhaba, nasıl yardımcı olabilirim?")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("Jarvis Asistanı: Sizin dediğiniz: " + text)
except:
    print("Jarvis Asistanı: Özür dilerim, anlayamadım.")

if "nasıl gidiyor" in text:
    print("Jarvis Asistanı: İyiyim, teşekkür ederim.")
elif "ne zaman" in text:
    print("Jarvis Asistanı: Şu an " + str(datetime.datetime.now()))
elif "nerede" in text:
    webbrowser.open("https://www.google.com/maps/place/" + text)
