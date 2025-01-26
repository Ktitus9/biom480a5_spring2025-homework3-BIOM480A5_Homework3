import random, pickle
import numpy as np
import matplotlib.pyplot as plt

# generate a random integer between 1 and 1000
n2 = random.randint(1,1000)
seq = ''
for i in range(1000):
    seq += random.choice('ACGT')
with open('data3.txt', 'w') as file:
    file.write(seq)

q1 = 'xxx'
q4 = 'XXX'
q8 = 'XXX'

welcomeMessage = '''Welcome to Homework 3!
    This homework is designed to test your understanding of packages, reading and writing files, 
    using Pandas, and plotting in Python. Please answer the questions in the homework by filling 
    in the variables q1, q2, etc. Each time you fill in a variables, run the saveResults('q',q) 
    function to save your answers. Make sure not to change the variable names or overwrite your 
    answers in subsequent questions!

    Please Note -- this assignment has several questions that will require you to update your 
    README.md file with the answers. Please be sure to do this before submitting your assignment.
    Any requested figures should be saved as .png files in your repository and should be added
    to your README.md file as well.  All figures should include captions that describe the figure, 
    labels for the axes (if applicable), and a figure legend (if applicable).

    Note, you might need to install the matplotlib and pandas packages to complete this homework.
    You should know how to do this by now, but if you need a refresher, please refer to the
    example notebooks in this module.
    
    Good luck!'''

fnDat = 'Hwk3Data.pkl'
dataDict = {'n2':n2}
with open(fnDat, 'wb') as file:
    pickle.dump(dataDict, file)

fn = 'Hwk3Answers.pkl'
answerDict = {'q1':q1, 'q4':q4, 'q8':q8}
with open(fn, 'wb') as file:
    pickle.dump(answerDict, file) 

def saveResults(qn,qa):
    # load the answers
    with open(fn, 'rb') as file:
        answerDict = pickle.load(file)

    answerDict[qn] = qa
    
    with open(fn, 'wb') as file:
        pickle.dump(answerDict, file)    