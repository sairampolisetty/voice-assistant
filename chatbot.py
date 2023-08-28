import pyttsx3 as pt
import webbrowser as web
import speech_recognition as sr
import random
import wikipedia
import datetime
import os
import time
import pywhatkit as pwt
import pyautogui
import calendar
import pyjokes
import psutil
import socket
import requests
from tkinter import *
from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup
from time import time
from numpy import number
import phonenumbers
from phonenumbers import carrier,timezone,geocoder


r=sr.Recognizer()
#r1=sr.Recognizer()
engine=pt.init()    
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)                    
engine.setProperty('rate', 200)  

#wishing
def wish():

    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print(" good morning")
        engine.say("hey good morning")
        engine.runAndWait()
    elif hour>=12 and hour<18:
        print(" good afternoon")
        engine.say("helo, good afternoon")
        engine.runAndWait()
    else:
        print('good evening')
        engine.say("helo, good evening")
        engine.runAndWait()
    speak('what can i do for you')

#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def search():
    #print('Type something.......')
    text=input("Type something.......\n")
    return text
  
def query():
    text=input("Type your query here.......\n")
    return text

#rock paper scissors game
def scissors_game():   
    player=0
    cpu=0
    engine=pt.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("welcome to rock paper scissors game ")
    engine.runAndWait()

    while player<3 and cpu<3:
        cpu_choice=random.choice(["r","p","s"])
  
        player_choice=input("r,p,s: ")

        print("cpu:",cpu_choice,"player:",player_choice)

        if player_choice==cpu_choice:
            engine.say("tie!no points")
            engine.runAndWait()
  
        elif player_choice.lower()=="r":
            if cpu_choice.lower()=="s":
                player+=1
                engine.say(f"player wins {player} games")
                engine.runAndWait()
            elif cpu_choice.lower()=="p":
                cpu+=1
                engine.say(f"cpu wins {cpu} games")
                engine.runAndWait()

        elif player_choice.lower()=="s":
            if cpu_choice.lower()=="p":
                player+=1
                engine.say(f"player wins {player} games")
                engine.runAndWait()
            elif cpu_choice.lower()=="r":
                cpu+=1
                engine.say(f"cpu wins {cpu} games")
                engine.runAndWait()

        elif player_choice.lower()=="p":
            if cpu_choice.lower()=="r":
                player+=1
                engine.say(f"player wins {player} games")
                engine.runAndWait()
            elif cpu_choice.lower()=="s":
                cpu+=1
                engine.say(f"cpu wins {cpu} games")
                engine.runAndWait()

        else:
            engine.say("invalid input")  
            engine.runAndWait()
 
    if player==3:
        engine.say("the total game won by player")
        engine.runAndWait()
    else:
        engine.say("the total game won by cpu")
        engine.runAndWait()
        
    return None    

#number guessing game
def guess_game():
#elif "guess game" in say:
    number=random.randint(0,10)
    tries=0
    found=False
    engine=pt.init()
    #for female voice
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("welcome to number guessing  game ")
    engine.runAndWait()

    engine.say("guess the number ")
    engine.runAndWait()
    while not found:
        guess=int(input("guess:"))
        tries+=1
        if guess==number:
            found=True
            engine.say(f"the number is {number}  you found that after {tries} tries")
            engine.runAndWait()
            print(f"you found the number {number} after {tries} tries")
        elif guess>number:
            engine.say(f"the number is less than {guess}")
            engine.runAndWait()
            print(f"the number is less than {guess}")
        else:
            engine.say(f"the number is greater than {guess}")
            engine.runAndWait()
            print(f"the number is greater than {guess}")

    return None


#######    main    program       ######
if __name__ == "__main__":
    wish()

    while True:
    #if 1:

        say=search().lower()
        if "close" in say:
            if 'close notepad' in say:
                os.system('taskkill /f /im notepad.exe')
                speak('closing notepad')

            if "close excel" in say:
                os.system('taskkill /f /im excel.exe')
                speak('closing excel')

            if "close calculator" in say:
                os.system('taskkill /f /im calculator.exe')
                speak('closing calculator') 

            if "close google" in say:
                os.system("taskkill /im chrome.exe /f")
                speak('closing google')

            if "close youtube" in say:
                os.system("taskkill /im chrome.exe /f")
                speak('closing youtube')
            if "close chrome" in say:
                os.system("taskkill /im chrome.exe /f")

        elif "google" in say:
            engine.say('what do you want to search in google')
            engine.runAndWait()
            inp=query()
            inp=inp.replace("search for ","")
            url="www.google.com/search?q="+inp
            web.open(url)
            engine.say("i found these results")
            engine.runAndWait()
            print("press enter to continue")
            input('')

        elif "wikipedia" in say:
            result=wikipedia.summary(say,sentences=2)
            speak('according to wikipedia')
            print(result)
            speak(result)

        elif "facebook" in say:
            web.open("www.facebook.com")
            engine.say("opening facebook")
            engine.runAndWait()
            print("press enter to continue")
            input('')

        elif "instagram" in say:
            web.open("www.instagram.com")
            engine.say("opening instagram")
            engine.runAndWait()
            print("press enter to continue")
            input('')

        elif 'stack' in say:
            web.open("www.stackoverflow.com")
            speak('opening stackoverflow')
            print("press enter to continue")
            input('')

        elif "mail" in say:
            web.open("www.gmail.com")
            engine.say("opening mail")
            engine.runAndWait()
            print("press enter to continue")
            input('')

        elif "github" in say:
            web.open("https://github.com/sairampolisetty")
            engine.say("opening github")
            engine.runAndWait() 
            print("press enter to continue")
            input('')

        elif "whatsapp" in say:
            web.open("www.whatsapp.com")
            engine.say("opening whatsapp")
            engine.runAndWait()
            print("press enter to continue")
            input('')

        elif "youtube" in say:
            engine.say('what do you want to search in youtube')
            engine.runAndWait()
            inp=query()
            inp=inp.replace("search for ","")
            url="www.youtube.com/search?q="+inp
            web.open(url)
            engine.say("i found these results ")
            engine.runAndWait()
            print("press enter to continue")
            input('')

        elif "music" in say:
            speak("playing songs that you liked very much")
            os.startfile("C:\\Users\\HP\\Music\\Unstoppable(PagalWorld).mp3")

        elif "location" in say:
            engine.say("which location you want to search for")
            engine.runAndWait()
            inp=query()   
            inp=inp.replace("search for ","")         
            url="www.google.nl/maps/place/"+inp
            web.open(url)
            engine.say("i found these results")
            engine.runAndWait()
            print("press enter to continue")
            input('')

        elif "temperature" in say:
            say=say.replace("tell me the current temperature in ","")
            say=say.replace("what is the current temperature in ","")
            say=say.replace("tell me the temperature in ","")
            say=say.replace("what is the temperature in ","")
            url="https://www.google.com/search?q="+"weather"+say
            html=requests.get(url).content
            soup=BeautifulSoup(html,'html.parser')
            temp=soup.find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
            print(f"the current temparature in {say} is {temp}")
            engine.say(f"the current temparature in {say} is {temp}")
            engine.runAndWait() 

        elif "number game" in say:
            guess_number=guess_game()

        elif "rock paper game" in say:
            r_p_s=scissors_game()

        elif 'calendar' in say:
            engine.say("please type which year you want")
            engine.runAndWait()
            year=int(input("enter year"))
            engine.say("and which month")
            engine.runAndWait()
            month=int(input('enter month'))
            print(calendar.month(year,month))

        elif "trace" in say:
            engine.say('enter any phonenumber')
            engine.runAndWait()
            number=input("enter number")
            #number=+919666988423
            phone=phonenumbers.parse(number)
            time=timezone.time_zones_for_number(phone)
            car=carrier.name_for_number(phone,'en')
            reg=geocoder.description_for_number(phone,'en')
            valid=phonenumbers.is_valid_number(phone)
            if valid==1:
                print('yes its valid number')
            else:
                engine.say('its not a valid number please type valid number')
                engine.runAndWait()
                exit()
            #print(valid)
            print(time)
            print(car)
            print(reg)
            print(phone)

        elif "date" in say:
            current_time=datetime.datetime.now()
            print("day:",end="")
            print(current_time.day)
            engine.say(f"todays date is {current_time.day}")
            engine.runAndWait()

        elif "time" in say:
            time=datetime.datetime.now().strftime("%H %M")
            print(time)
            engine.say(f"the time is {time}")
            engine.runAndWait()

        elif "get the details of" in say:
            city=say.replace("get the details of ","")
            cty=city.replace(" city","")
            loc=Nominatim(user_agent="GetLoc")
            getloc=loc.geocode(cty)
            print(getloc.address)
            print("latitude:",getloc.latitude)
            print("longitude:",getloc.longitude)

        elif "ip address" in say:
            host=socket.gethostname()
            ip_address=socket.gethostbyname(host)
            print(ip_address)
            speak(ip_address)

        elif "digital clock" in say:
            #import tkinter
            dc=Tk()
            dc.title("clock")
            dc.geometry("600x90")
            def time():
                import datetime
                #d=time.strftime("%d-%m-%Y, %H %M:%S")
                now=datetime.datetime.now()
                d=now.strftime("%d-%m-%Y, %H %M:%S")
                l.config(text=d)
                l.after(1000,time)

            l=Label(dc,font=("Arial",45),bg="black",fg="green")
            l.pack()
            time()
            mainloop()

        elif "month" in say:
            time=datetime.datetime.now().strftime("%B")
            print(time)
            engine.say(time)
            engine.runAndWait()

        elif "window" in say:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            #time.sleep(1)
            pyautogui.keyUp("alt")

        elif "notepad" in say:
            npath='notepad.exe'
            os.startfile(npath)
            engine.say("opening notepad")
            engine.runAndWait()

        elif 'command prompt' in say:
            os.system('start cmd')
            engine.say("opening command prompt")
            engine.runAndWait()

        elif "camera" in say:
            os.system("start microsoft.windows.camera:")
            engine.say("opening camera")
            engine.runAndWait()

        elif "calculator" in say:
            npath='start calculator:'
            os.system(npath)
            engine.say("opening calculator")
            engine.runAndWait()

        elif "excel" in say:
            npath='excel.exe'
            os.startfile(npath)
            engine.say("opening excel")
            engine.runAndWait()

        elif "battery" in say:
            battery=psutil.sensors_battery()
            per=battery.percent
            print(battery)
            print(per)
            speak(f"we have {per} percentage of battery")
            if per>=80:
                speak('we have enough battery, no need to charge now')
            elif per<=20:
                speak("we have very low power, we have to connect a charger to our system")

        elif "shutdown" in say:
            pwt.shutdown(time=60)
            #os.system('shutdown /s /t /s')

        elif "created" in say:
            engine.say("i was created by sairam polisetty")
            engine.runAndWait()

        elif "name" in say:
            engine.say("my name is sophia")
            engine.runAndWait()

        elif 'who are you' in say:
            speak('i am your personal assistant')

        elif "how are you" in say:
            engine.say('i am doing good ')
            engine.runAndWait()
            engine.say('what about you')
            engine.runAndWait()

        elif "i am also good" in say:
            speak('wow, sounds to be great')

        elif "tell me about yourself" in say:
            speak('ok, i am your virtual assistent, i can lookup answers for you, or help you with find the quickest way home')
            speak('if ypu need anything just ask me , your wish is my command')

        elif "joke" in say:
            joke=pyjokes.get_joke(language="en",category="all")
            print(joke)
            engine.say(joke)
            engine.runAndWait()

        elif "don't need" in say:
            speak("ok thank you for using me have a great day")
            exit()

        elif "second" in say:
            import time
            time.sleep(10)
            speak('your wait time is over')

        elif "what are you doing" in say:
            speak('nothing just searching results for you')

        elif "thank you" in say:
            speak("you are always welcome")

        elif 'exit' in say:
            speak('ok')
            exit()

        elif "break" in say:
            speak('ok,you can call me anytime')
            break

        #else:
         #   engine.say('sorry i dont know answer to this question but i am learning')
          #  engine.runAndWait()
        #speak('anything else')
        ##########################################################