import os 
import pyautogui
import pyttsx3
import webbrowser
from time import sleep


engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
engine.setProperty("rate",170)

#defining function for audio

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


dictapp={"commandprompt":"cmd","painter":"paint","notepad":"notepad","matlab":"matlab","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpoint","camera":"camera","calculator":"calculator","settings":"settings"}

#for webapp opening

def openwebapp(query):
    speak("launching ,sir")
    if ".com" in query or ".co.in" in query or ".co.out" in query or ".bd" in query or ".org" in query:
        query=query.replace("open","")
        query=query.replace("emu","")
        query=query.replace("launch","")
        query=query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    
    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")


#for closing app

def closeapp(query):
    speak("closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("one tab minimized ,sir")
    
    elif "two tab" in query or "2 tab" in query or "to tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("two tab minimized ,sir")
    elif "three tab" in query or "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("three tab minimized ,sir")
    elif "four tab" in query or "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("four tab minimized ,sir")
    
    elif "five tab" in query or "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tab minimized ,sir")
    
    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
                speak("app minimized,sir")


#for restored app

def restoreapp(query):
    speak("restoring,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","shift","t")
        speak("one tab restored ,sir")
    
    elif "two tab" in query or "2 tab" in query or "to tab" in query:
        pyautogui.hotkey("ctrl","shift","t")
        sleep(0.5)
        pyautogui.hotkey("ctrl","shift","t")
        speak("two tab restored ,sir")
    elif "three tab" in query or "3 tab" in query:
        pyautogui.hotkey("ctrl","shift","t")
        sleep(0.5)
        pyautogui.hotkey("ctrl","shift","t")
        sleep(0.5)
        pyautogui.hotkey("ctrl","shift","t")
        speak("three tab restored ,sir")
    elif "four tab" in query or "4 tab" in query:
        pyautogui.hotkey("ctrl","shift","t")
        sleep(0.5)
        pyautogui.hotkey("ctrl","shift","t")
        sleep(0.5)
        pyautogui.hotkey("ctrl","shift","t")
        sleep(0.5)
        pyautogui.hotkey("ctrl","shift","t")
        speak("four tab restored ,sir")
    
    elif "five tab" in query or "5 tab" in query:
        pyautogui.hotkey("ctrl","shift","t")
        sleep(0.5)
        pyautogui.hotkey("ctrl","shift","t")
        sleep(0.5)
        pyautogui.hotkey("ctrl","shift","t")
        sleep(0.5)
        pyautogui.hotkey("ctrl","shift","t")
        sleep(0.5)
        pyautogui.hotkey("ctrl","shift","t")
        speak("all tab restored ,sir")
    
    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
                speak("app restored,sir")        
        
                
        

        
    