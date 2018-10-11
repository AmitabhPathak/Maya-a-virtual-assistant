import src.SpeechRecognition.text
import src.text2speech.speech
import src.wiki.wikipedia
import src.wolframalpha.wolf
while True:
    query=src.SpeechRecognition.text.ask()
    try:
        answer=src.wolframalpha.wolf.calculate(query)
    except:
        answer=src.wiki.wikipedia.find(query)
    src.text2speech.speech.speak(answer)
