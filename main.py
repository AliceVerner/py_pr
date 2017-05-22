#!/usr/bin/env python

from tkinter import *

def countNumberOfSentences(text):
    return text.count('. ')+text.count('! ')+text.count('? ')
 
def updateCounter(event):              #обработчик событий 
    textForCounting = textArea.get("1.0",END)
    sentenceCount = countNumberOfSentences(textForCounting)
    sentenceCount = str(sentenceCount)
    outputText = "Введите текст в поле и нажмите Enter\n" + "В тексте: " + sentenceCount + "предложений."
    textCount.configure(text=outputText)
 
root = Tk()
 
textCount = Label(root,width=60, font="14",        #плашка сверху
            text="Введите текст в поле и нажмите Enter")

scry = Scrollbar( root, orient=VERTICAL )   #скроллбар
scry.pack( side = RIGHT, fill=Y )

textArea = Text(root,width=50,height=10,wrap=WORD,yscrollcommand=scry.set) #текстовое поле
 

 
textCount.pack()
textArea.pack( side = LEFT, fill = BOTH, expand = True )
scry.config( command = textArea.yview )

textArea.bind("<Return>",updateCounter)
root.mainloop()