#Work-in-Progress 

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb

engine = pyttsx3.init()


def  speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(" the current time is, ")
    speak(Time)
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(" the current date  is, ")
    
    speak(day)
    speak(month)
    speak(year)



def greetings():
    speak("welcome back Nithin.")
    
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("good morning , sir!")
    elif hour>=12 and hour<18:
        speak("good afternoon ,sir")
        
    elif hour>=18 and hour<24:
        speak("good evening ,sir")


    else:
        speak("good night sir")



    speak("Chris at your service. please tell me how can i help you")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        r.adjust_for_ambient_noise(source, duration=2) 
        print("Listening....")
        r.pause_threshold =1
        audio = r.listen(source)


    try:
        print("Recognizing....")
        query = r.recognize_google(audio ,language = 'en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("sorry can you repeat your self")
        return "none"

    return query




if __name__ == "__main__":
    # greetings()
    while True:
        query = take_command().lower() 

        if 'time ' in query:
            time()
        elif 'date' in query:
            date()

        elif 'wikipedia' in  query:
            speak("searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak(result)

        elif 'search ' in query:
            speak("What should i search..?")
            chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

            search = take_command().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'offline' in query:
            quit()
