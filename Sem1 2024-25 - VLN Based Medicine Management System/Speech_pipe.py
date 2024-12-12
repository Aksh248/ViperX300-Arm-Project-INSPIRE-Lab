import os
from openai import OpenAI

def speech_2_txt():
    client = OpenAI(api_key='ENTER_API_KEY')
    origin = '/home/alpha3/Desktop/Arm_project/24-25 sem1/speech_pipe/uploads/'
    target = '/home/alpha3/Desktop/Arm_project/24-25 sem1/speech_pipe/old_files/'
    files = os.listdir(origin)

    for q in files:
        os.rename(origin + q, target + q)
        audio_file = target + q
        audio_file= open(audio_file, "rb")
        transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
        )
        return transcription.text

def chatgpt(text):
    file1 = open('prompt.txt','r')
    prompt = file1.read()
    client = OpenAI(api_key='ENTER_API_KEY')
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": text}
    ]
    )
    file = open('ans.py','w')
    file.write(response.choices[0].message.content)
    file.close()

trans = speech_2_txt()
print("entering chatGPT")
chatgpt(trans)
print("ChatGPT done")