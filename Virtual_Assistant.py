import speech_recognition as sr
import pyttsx3
import pywhatkit
import sys
import datetime
import wikipedia
import pyjokes
import webbrowser

from logging import exception

engine = pyttsx3.init()                         
engine.setProperty('rate',150)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
recognizer = sr.Recognizer()

def say(text):                                  
    engine.say(text)
    engine.runAndWait()

def run_va():                                   
    with sr.Microphone() as source:    
        recognizer.adjust_for_ambient_noise(source,duration=1)
        print(" \n Yes ")
        print("Listening...")
        say('Listening')
        audio = recognizer.listen(source)

    try :
        command = recognizer.recognize_google(audio,language='en-in')
        command = command.lower()
        
        if 'hello' in command :
            print("Hi, how can I help you ?")
            say("Hi, how can I help you ?")

        elif 'can you do' in command :
            print('i can tell you a joke, search on wikipedia, tell date and time,find your location, locate area on map, open different websites like instagram, youtube,gmail, git hub, stack overflow and searches on google')
            say('i can tell you a joke, search on wikipedia, tell date and time,find your location, locate area on map, open different websites like instagram, youtube,gmail, git hub, stack overflow and searches on google')

        elif 'play' in command :
            song = command.replace('play','')
            print('playing'+song)
            say('playing'+song)    
            pywhatkit.playonyt(song)

        elif 'date and time' in command :
            today = datetime.date.today()
            time = datetime.datetime.now().strftime('%I:%M %p')
            d2 = today.strftime("%B %d, %Y")
            print("Today's Date is ", d2, 'Current time is', time)
            say('Today is : '+ d2)
            say('and current time is '+ time)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('It is' +time)
            say('It is')
            say(time)   

        elif 'date' in command:
            today = datetime.date.today()
            print("Today's date:", today)
            d2 = today.strftime("%B %d, %Y")
            print("It is ", d2)
            say('It is')
            say(d2)

        elif 'tell me about' in command:
            name = command.replace('tell me about' , '')
            answer = wikipedia.summary(name, 2)
            print(answer)
            say(answer)    

        elif 'wikipedia' in command:
            name = command.replace('wikipedia' , '')
            answer = wikipedia.summary(name, 2)
            print(answer)
            say(answer)

        elif 'google' in command :
            search = 'https://www.google.com/search?q='+command
            print(' This is what i found on the google..')
            say('searching... This is what i found on the google..')
            webbrowser.open(search)
        
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            say(joke)

        elif "my location" in command:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            say("As per Google maps, you must be near")

        elif 'on map' in command :
            say('locating ...')
            loc = command.split(" ")
            print(loc[1])
            url = 'https://google.nl/maps/place/'+loc[1] +'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc[1])
            say('Here is the location of '+loc[1]) 

        elif 'location of' in command :
            say('locating ...')
            loc = command.replace('find location of', '')
            url = 'https://google.nl/maps/place/'+loc+'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc)
            say('Here is the location of '+loc)

        elif 'open google' in command :
            print('opening google ...')
            say('opening google..')
            webbrowser.open_new('https://www.google.co.in/')

        elif 'open gmail' in command :
            print('opening gmail ...')
            say('opening gmail..')
            webbrowser.open_new('https://www.mail.google.co.in/')  

        elif 'open youtube' in command :
            print('opening youtube ...')
            say('opening youtube..')
            webbrowser.open_new('https://www.youtube.com')

        elif 'open insta' in command :
            print('opening instagram ...')
            say('opening instagram..')
            webbrowser.open_new('https://www.instagram.com')

        elif 'open github' in command :
            print('opening github ...')
            say('opening github..')
            webbrowser.open_new('https://www.github.com')

        elif 'bye' or 'stop' in command:
            print('good bye, see you soon')
            say('good bye, see you soon')
            sys.exit()

        elif 'thank you' or 'thanks' in command :
            print("my pleasure")
            say("my pleasure") 

        else:
            print(' Here is what I found on the internet..')
            say('Here is what i found on the internet..')
            search = 'https://www.google.com/search?q='+command
            webbrowser.open(search)

    except exception as e:
        print(e)             

print('Loading...Please wait')
say('Loading...Please wait')
print("\nhi pal, I am your virtual friend. How can I help you ?")
say("hi pal, I am your virtual friend. How can I help you ?")