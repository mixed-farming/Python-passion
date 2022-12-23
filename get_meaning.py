import pyttsx3
from PyDictionary import PyDictionary

class Speaking:
    def speak(self, audio):
        # Having the initial constructor of pyttsx3
        # and having the sapi5 in it as a parameter
        engine = pyttsx3.init('sapi5')

        # Calling the getter and setter of pyttsx3
        voices = engine.getProperty('voices')

        # Method for the speaking of the assistant
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()


class My:
    def Dictionary(self):
        speak = Speaking()
        dic = PyDictionary()
        speak.speak("Which word do u want to find the meaning brother")

        # Taking the string input
        query = str(input())
        word = dic.meaning(query)
        print(len(word))

        for state in word:
            print(word[state])
            speak.speak("The meaning of the word" + query + "is" + str(word[state]))

My()
My.Dictionary(self=None)
