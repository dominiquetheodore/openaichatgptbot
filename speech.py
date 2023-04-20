import speech_recognition as sr
import os
import openai
import pyttsx3
import subprocess

openai.api_key = os.getenv("OPENAI_API_KEY")

# obtain audio from the microphone
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)
print(sr.Microphone.list_microphone_names())
conversation = ""

while True:
    with mic as source:
        print("Say something!")
        audio = r.listen(source, phrase_time_limit=3.0)
    
    print("No longer listening")

    try:
        user_input = r.recognize_google(audio)
    except:
        continue

    print("You said " + r.recognize_google(audio))
    conversation += user_input

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,  
        max_tokens=50
    )

    response_str = response["choices"][0]["text"].replace("\n", "")
    print(response_str)
    subprocess.call(["say",response_str])