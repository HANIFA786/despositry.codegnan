'''
smtplib module
--------------
->This provides a client to sending emails via the Simple Mail Transfer Protocol (SMTP)



import smtplib
from email.message import EmailMessage

sender_email = "aareefashaik00@gmail.com"
password = "Ammulu@786"

receiver_email = "pallipujitha3@gmail.com"

msg = EmailMessage()
msg['subject'] = "Python Email Automation"
msg['From'] = sender_email
msg['To'] = receiver_email

msg.set_content("Hello Student, \nThis email is sent using python.")

server = smtplib.SMTP_SSl('@gmail.com',465)

server.login(sender_email,password)

server.send_message(msg)

server.quit()

print("Email Sent Successfully")

'''
import pyttsx3
import speech_recogination as sr
import datetime
import webbrower
import wikipedia

#initialize voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recoginer.pause_threshold = 1
        audio = recoginer.listen(source)

    try:
        print("Recognizing...")
        command = recogizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    
    except Exception:
        print("Sorry, please say that again.")
        return ""

def wish_user():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning")

    elif hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    speak("I am Your Virtual Assistant")
wish_user()

while True:

    command = take_command()

    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %P")
        speak(f"The time is {time}")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "oppen google" in command:
        webbrowser.open("https://www.google.com")

    elif "who is" in command:
        person = command.replace("who is"  "")
        info = wikipedia.summary(person,2)
        print(info)
        speak(info)
    elif "exit" in command:
        speak("Goodbye")
        break








































