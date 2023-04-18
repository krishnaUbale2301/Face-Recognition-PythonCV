import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
#----------------face Recognition part--------------#
import cv2
import face_recognition as fr
import numpy as np
#-------------------end of module-------------------#
camera = cv2.VideoCapture(0)

Shahrukh_image = fr.load_image_file("C:/Users/hp/OneDrive/Pictures/faces/shahrukh-khan.jpg")
Shahrukh_face_encoding =fr.face_encodings(Shahrukh_image)[0]

Rutik_image = fr.load_image_file("C:/Users/hp/OneDrive/Pictures/faces/rutik.jpg")
Rutik_face_encoding =fr.face_encodings(Rutik_image)[0]

Amitabh_image = fr.load_image_file("C:/Users/hp/OneDrive/Pictures/faces/Amitabh_bachchan.jpg")
Amitabh_face_encoding =fr.face_encodings(Amitabh_image)[0]

Krishna_image = fr.load_image_file("C:/Users/hp/OneDrive/Pictures/faces/Krishna.jpg")
Krishna_face_encoding =fr.face_encodings(Krishna_image)[0]

Gosavi_sir_image = fr.load_image_file("C:/Users/hp/OneDrive/Pictures/faces/Prof_gosavi_sir.jpg")
Gosavi_sir_face_encoding =fr.face_encodings(Gosavi_sir_image)[0]

known_face_encodings = [Shahrukh_face_encoding , Rutik_face_encoding , Amitabh_face_encoding, Krishna_face_encoding, Gosavi_sir_face_encoding]
known_face_names = ["Shahrukh khan", "Rivtik Roshan" , "Amitabh Bachchan", "Krishna", "Professor Gosaavi sar"]


#------------------------------------------------
#  shift + f5 to stop 
#----------------------faces encoding is ended here-------------------------------------------------

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

def communi():
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
        speak("Hello " + name + "sar")  
    elif 'namaste' in query :
        speak("Namaskar " + name + "sar")        
    elif 'thank you ' in query:
        speak("its my plasure" + name + "sar!")
    elif 'good morning' or 'good afternoon' or 'good evening' in query :
        speak("helow" + name + "sar")
        wishMe()

if __name__ == "__main__":
    #wishMe()
    while True:
        #my face recognition is will done here -----------------------------------------
        ret, frame = camera.read()

        rgb_frame = frame[:, :, ::-1]

        face_locations = fr.face_locations(rgb_frame)
        face_encodings = fr.face_encodings(rgb_frame, face_locations)

        for(top, right, bottom, left),face_encodings in zip(face_locations, face_encodings):
        
                matches = fr.compare_faces(known_face_encodings, face_encodings)

                name = "Unknown"
                #qspeak(name)
                print(name)

                face_distance = fr.face_distance(known_face_encodings, face_encodings)
    
                best_match_index = np.argmin(face_distance)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    speak("hello" + name + "saar")
                    print(name)
                    wishMe()
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
                            speak("Hello " + name + "sar")  
                        elif 'namaste' in query :
                            speak("Namaskar " + name + "sar")        
                        elif 'thank you ' in query:
                            speak("its my plasure" + name + "sar!")
                        elif 'good morning' or 'good afternoon' or 'good evening' in query :
                            speak("helow" + name + "sar")
                            wishMe()
                        break        
                    #speak(name + "sar")
                cv2.rectangle(frame, (left, top), (right, bottom), (255,255,0),2)   
                cv2.rectangle(frame, (left, bottom -35), (right, bottom),(255,255,0),cv2.FILLED)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, name, (left +6, bottom - 6), font, 1.0, (0,0,255),1)

                #-----------------------end of face recognization---------------------------      


        cv2.imshow('Webcam', frame)  

        if cv2.waitKey(0) & 0xFF == ord('q'):
                break

    camera.release()
    cv2.destroyAllWindows()
    
    