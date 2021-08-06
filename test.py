import pyttsx3
converter = pyttsx3.init()

voices = converter.getProperty('voices')
i = 0
for voice in voices:
    # to get the info. about various voices in our PC
    print(i)
    i += 1
    print("Voice:")
    print("ID: %s" % voice.id)
    print("Name: %s" % voice.name)
    print("Age: %s" % voice.age)
    print("Gender: %s" % voice.gender)
    print("Languages Known: %s" % voice.languages)
