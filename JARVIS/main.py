import win32com.client
import speech_recognition as sr
import webbrowser
import pygame
import openai
import os
from config import apikey
from datetime import date, datetime

openai.api_key = apikey
chat = ""

def chats(query):
    global chat
    chat += f"Manali said : {query}\n Jarvis : "
    print(chat)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chat,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    saying(response.choices[0].text)
    chat += f"{response.choices[0].text}\n"

    return response.choices[0].text








def ai(prompt):
    # openai.api_key = apikey

    text = f"OpenAI response for {prompt} \n********************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response.choices[0].text)

    # todo: wrap this inside try&catch

    text += response.choices[0].text
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    filename = ''.join(prompt.split('intelligence')[1:]).strip() + ".txt"
    with open(os.path.join("Openai", filename), "w") as f:
        f.write(text)


def saying(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said : {query}")
        except Exception as e:
            return "Some Error Occured. Sorry from Jarvis"
    return query


if __name__ == '__main__':
    saying("hello I am Jarvis AI")
    while True:
        print("listening..")
        # saying(text)
        query = take()
        sites = [["YouTube", "https://youtube.com"], ["Google", "https://google.com"],
                 ["Instagram", "https://www.instagram.com/"], ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                saying(f"Opening {site[0]}")*-
                webbrowser.open(site[1])
        music = [["mausam ki baarish", "/Users/User/Downloads/ymkb.mp3"],
                 ["dandelions", "/Users/User/Downloads/dandelions.mp4"]]
        for music in music:
            if f"play music {music[0]}" in query:
                pygame.mixer.init()
                pygame.mixer.music.load(music[1])
                pygame.mixer.music.play()

        if "say date and time" in query:
            today = date.today()
            saying(f"Today's date is {today}")

            now = datetime.now()
            saying(f"Current date and time is {now}")
        # query = take()
        # if "stop listening".lower() in query:
        #     saying("Jarvis has stopped recognizing")

        if "Using Artificial Intelligence".lower() in query.lower():
            ai(prompt=query)

        if "exit".lower() in query.lower():
            saying("Jarvis has stopped recognizing")
            break

        if "reset chat".lower() in query.lower():
            chat = ""

        else:
            chats(query)


            # Example usage:
            # Replace "your_music_file_path.mp3" with the actual path of your music file

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
