import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
text_file = open("лул.txt", "r")
lines = text_file.readlines()
x=0
tokenized_words = [word_tokenize(i) for i in lines]
for i in tokenized_words:

    # print(i) #array contain with tokens
    # print(str(len(i))) #word count

    for j in i:
        if j== 'words': #simple algo for count number of 'words' to be count
            x = x+1

tokenized_sents = [sent_tokenize(k) for k in lines]

for  k in tokenized_sents:
    # print("Sentences"+str(k)) #array contain with sentences
    print("number of sentences "+str(len(k))) #number of sentences

print("number of word"+str(x))
print("Probability of 'word' in text file "+str(x/len(i)))