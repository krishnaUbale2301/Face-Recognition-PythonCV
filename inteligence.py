import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("good Evening!")
    speak("I am cheetty , A vertual Assistant. Welcome to CSMSS Chhatrapati shahu college of engineering Aurangabad")
    
def takeCommand():
    # It takes microphone input from the user and returns string output    
    r = sr.Recognizer()
    with sr.Microphone()as sourse:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(sourse)
    try:
        print("Recognizinig...")   
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please.....")
        return "None"
    return query

def sendEmail(to , content): 
    server = smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    # emailID = dadusrobot001@gmail.com 
    #password = Dadusrobot001@
    server.login('yourmail@gmail.com','your password here')
    server.close()

def date():
    year = int(datetime.datetime.now().year)  
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().date)
    #day = int(datetime.datetime.now().day) 
    speak(date + month + year)  


if __name__ == "__main__":
    
    while True:
        query = takeCommand()
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentenses=4)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")    

        elif 'hellow' in query:
            speak("Hellow" + "sir")  
        elif 'namaste' in query :
            speak("Namaskar " + "sir")        
        elif 'thank you ' in query:
            speak("its my plasure" + "sir!")
        
        elif 'good morning' or 'good afternoon' or 'good evening' in query :
            speak("helow" + "sir")
            wishMe()    
        
        elif 'the time' in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is (strTime)")
        
        
        '''elif 'play music' in query :
            music_dir = 'E_drive\\ Moh_Moh'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0])) 

        elif 'email to krishna' in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "krishnaubale2301@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e :
                print(0)
                speak("Sorry sar , iam not able to send this email")'''    



