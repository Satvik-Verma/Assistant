import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes

listener = sr.Recognizer()
Jarvis = pyttsx3.init()
voices = Jarvis.getProperty('voices')
Jarvis.setProperty('voice', voices[1].id)


def speak(text):
    Jarvis.say(text)
    Jarvis.runAndWait()


def user_command():
    try:
        print('listening...')
        with sr.Microphone() as source:
            voice = listener.listen(source, timeout=1, phrase_time_limit=10)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')

    except:
        pass
    return command


def run():
    command = user_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)
    elif 'joke' in command:
        command_joke = pyjokes.get_joke()
        speak('Here\'s a good joke.. ' '   '+ command_joke)



while True:
    run()
