import pyttsx3 as pt
import webbrowser as web
import speech_recognition as sr
import random
import wikipedia
import datetime
import os
import time
import calendar
import pyjokes
from time import time
from numpy import number
import phonenumbers
from phonenumbers import carrier,timezone,geocoder

r=sr.Recognizer()
#r1=sr.Recognizer()
engine=pt.init()                        
engine.setProperty('rate', 300)  

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print(" good morning")
        engine.say("hey good morning")
        engine.runAndWait()
    elif hour>=12 and hour<18:
        print(" good afternoon")
        engine.say("hey good afternoon")
        engine.runAndWait()
    else:
        print('good evening')
        engine.say("hey good evening")
        engine.runAndWait()

def search():
    engine.say("what can i do for you")
    engine.runAndWait()
    text=input('type something.....\n')
    return text
    
def query():
    text=input('type something.....\n')
    return text

def scissors_game():   
    player=0
    cpu=0
    engine=pt.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("welcome to rock paper scissors game ")
    engine.runAndWait()

    while player<3 and cpu<3:
        cpu_choice=random.choice(["rock","paper","scissors"])
  
        player_choice=input("rock,paper,scissors : ")

        print("cpu:",cpu_choice,"player:",player_choice)

        if player_choice==cpu_choice:
            engine.say("tie!no points")
            engine.runAndWait()
  
        elif player_choice.lower()=="rock":
            if cpu_choice.lower()=="scissors":
                player+=1
                engine.say(f"player wins {player} games")
                engine.runAndWait()
            elif cpu_choice.lower()=="paper":
                cpu+=1
                engine.say(f"cpu wins {cpu} games")
                engine.runAndWait()

        elif player_choice.lower()=="scissors":
            if cpu_choice.lower()=="paper":
                player+=1
                engine.say(f"player wins {player} games")
                engine.runAndWait()
            elif cpu_choice.lower()=="rock":
                cpu+=1
                engine.say(f"cpu wins {cpu} games")
                engine.runAndWait()

        elif player_choice.lower()=="paper":
            if cpu_choice.lower()=="rock":
                player+=1
                engine.say(f"player wins {player} games")
                engine.runAndWait()
            elif cpu_choice.lower()=="scissors":
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
#wish()
say=search().lower()

if "google" in say:
    engine.say('what do you want to search in google')
    engine.runAndWait()
    inp=query()
    url="www.google.com/search?q="+inp
    web.open(url)
    engine.say("i found these results")
    engine.runAndWait()

elif "wikipedia" in say:
    result=wikipedia.summary(say,sentences=3)
    print(result)

elif "facebook" in say:
    web.open("www.facebook.com")
    engine.say("opening facebook")
    engine.runAndWait()

elif "mail" in say:
    web.open("www.gmail.com")
    engine.say("opening mail")
    engine.runAndWait()

elif "youtube" in say:
    engine.say('what do you want to search in youtube')
    engine.runAndWait()
    inp=query()
    url="www.youtube.com/search?q="+inp
    web.open(url)
    engine.say("i found these results ")
    engine.runAndWait()

elif "location" in say:
    engine.say("which location you want to search for")
    engine.runAndWait()
    inp=query()
    url="www.google.nl/maps/place/"+inp
    web.open(url)
    engine.say("i found these results")
    engine.runAndWait()

elif "my github" in say:
    web.open("https://github.com/sairampolisetty")
    engine.say("opening github")
    engine.runAndWait()  

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

elif "whatsapp" in say:
    web.open("www.whatsappweb.com")
    engine.say("opening whatsapp")
    engine.runAndWait()  

elif "guess game" in say:
    guess_game()
    quit()

elif "rock paper game" in say:
    guess=scissors_game()
    quit()

elif 'calendar' in say:
    engine.say("please type which year you want")
    engine.runAndWait()
    year=int(input("enter year"))
    engine.say("and which month")
    engine.runAndWait()
    month=int(input('enter month'))
    print(calendar.month(year,month))

elif "date" in say:
    current_time=datetime.datetime.now()
    print("day:",end="")
    print(current_time.day)
    engine.say(f"todays date is {current_time.day}")
    engine.runAndWait()

elif "time" in say:
    time=datetime.datetime.now().strftime("%H %M")
    print(time)
    engine.say(f"the time is{time}")
    engine.runAndWait()

elif "month" in say:
    time=datetime.datetime.now().strftime("%h")
    print(time)
    engine.say(time)
    engine.runAndWait()

elif "created" in say:
    engine.say("i was created by sairam polisetty")
    engine.runAndWait()

elif "name" in say:
    engine.say("my name is personal assistent")
    engine.runAndWait()

elif "notepad" in say:
    npath='notepad.exe'
    os.startfile(npath)
    engine.say("opening notepad")
    engine.runAndWait()

elif "camera" in say:
    os.system("start microsoft.windows.camera:")
    engine.say("opening camera")
    engine.runAndWait()

elif "excel" in say:
    npath='excel.exe'
    os.startfile(npath)
    engine.say("opening excel")
    engine.runAndWait()

elif "how are you" in say:
    engine.say('i am doing good ')
    engine.runAndWait()
    engine.say('hope you are also doing well')
    engine.runAndWait()

elif "joke" in say:
    joke=pyjokes.get_joke(language="en",category="all")
    print(joke)
    engine.say(joke)
    engine.runAndWait()

elif "need" in say:
    engine.say("ok thank you for using me have a great day")
    engine.runAndWait()
    exit()

elif "exit" in say:
    exit()

elif "what are you doing" in say:
    engine.say('nothing just searching results for you')
    engine.runAndWait()

else:
    engine.say('sorry i dont know answer to this question but i am learning')
    engine.runAndWait()

###########################################