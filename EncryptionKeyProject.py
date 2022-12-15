#python3 EncryptionKeyProject.py
#Imports all neccesary things
import sys
import random
import math
import tkinter as tk
from tkinter import messagebox

#Creates a list with the alphabet
alphabetLowerCase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#Creates an empty string
finalEntry = ""
#Creates an empty list
splitUpLetters = []
#Creates an empty list
combinedLettersList = []
#Creates an empty list
getTheMessage = []

#This function randomizes the order of the alphabet to create a unique key for each time the program is run
def GetKey():
    global finalNum #Sets the variable to global so it can be used outside function
    finalNum = (random.sample(alphabetLowerCase,k=26)) #Randomizes list order
    messagebox.showinfo("Here is your unique key", finalNum) #Creates a popup message box to show that the user has created a unique key
    gettingKey.pack_forget() #Hides the button so the user does not click it again (Program will error)
    return finalNum #Returns the list with randomized key

#A function that takes in the string of randomized words and splits them up into a list
def wordToLetterSplitter(stringEntry):
    for y in stringEntry:
        splitUpLetters.append(y) #Adds each letter into a list individually
    swapLetters(splitUpLetters) #Calls another function (go to swapLetters to see what it does line 47)

#Function that pulls the users message that they typed into the entry boxed
def getAMessage():
    global finalEntryCopy #Sets the variable to global so it can be used outside function
    messagebox.showinfo("Message saved!", "Click OK and then the Translate a message button!") #Creates a popup message box to show the user that their message has been saved
    finalEntry = entry.get() #Sets the entry to a variable
    finalEntryCopy = finalEntry #Sets the entry to a variable
    entry.delete(0,len(finalEntry)) #Deletes what is in the entry box
    entry.pack_forget() #Hides the entry box so the uder does not enter another message (will result in an error)
    entryGreeting.pack_forget() #Hides the label so the user does not see it
    creatingAMessage.pack_forget() #Hides the button so the user does not click it again (Program will error)
    return wordToLetterSplitter(finalEntryCopy) #Calls another function (go to wordToLetterSplitter to see what it does line 29)

#Function that swaps the letters of the original message that the user inputed and translates to encrypted message with unique key that was created
def swapLetters(newList):
    global getTheMessage #Sets the variable to global so it can be used outside function
    getTheMessage = newList #Sets the entry to a variable
    for x in range(len(getTheMessage)):
        for m in range(len(alphabetLowerCase)):
            if (getTheMessage[x].lower() == alphabetLowerCase[m]): #Checks alphabet and switches with new letter
                getTheMessage[x] = finalNum[m]
                break
    return combineLetterToWords(getTheMessage) #Calls another function (go to combineLetterToWords to see what it does line 58)

#Function that puts the letters from a list into one string entry
def combineLetterToWords(listInput):
    finalWordd = "" #Creates an empty string
    combinedLettersList = listInput #Sets the entry to a variable
    for length in range(len(combinedLettersList)):
        finalWordd = finalWordd + combinedLettersList[length] #Combines letters
    return finalWordd #Returns the string

#Function that makes the key readable to the user in a simple string
def keyMaker(key):
    wordString = "" #Creates empty string
    for lengthX in range(len(key)):
        wordString = str(wordString) +" " + str(key[lengthX]) #Iterates through list and combines it into a string
    str(wordString) #Converts message to string
    return wordString

#Function that makes the message visable to the user and translates the encrypted message
def TranslateMessageFinal():
    alphabetStringOG = alphabetLowerCase
    alphabetStringNEW = finalNum
    #Creates a popup message box to show that the user that their message has been translated
    messagebox.showinfo("Here is your message!", message =  "Old message: \n"+ finalEntryCopy + "\n\nNew message: \n"+ combineLetterToWords(getTheMessage) +"\n\nAlphabet then the New Key: \n\n" + keyMaker(alphabetStringOG) + "\n\n" + keyMaker(alphabetStringNEW))
    sys.exit() #Stops program after the user clicks ok after seeing their message

window = tk.Tk() #Calls the window to run
#Calls the label "greeting"
greeting = tk.Label(text="Hello, please press the top button first. GO IN ORDER FROM TOP TO BOTTOM!\nThis code was created to encrypt messages, the program will close once you press OK on the last button!\nCreated by Spencer Mendelsohn")
#Calls the button to "Create a key"
gettingKey = tk.Button(text="Create a new key!",width=50,height=10, bg="white",activeforeground = "blue", fg="black", command=GetKey)
#Calls the label to "Enter the message"
entryGreeting = tk.Label(text="Enter your message below!")
#Calls the entry so user can type in their message
entry = tk.Entry(window,bg="white",fg="black", width = 50)
#Calls the button to "Save their message"
creatingAMessage = tk.Button(text="Click here when your message is finished below!",width=50,height=10, bg="white",activeforeground = "blue", fg="black", command=getAMessage)
#Calls the button to "Translate their message"
buttonTwo = tk.Button(text="Translate your message!",width=50,height=10, activeforeground = "blue", fg="black", command = TranslateMessageFinal)

window.geometry("1000x1000") #Resizes the window to fit the whole screen
greeting.pack() #Makes the label visable by "packing" it
gettingKey.pack(padx = 100,pady=10) #Makes the button visable by "packing" it and spacing it out
creatingAMessage.pack(padx = 100,) #Makes the button visable by "packing" it and spacing it out
entryGreeting.pack() #Makes the label visable by "packing" it
entry.pack() #Makes the entry box visable by "packing" it
buttonTwo.pack(padx = 100,pady=10) #Makes the button visable by "packing" it and spacing it out
window.mainloop() #Runs everything so the buttons and labels are visable
