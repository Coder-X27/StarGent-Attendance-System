# Here in the spread sheet The code of the members start from the A7 to the end 
# The name of the members start from the B7 
# The presents start from AH7 and the Absents start from the AI7
# import pyttsx3
# engine=pyttsx3.init('sapi5')
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

def identify(user):
    pass

def markPresent(user):
    pass

def showPresents(user):
    pass
def validation():
    pass


if __name__=="__main__":
    print("Welcome to the StarGent Robotics Biomatrix Attendance System \n")
    choice=int(input("What do you want\n1) Mark Present\n2) Register Yourself as a Community Member\n3) Forgot Code\n4) Show total Presents\n"))
    if(choice==1 or choice==4):
        print("Plz Place your Thumb on the scanner to know your identification\n")
        isValid=validation()
        if isValid is True:
            user=identify()
            if(user):
                print(f'Welcome {user} !')
                if(choice==1):
                    markPresent(user)
                else:
                    showPresents(user)
        else:
            print("You are not a part of the Community Plz Register Your self or Contact The head")
    elif(choice==2 or choice==3):
        print('Welcome To the Stargent Robotics Community Here Our Motto is to Make Bots and TO make the Gyanni 3.0')