import pyttsx3 as tts
import speech_recognition as sr
import datetime as dt
import smtplib
import pywhatkit as pw
import pyautogui
import webbrowser as wb

phone_no = '+2348160475336'
phone_book = {"babe": "+2348148292779","joy": "+2347080035379"}
engine = tts.init()
rate = engine.getProperty('rate')
engine.setProperty(rate,150)

def getvoices(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice',voices[0].id)
        speak("This is Prime")

    if voice == 2:
        engine.setProperty('voice',voices[1].id)
        speak("This is Favour")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

"""def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            speak(text)
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            speak("Oops! An error occurred. Check your internet connection or try again later.")"""

def time():
    Time = dt.datetime.now().strftime("%I:%M") # getting the hour, minute
    speak("The current time is: ")
    speak(Time)

def date():
    months_of_the_year = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
        ]

    year = int(dt.datetime.now().year)
    month_index = int(dt.datetime.now().month)
    month = months_of_the_year[month_index]
    date_now = int(dt.datetime.now().day)
    speak(str(date_now)+'th of')
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    greeting()
    speak("prime at your service, please tell me how can i be of service?")

def greeting():
    hour = dt.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("good morning")

    elif hour >= 12 and hour <18:
        speak("good afternoon")
    elif hour >= 18 and hour < 24:
        speak("good evening")
    else:
        speak("good night")

def take_CMD():
    query = input("Please How can i be of service?: ")
    return query


def sendEmail():
    server = smtplib.SMTP("smtp.gmail.com", 587) # setting the server type to gmail 
    server.starttls()  # ensure its secured
    server.login(senderEmail, password)
    server.sendmail(senderEmail,receiver_email,"hello this is a test email")
    server.close()

def sendWhatsappMsg(phone_no, message):
   recognizer = sr.Recognizer()
   with sr.Microphone() as source:
        print("Listening for message......")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing message ......")
            query = recognizer.recognize_google(audio,language="en-NG")
            print(query)
            speak("I have gotten the message. Who do you want to send it to?")
            print("Listening for Reciever......")
            recognizer.pause_threshold = 1
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = recognizer.listen(source)
            receiver_phone = recognizer.recognize_google(audio,language="en-NG")
            print(receiver_phone)
            if receiver_phone not in phone_book.keys():
                speak("Invalid Contact")
                speak("Pleae say the name again.")
                print("Listening for Reciever......")
                recognizer.pause_threshold = 1
                recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
                audio = recognizer.listen(source)
                receiver_phone = recognizer.recognize_google(audio,language="en-NG")
                print(receiver_phone)

            else:
                pw.sendwhatmsg(phone_book[receiver_phone],message,12,48)
                speak("message sent.")

        except Exception as e:
            print(e)
            speak("say that again please...")


    



def take_CMD_MIC():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening......")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing......")
            query = recognizer.recognize_google(audio,language="en-NG")
            print(query)
        except Exception as e:
            print(e)
            speak("say that again please...")
            return "None"
        return query

if __name__ == "__main__":
    wishme()
    while True:
        query = take_CMD_MIC().lower()
        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'whatsapp' in query:
            sendWhatsappMsg(phone_no,query)
        else:
            speak("i don't understand your command sir")


