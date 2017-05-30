#!/usr/bin/env python

from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
import fileinput
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
# from nltk.corpus import stopwords


def openTextFile():
     TextFileData = askopenfilename()
     for l in fileinput.input(TextFileData):
          textArea.insert(END,l)
     updateCounterForDownloadedFile()

def closeApplication():
        root.destroy()

def openAboutWindow():
    aboutWindow = messagebox.showinfo("about", "Made with love in RSSU, 2017")

# def countNumberOfSentences(text):
#     return text.count("...")+text.count(". ")+text.count('!')+text.count('?')+text.count('.')
def countNumberOfSentences(text1):
    lines = text1
    tokenized_sents = [sent_tokenize(lines)]
    for  k in tokenized_sents:
        return(str(len(k)))
 
def updateCounter(event):              #обработчик событий 
    updateCounterForDownloadedFile()

def updateCounterForDownloadedFile():              #обработчик событий 
    textForCounting = textArea.get("1.0",END)
    sentenceCount = countNumberOfSentences(textForCounting)
    sentenceCount = str(sentenceCount)
    outputText = "Введите текст в поле\n" + "В тексте " + sentenceCount + " предложений"
    textCount.configure(text=outputText)    
 
root = Tk()
root.title("Счётчик предложений")

mainMenu = Menu(root)
root.config(menu=mainMenu)
mainMenuLine = Menu(mainMenu)
mainMenu.add_cascade(label="Options",menu=mainMenuLine)
mainMenuLine.add_command(label="Open file",command=openTextFile)
mainMenuLine.add_command(label="About", command=openAboutWindow)
mainMenuLine.add_command(label="Exit", command=closeApplication)
 
textCount = Label(root,width=60, font="14",        #плашка сверху
            text="Введите текст в поле\nВ тексте 0 предложений")

scry = Scrollbar( root, orient=VERTICAL )   #скроллбар
scry.pack( side = RIGHT, fill=Y )

textArea = Text(root,width=50,height=10,wrap=WORD,yscrollcommand=scry.set) #текстовое поле
 

 
textCount.pack()
textArea.pack( side = LEFT, fill = BOTH, expand = True )
scry.config( command = textArea.yview )

textArea.bind("<KeyPress>",updateCounter)

root.mainloop()