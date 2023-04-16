import pyttsx3
friend = pyttsx3.init()
speech = input("Type Something:")
friend.say(speech)
friend.runAndWait()
