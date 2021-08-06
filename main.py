from subprocess import run
import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[13].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk("I am Harry, what can I help you with")


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'harry' in command:
                command = command.replace('harry', '')
                print(command)

    except:
        pass
    return command


def run_harry():
    command = take_command()
    while 'turn off please' not in command:
        if 'play' in command:
            song = command.replace('play', '')
            print(song)
            talk('playing' + song)
            pywhatkit.playonyt(song)
            command = take_command()
        elif 'time' and 'what' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(" Right now is " + time)
            command = take_command()
        elif 'search for' in command:
            object = command.replace('search for', '')
            info = wikipedia.summary(object, 1)
            talk(info)
            command = take_command()


run_harry()
