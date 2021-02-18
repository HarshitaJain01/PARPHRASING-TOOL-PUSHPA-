import threading

import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from tkinter import *
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from ttkthemes import themed_tk
from tkinter import ttk

root = Tk()

messagebox.showinfo("Welcome", "ParaPhrashing Tool By Antaryami Coders")  # to show the main GUI
nltk.download('wordnet')  # We Have Downloaded A Function in nltk using nltk.download("Function Name")

words_not_to_be_changed = ["or", "is", "of", "for", "this",
                           "and", "am", "a", "that", "in", "at", "there", "that", "are", 'as', 'he', 'be', 'does', ]


# These Are The Words That Do not Take Part In ParaPhrashing Tool

def check_staticwords(token):  # Declaring a function that cofirms whenever a words provides in
    # words_not_to_be_changed comes it doesn't gets changed
    if words_not_to_be_changed.count(token.lower()) > 0 or token.isupper():
        return False
    return True


def Paraphrase(array):  # declaring the function of the tool
    newTokenArray = []
    tempArray = []

    for token in array:
        if check_staticwords(token):
            data = wordnet.synsets(token)
            for synonym in data:
                for lemma in synonym.lemmas():
                    if lemma.name().lower() != token.lower():
                        tempArray.append(lemma.name())

        if len(tempArray) > 0:
            # pick the first item
            newTokenArray.append(tempArray[0])
            tempArray.clear()
        else:
            newTokenArray.append(token)

    return newTokenArray


a = tk.simpledialog.askstring("Para", "Enter The Para You Want To Phrasing")  # using tkinter we devloped our main
# dialog box
tokens = word_tokenize(a)

result = Paraphrase(tokens)


def convert(s):  # For Converting The OutCome List As A String
    # initialization of string to ""Y
    new = " "

    # traverse in the string
    for x in s:
        new += x + " "

        # return string
    return new


tk.messagebox.showinfo("Your Para Is Phrased:-", convert(result))
print(convert(result))

root.mainloop()
