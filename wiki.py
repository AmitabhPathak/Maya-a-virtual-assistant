import wolframalpha
import wikipedia
import speech_recognition as sr
x=""
def ask():
    r=sr.Recognizer()
    r.energy_threshold = 2000
    with sr.Microphone() as source:
        print("say something")
        audio=r.listen(source)
    try:
        return r.recognize_google(audio)
        
    except:
        pass
while True :
    
    q=ask()
    try:
        app_id="4UJQRT-7LJEWV7WT2"
        client=wolframalpha.Client(app_id)

        res=client.query(q)
        answer=next(res.results).text
        print(answer)
    except:
        print(wikipedia.summary(q))

