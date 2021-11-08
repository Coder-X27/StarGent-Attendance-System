
# import openpyxl as ex

# a=ex.load_workbook("data.xlsx")

# sheets=a.sheetnames
# print(sheets)
# print(a.active.title)
# sh1=a['Attendance']
# start=7
# while start<=16:
#     data=sh1[f'a{start}'].value
#     print(data)
#     start+=1
    
# # row=sh1.max_row
# # column=sh1.max_column
# # print(row,column)
import pyttsx3
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recongnizing. . .")
        query=r.recognize_google(audio,language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        print('say that again please. . .')
        return 'None'
    return query