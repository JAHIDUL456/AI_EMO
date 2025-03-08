import sys
import typing 
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QThread 
import pyttsx3
import speech_recognition
import cv2
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QPushButton, QWidget
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pyautogui
import random
import webbrowser
import pygame
from PyQt5.QtGui import QTextCursor
import speedtest
from datetime import datetime
import time as my_time
from PyQt5.QtCore import pyqtSignal,pyqtSlot
#from emoui import Ui_Form
import pywhatkit
import wikipedia
import pygetwindow as gw
import wolframalpha
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 700)
        Form.setStyleSheet("background-color:black;")
        gif_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gif')
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.label.setText("")
        gif_path_one = os.path.join(gif_folder, 'one.gif')
        self.label.setPixmap(QtGui.QPixmap(gif_path_one))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(780, 50, 131, 121))
        self.label_2.setText("")
        gif_path_four = os.path.join(gif_folder, 'four.gif')
        self.label_2.setPixmap(QtGui.QPixmap(gif_path_four))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(200, 490, 571, 181))
        self.plainTextEdit.setStyleSheet("background-color:transparent;\n"
"color:white;\n"
"border-radius:0.5rem;\n"
"font-size:18px")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(330, 10, 341, 111))
        self.label_3.setText("")
        gif_path_name = os.path.join(gif_folder, 'name.gif')
        self.label_3.setPixmap(QtGui.QPixmap(gif_path_name))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
#hello






#jaa






engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
engine.setProperty("rate",170)





#defining function for audio

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#another
def play_listening_sound():
    pygame.mixer.init()

    
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

    active_window = gw.getActiveWindow()
    if active_window and "chrome" in active_window.title.lower():
        return  

    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sound_file_path = os.path.join(script_dir, 'listening.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file_path)
    pygame.mixer.music.play()
    



#alarm

def alarm(query):
    timehere=open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

#haha sound 
def play_laughter():
                script_dir = os.path.dirname(os.path.abspath(__file__))
                sound_file_path = os.path.join(script_dir, 'archivo.mp3')
                pygame.mixer.init()
                pygame.mixer.music.load(sound_file_path)
                pygame.mixer.music.play()
                my_time.sleep(1)
    
#calculation
def WolfRamAlpha(query):
    apikey='XJ2V8Y-6WXUAV4JXU'
    requester=wolframalpha.Client(apikey)
    requested=requester.query(query)
    
    try:
        answer=next(requested.results).text
        return answer
    except:
        speak("the value is not answerable, sir")
    

def cal(query):
    Term=str(query)
    Term=Term.replace("emo","")
    Term=Term.replace("multiply","*")
    Term=Term.replace("into","*")
    Term=Term.replace("in to","*")
    Term=Term.replace("plus","+")
    Term=Term.replace("minus","-")
    Term=Term.replace("divide","/")
    Term=Term.replace("divided by","/")
    Term=Term.replace("to the power","**")
    Term=Term.replace("modulo","%")
    
    Final=str(Term)
    
    try:
        result=WolfRamAlpha(Final)
        ui.terminalPrint(f"{result}")
        speak(f'answer is {result}')
        
    except:
        speak("the value is not answerable , sir")






#notepad

def notepad():
    speak("Tell me the query , I am ready to write")
    
    
    writes =startExecution.takeCommand()
    current_time = datetime.now().strftime("%H-%M")
    filename = f"{current_time}-note.txt"
    
    folder_path = "C:\\notepad"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    file_path = os.path.join(folder_path, filename)
    
    with open(file_path, "w") as file:
        file.write(writes)
    
    os.startfile(file_path)

#memory mode

class VoiceAssistant:
    def __init__(self):
        home_directory = os.path.expanduser("~")
        memory_folder_path = os.path.join(home_directory, "memory") #1
        if not os.path.exists(memory_folder_path):
            os.makedirs(memory_folder_path)
        self.memory_file_path = os.path.join(memory_folder_path, "memory.txt")   
        self.memory = {}
        self.load_memory_from_file()

    def listen(self):
        recognizer = speech_recognition.Recognizer()

        with speech_recognition.Microphone() as source:
            ui.terminalPrint("Listening...")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            ui.terminalPrint(f'you said: {command}')
           
            return command.lower()
        except speech_recognition.UnknownValueError:
            ui.terminalPrint("Could not understand audio.")
            return ""
        except speech_recognition.RequestError as e:
            ui.terminalPrint("Could not request results; {0}".format(e))
            return ""

    def remember(self, questions, answers):
        for question, answer in zip(questions, answers):
            self.memory[question.lower()] = answer
        self.save_memory_to_file()
        speak("I've remembered the answers for the given questions.")

    def recall(self, question):
        question_lower = question.lower()

        if question_lower in self.memory:
            ui.terminalPrint(f"Answer for {question}: {self.memory[question.lower()]}")
           # ui.terminalPrint("Answer for", question, ":", self.memory[question_lower])
            speak("Answer for {}: {}".format(question, self.memory[question_lower]))

        else:
            ui.terminalPrint(f"I don't have an answer for {question}")
           # ui.terminalPrint("I don't have an answer for", question)
            speak(f'I dont have an answer for{question}')
            
            

    def clear_memory(self):
        self.memory.clear()
        self.save_memory_to_file()
        speak("Memory has been cleared , sir")

    def clear_specific(self, question):
        question_lower = question.lower()

        if question_lower in self.memory:
            del self.memory[question_lower]
            self.save_memory_to_file()
            speak(f'memory for {question} has been cleared')
        else:
            speak("Question not found. Cannot clear memory.")

    def update_answer(self, question, new_answer):
        question_lower = question.lower()
        if question_lower in self.memory:
            self.memory[question_lower] = new_answer
            self.save_memory_to_file()
            speak(f'answer for {question} has been updated')
        else:
            speak("Question not found. Cannot update the answer.")

    def clear_method(self):
        speak("Do you want to clear all stored data or a specific question?")
        action = self.listen()

        if "all" in action:
            self.clear_memory()
        elif "specific" in action:
            speak("Which question would you like to clear?")
            specific_question = self.listen()
            self.clear_specific(specific_question)
        else:
            speak("Invalid option. Please say 'all' or 'specific'.")

    def save_memory_to_file(self):
        with open(self.memory_file_path, "w") as file:
            for question, answer in self.memory.items():
                file.write(f"{question}:{answer}\n")

    
    
    #2
    def load_memory_from_file(self):
        try:
            with open(self.memory_file_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(":")
                    if len(parts) == 2:
                        question, answer = parts
                        self.memory[question.lower()] = answer
        except FileNotFoundError:
            # If the file is not found, create the file
            with open(self.memory_file_path, "w") as file:
                file.write("")

def run_voice_assistant():
    assistant = VoiceAssistant()

    while True:
        command = assistant.listen()

        if "remember" in command:
            speak("Start adding question-answer pairs. Say 'stop' to finish.")
            questions = []
            answers = []

            while True:
                speak("Enter a question:")
                question = assistant.listen()
                if "stop" in question.lower():
                    break

                speak("Enter the answer:")
                answer = assistant.listen()

                questions.append(question)
                answers.append(answer)

            assistant.remember(questions, answers)

        elif "recall" in command:
            speak("What question would you like me to recall the answer to?")
            question = assistant.listen()
            assistant.recall(question)

        elif "clear" in command:
            assistant.clear_method()

        elif "update" in command:
            speak("For which question would you like to update the answer?")
            question = assistant.listen()
            speak("What is the new answer for that question?")
            new_answer = assistant.listen()
            assistant.update_answer(question, new_answer)

        elif "exit" in command:
            speak("exit from memory mode")
            break

        else:
            speak("Sorry, I don't understand that command.")


 

   
#search option

    
#searching on google and wikipedia
def searchongoogle(query):
    import wikipedia as googlescrap
    if "google" in query:
        query=query.replace("google"," " )
        query=query.replace("emu"," " )
        query=query.replace("google search"," " )
        speak("this is what i found on google")
        
        try:
            pywhatkit.search(query)
            result=googlescrap.summary(query)
            speak(result,2)
        
        except:
            speak("sorry sir, i am not able to find that")
        
                            
#searching on youtube 

def searchonyoutube(query):
    if "youtube" in query:
        query=query.replace("emo"," " )
        query=query.replace("youtube"," " )
        query=query.replace("youtube search"," " )
        query=query.replace("search on youtube"," " )
        speak("this is what i found on youtube") 
        
        web="https://www.youtube.com/results?search_query="+query
        webbrowser.open(web)
        pywhatkit.playonyt(query)


#search in wikipedia

def searchonwikipedia(query):
    if "wikipedia" in query:
        query=query.replace("emo"," " )
        query=query.replace("wikipedia"," " )
        query=query.replace("wikipedia search"," " )
        query=query.replace("search on wikipedia"," " )
        results=wikipedia.summary(query,sentences=2)
        speak("this is what i found on wikipedia")
        speak(results)

   
#screenshot

def screen():
    folder_name = "screenshots"
    folder_path = os.path.join("C:\\", folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    my_time.sleep(5)
    timestamp = my_time.strftime("%Y%m%d_%H%M%S")
    screenshot = pyautogui.screenshot()
    file_name = f"screenshot_{timestamp}.png"
    file_path = os.path.join(folder_path, file_name)
    screenshot.save(file_path)
    ui.terminalPrint(f"Screenshot taken and saved as '{file_path}'")
    speak(f"Screenshot taken and saved in your device")

#selfie

def selfie():
    folder_name = "selfies"
    folder_path = os.path.join("C:\\", folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    timestamp = my_time.strftime("%Y%m%d_%H%M%S")
    cap = cv2.VideoCapture(0)
    for _ in range(50):
        ret, frame = cap.read()
        cv2.imshow("Camera Feed", frame)
        cv2.waitKey(10) 
    speak("perfect ")   
    file_name = f"selfie_{timestamp}.png"
    file_path = os.path.join(folder_path, file_name)
    cv2.imwrite(file_path, frame)
    cap.release()
    cv2.destroyAllWindows()
    ui.terminalPrint(f"Selfie taken and saved as '{file_path}'")
    


#ui
class jarvisMain(QThread):
    close_signal = pyqtSignal()
    def __init__(self):
        super(jarvisMain,self).__init__()

    def run(self):
        self.runJarvis()
    #defining function for speech recognition
    def takeCommand(self):
        r=speech_recognition.Recognizer()
        play_listening_sound()
        
         
        with speech_recognition.Microphone() as source:
            
            ui.terminalPrint("Listening...")
            #r.pause_threshold=2
            #r.energy_threshold=300
            audio=r.listen(source,0,4)
            
        try:
            ui.terminalPrint("Recognizing...")
            query=r.recognize_google(audio,language="en-India")
            ui.terminalPrint(f"You said:{query}\n")
        
        except Exception as e:
            ui.terminalPrint("Say it again...")
            return "None"
        return query  



    def runJarvis(self):
        while True:
            query=self.takeCommand().lower()
            if "emo" in query or "emu" in query or "imo" in query:
                from greet import greetMe
                greetMe()
            
            elif "" in query:
                continue
            
            
      
            
            
            while True:
                query=self.takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir . Call me any time you want")
                    break
                
                elif "hello" in query:
                    speak("Hello sir ,how are you?")
                elif "hi" in query:
                    speak("Hi sir ,how are you?")
                elif "oi" in query:
                    speak("Hello sir ,how are you?")
                elif "hola" in query:
                    speak("Hola sir ,how are you?")    
                elif "i am fine" in query:
                    speak("that's great sir")   
                elif "good" in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("I am AI voice assistant ,so i am always fine and cheerful")
                elif "what about you" in query:
                    speak("I am AI voice assistant ,so i am always fine and cheerful")
                elif "thank you" in query:
                    speak('you are welcome , sir')
                elif "who made you" in query:
                    speak("Muhammad Jahidul islam made me")
                elif "who is your boss" in query:
                    speak("Currently you are my boss")
                elif "hahahah" in query or "haha" in query:
                    speak("why you are laughing sir")
                
                #app control
                
                
                #tab minimize
                elif "minimize" in query:
                    from dictapp import closeapp
                    closeapp(query)
                    
                #tab restore
                elif "restore" in query:
                    from dictapp import restoreapp
                    restoreapp(query)
                
                
                #full youtube controll
                
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                
                elif "play a game" in query or "play again" in query:
                    pyautogui.press("k")
                    speak("video playing")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up, sir")
                    volumeup()
                
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume downk, sir")
                    volumedown()
            
                #Remember something personal
                elif "memory mode" in query:
                    speak("memory mode activated , sir")
                    run_voice_assistant()
                
                #Set reminder
                
                elif "reminder" in query or "set a reminder" in query:
                    rememberMessage=query.replace("set a reminder", "")
                    rememberMessage=query.replace("that", "")
                    rememberMessage=query.replace("remember that", "")
                    rememberMessage=query.replace("emo", "")
                    speak("you told me "+rememberMessage)
                    reminder1=open("reminder.txt","w")
                    reminder1.write(rememberMessage)
                    reminder1.close()
                
                elif "tell me the schedule" in query:
                    reminder1=open("reminder.txt","r")
                    speak("you told me "+reminder1.read())
                
                #this portion is for your entertainment
                
                elif "tired" in query or "i am tired" in query:
                    speak("playing some relaxing song sir ")
                    b=random.randint(1, 3)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=SuEkOAayWZo&ab_channel=SuccessfulAspects")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=bP9gMpl1gyQ&ab_channel=TheSoulofWind")
                    elif b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=lFcSrYw-ARY&ab_channel=MeditationRelaxMusic")
                    else:
                        speak("go for sleep") 
                
                
                #this part is for some jokes
                
        
                
                elif "jokes" in query or "tell me a joke" in query:
                    speak("Let me warn you, if laughter were a sport, this one would be a gold medalist.") 
                    d = random.randint(1, 3)
                    if d==1:
                        speak("Why did the math book look sad?   Because it had too many problems.")
                        play_laughter()
                    elif d==2:
                        speak("Parallel lines have so much in common. It's a shame they'll never meet.") 
                        play_laughter()                  
                    elif d==3:
                        speak("I used to play piano by ear, but now I use my hands and fingers.")
                        play_laughter()               
                    else:
                        speak("no more jokes today")
                    
                    
                #this lines is for calculation
                elif "calculate" in query:
                    query=query.replace("calculate","")
                    query=query.replace("please","")
                    query=query.replace("emo","")
                    cal(query)
                    
                #this portion is for shut down the pc
                elif "shut down the pc" in query:
                    ui.terminalPrint("are you sure to shut down the pc?")
                    speak("are you sure to shut down the pc?")
                    confirm=self.takeCommand()
                    if confirm=="yes":
                        speak("ok,sir")
                        os.system("shutdown /s /t 1")
                    else:
                        speak("cancelled")
                        break
                
                #open any app simple method
                
                elif "open" in query:
                    query=query.replace("emo","")
                    query=query.replace("open","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(1)
                    pyautogui.press("enter")
                
                elif "close" in query:
                    query=query.replace("emo","")
                    query=query.replace("close","")
                    pyautogui.hotkey('alt','f4')
                    my_time.sleep(1)
                    
                    
                #internet speedtest
                
                elif "internet speed" in query:
                    query=query.replace("emo","")
                    query=query.replace("tell me","")
                    ui.terminalPrint("internet speed test running----")
                    wifi=speedtest.Speedtest()
                    upload_net=round(wifi.upload()/1048576)
                    download_net=round(wifi.download()/1048576)
                    ui.terminalPrint(f"wifi upload speed is {upload_net} mbps")
                    ui.terminalPrint(f"wifi download speed is {download_net} mbps")
                    speak(f"your internet upload speed is {upload_net} mbps")
                    speak(f"your internet download speed is {download_net} mbps")
                
                
                #notepad
                elif "note" in query:
                    speak("ok,sir")
                    notepad()
                
                #screenshot
                
                elif "screenshot" in query:
                    speak("capturing screenshots please wait")
                    screen()
                
                
                #selfie
                elif "selfie" in query:
                    speak("smile ")
                    selfie()
                
                #keyboard mastery
                elif "select all" in query:
                    x_coordinate = 0
                    y_coordinate = 0
                    pyautogui.moveTo(x_coordinate, y_coordinate)
                    pyautogui.click()
                    pyautogui.hotkey('ctrl', 'a')
                
                elif "copy" in query:
                    pyautogui.hotkey('ctrl', 'c')
                    my_time.sleep(1)
                    speak("Content copied, sir")
                
                elif "paste" in query or "peste" in query or "best" in query:
                    pyautogui.hotkey('ctrl', 'v')
                    my_time.sleep(1)
                    speak("Content pasted, sir")
                
                elif "undo" in query:
                    pyautogui.hotkey('ctrl', 'z')
                    my_time.sleep(1)
                
                elif "redo" in query:
                    pyautogui.hotkey('ctrl', 'y')
                    my_time.sleep(1)
                
                elif "new file" in query:
                    pyautogui.hotkey('ctrl', 'n')
                    my_time.sleep(1)
                
                #file save
                elif "save the file" in query:
                    speak("Please provide the file name for saving.")
                    file_name = startExecution.takeCommand()
                    pyautogui.hotkey('ctrl', 's')
                    my_time.sleep(2)
                    pyautogui.write(file_name)
                    pyautogui.press('enter')
                    speak(f"File '{file_name}' saved successfully.")
                    
                
                #typing mode
                elif "typing mode" in query:
                    speak("typing mode activated, sir")
                    file_name = startExecution.takeCommand() 
                    pyautogui.write(file_name)
                    pyautogui.press('space')
                    my_time.sleep(1)
                    
                
                elif "backspace" in query or "Back space" in query or "back space" in query:
                    pyautogui.press('backspace') 
                    my_time.sleep(1) 
                
                
                #power mode
                
                elif "enter" in query:
                    pyautogui.press('enter')
                    my_time.sleep(1)
                
                
                elif "recent" in query or "recents" in query:
                    pyautogui.hotkey('winleft', 'tab') 
                    my_time.sleep(1)
                
                elif "left" in query:
                    my_time.sleep(1)
                    pyautogui.press('left')
                    my_time.sleep(1)
                
                elif "right" in query:
                    my_time.sleep(1)
                    pyautogui.press('right')
                    my_time.sleep(1)
                
                elif "upper" in query:
                    my_time.sleep(1)
                    pyautogui.press('up')
                    my_time.sleep(1)
                
                elif "down" in query:
                    my_time.sleep(1)
                    pyautogui.press('down')
                    my_time.sleep(1)
            
                    
                elif "who is your creator" in query:
                    speak("muhammad jahidul islam programmed me")
                    ui.terminalPrint("MD. JAHIDUL ISLAM (ETE-19 ,RUET) EMAIL: mdjahidulislamjahid099@gmail.com")  
                    my_time.sleep(10) 
                    
                    
                    
                
                    
                    
                
                    
                    
                    
                
                
                
                
                    
                    
                    
                
                
                
            
                        
                    
                    
            
                
                    
                    
                
                
                    
                #this portion is for setting the alarm manually
                
                
            
                #this portion is for documentry purposes
                elif "google" in query:
                    searchongoogle(query)
                    
                elif "youtube" in query:
                    searchonyoutube(query)
                elif "wikipedia" in query:
                    searchonwikipedia(query)
                elif "the time" in query:
                    current_time = datetime.now().strftime("%I:%M %p")
                    speak(f"current time is {current_time}")
                elif "the date" in query:
                    current_date = datetime.now().strftime("%A, %B %d, %Y")
                    speak(f"current date is {current_date}")
                elif "bye" in query:
                    speak("Good bye sir")
                    self.close_signal.emit()
                    break
                

           
           


startExecution=jarvisMain()
#class2

class guiOfJarvis(QWidget):
    terminalPrintSignal = pyqtSignal(str)
    
    def __init__(self):
        super(guiOfJarvis,self).__init__()
        self.jarvisUi=Ui_Form()
        self.jarvisUi.setupUi(self)
        self.terminalPrintSignal.connect(self.terminalPrint)
        self.runAllMovies()

    
        
    def runAllMovies(self):
        gif_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gif')
        gif_path_one = os.path.join(gif_folder, 'one.gif')

        self.jarvisUi.codingMovie = QtGui.QMovie(gif_path_one)
        self.jarvisUi.label.setMovie(self.jarvisUi.codingMovie)
        self.jarvisUi.codingMovie.start()
        
        gif_path_four = os.path.join(gif_folder, 'four.gif')
        self.jarvisUi.codingMovie = QtGui.QMovie(gif_path_four)
        self.jarvisUi.label_2.setMovie(self.jarvisUi.codingMovie)
        self.jarvisUi.codingMovie.start()
        
        
        gif_path_name = os.path.join(gif_folder, 'name.gif')
        self.jarvisUi.codingMovie = QtGui.QMovie(gif_path_name)
        self.jarvisUi.label_3.setMovie(self.jarvisUi.codingMovie)
        self.jarvisUi.codingMovie.start()
       
        startExecution.start()
        startExecution.close_signal.connect(self.close)
    
   # def terminalPrint(self, text):
        # Emit the signal with the text
        
        #self.jarvisUi.plainTextEdit.setPlainText(text)
    
    
    def registerQTextCursor():
        # Registering QTextCursor using qRegisterMetaType
        try:
            from PyQt5.QtCore import QTextCursor
            QTextCursor
        except RuntimeError:
            pass
        
    def terminalPrint(self, text):
        # Disable the cursor temporarily
        self.jarvisUi.plainTextEdit.setUpdatesEnabled(False)

        # Append text to the end of the QPlainTextEdit
        cursor = self.jarvisUi.plainTextEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text + "\n")
        self.jarvisUi.plainTextEdit.setTextCursor(cursor)

        # Re-enable the cursor
        self.jarvisUi.plainTextEdit.setUpdatesEnabled(True)
        self.jarvisUi.plainTextEdit.update()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ui=guiOfJarvis()
    ui.show()
    
    sys.exit(app.exec_())
    
        
        
