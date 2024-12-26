import pyttsx3
import speech_recognition as sr
import datetime
import wikipediaapi
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#define the audio 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#define greetings (goodmorning/goodafternoon/goodevening/goodnight according to time)
def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    elif hour>=18 and hour<22:
        speak("Good Evening")    
    else:
        speak("Good Night!")

    speak("Namaste iam Gnana, how may i help you")
    
#define command to assitance 
def command():
    mic =sr.Recognizer()
    with sr.Microphone()as source:
        print("listening...")
        mic.pause_threshold = 1
        audio = mic.listen(source)
    
    try:
        print("Recognizing...")
        query = mic.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Can you please repeat that again...")
        speak("Can you please try again....")
        return "None"
    return query

if __name__== "__main__":
    greeting()
    while True:
        query = command().lower()


#executing task base on command
        if 'hello' in query:
            speak('Hello Dear, How i can answer you?')
            
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...?')
            query = query.replace("wikipedia","")
            results = wikipediaapi.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
                
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'play music' in query:
            music_dir = "C:\\Users\\DELL\\Music\\playlists"
            songs = os.listdir(music_dir) 
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'get time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Current Time is {strTime}")
            
        elif 'get date' in query:
            strdate = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"The Current Time is {strdate}")
            
        elif 'open code' in query:
            codepath = "c:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            
        elif "exit" or "bye" in query:
            speak("Goodbye! Have a great day.")
            quit()