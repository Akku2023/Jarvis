import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
# import feedparser
import ollama
from gtts import gTTS
import pygame
import os

#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")
    
    
def aiProcess(command):
    response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": "You are Jarvis, a helpful virtual assistant. Give short responses please."
        },
        {
            "role": "user",
            "content": command
        }
    ]
)

    print("Jarvis:", response["message"]["content"])
    
'''
def get_news(): 
    # Google News RSS feed for India 
    url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en" #"https://www.rss.org/"
    try: 
        feed = feedparser.parse(url) 
        if not feed.entries: 
            speak("Sorry sir, I couldn't find any news right now.") 
            return 
        speak("Here are the latest headlines.") 
        for i, article in enumerate(feed.entries[:5], start=1): 
            headline = article.title 
            print(f"{i}. {headline}") 
            speak(f"Headline {i}: {headline}") 
    except Exception as e: 
        print("News error:", e) 
        speak("Sorry sir, I couldn't fetch the news.")
'''
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
            webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
            webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
            webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
            webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    # elif "news" in c.lower():
    #     r = requests.get("https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en")
    #     if r.status_code == 200:
    #         #parse the JSON response
    #         data = r.json()
            
            #extract the articles
            # articles = data.get("articles", [])
            
            # #print the headlines
            # for article in articles:
            #     speak(article['title'])
                
    else:
        #let OpenAI handle the  request
        output = aiProcess(c)
        speak(output)
    
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        #listen for the wake word "jarvis"
        #obtain audio from the microphone
        r = sr.Recognizer()
             
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                
                    processCommand(command)
            
        except Exception as e:
            print("Error; {0}".format(e))