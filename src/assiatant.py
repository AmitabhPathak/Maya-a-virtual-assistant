import SpeechRecognition.text
import text2speech.speech
import wiki.wikipedia
import wolframalpha.wolf
while True:
    query=SpeechRecognition.text.ask()
    try:
        answer=wolframalpha.wolf.calculate(query)
    except:
        answer=wiki.wikipedia.find(query)
    text2speech.speech.speak(answer)
