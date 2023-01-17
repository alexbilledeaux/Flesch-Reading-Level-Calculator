import flesch
import matplotlib.pyplot as plt
import numpy as np
import re

"""
Calculate a rolling Flesch index for a given array of strings,
by incrementally concatenating each string and calculating the new Flesch index.
"""
def getRollingFleschIndex(sentences):
    tempContent = ""
    rollingFleschIndex = []
    for sentence in sentences:
        tempContent += sentence
        rollingFleschIndex.append(flesch.getFleschIndex(tempContent))
    return rollingFleschIndex

sourceFiles = ["example.txt"]
for file in sourceFiles:
    content = flesch.readFileIn(file)
    sentences = flesch.getSentences(content)
    rollingFleschIndex = getRollingFleschIndex(sentences)
    yaxis = np.array(rollingFleschIndex)
    plt.plot(yaxis)
        
plt.legend(sourceFiles)
plt.title("Rolling Flesch Index by Sentence")
plt.show()
