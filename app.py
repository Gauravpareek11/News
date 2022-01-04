import streamlit as st
import requests
import json
from win32com.client import Dispatch
# import pyttsx3
def speak(str1):
    speak=Dispatch("SAPI.spvoice")
    speak.speak(str1)
#     engine = pyttsx3.init()
#     engine.say(str1)
#     engine.runAndWait()

st.title('NEWS For The Day')
# speak=pyttsx3.init()
speak("NEWS for today.......")
url="http://newsapi.org/v2/top-headlines?country=in&apiKey=bf905beed1f440b780221fa6085b42f6"
t=requests.get(url=url).text
news=json.loads(t)
d=news['articles']
i=0
for articles in d:
    i+=1
    st.subheader(str(i)+'.'+articles['title'])
    speak(articles['title'])
    st.write(articles['description'])
    st.write('Read full news at:')
    st.write(articles['url'])
    speak("next news.......")
    if(i>20): 
        speak('Thank You.....')
        break
