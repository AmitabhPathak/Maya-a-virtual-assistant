import speech_recognition as sr
def ask():
    r=sr.Recognizer()
    r.energy_threshold = 2000
    with sr.Microphone() as source:
        print("say something")
        audio=r.listen(source)
    try:
        result=r.recognize_google(audio)
        print(result)
        return result
        
    except:
        pass
