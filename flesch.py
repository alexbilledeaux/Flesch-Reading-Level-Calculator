def readFileIn(fileName: str) -> str:
    file = open('assets/' + fileName, 'r')
    content = file.read()
    file.close()
    content = content.encode('ascii', 'ignore')
    content = content.decode()
    content = content.replace("\n", " ")
    content = content.rstrip()
    return content

def isWhitespace(char: chr) -> bool:
    return char == ' '

def isPunctuation(char: chr) -> bool:
    punctuation = ".?!,;:()[]{}\""
    return char in punctuation   

def containsEndingPunctuation(string: str) -> bool:
    isPresent = False
    if ('.' in string) or ('!' in string) or ('?' in string):
        isPresent = True
    return isPresent

def isVowel(char: chr) -> bool:
    vowels = "aAeEiIoOuUyY"
    return char in vowels

def isConsonant(char: chr) -> bool:
    consonants = "qQwWrRtTpPsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM"
    return char in consonants

def isEllipses(index: int, content: str) -> bool:
    # Make sure we aren't going out of bounds
    i = index
    while len(content) - 1 > i and (isWhitespace(content[i]) or content[i] == '.'):
        i += 1
        if content[i] == '.':
            return True
    return False

def getWords(content: str, withPunctuation: bool):
    words = []
    tempWord = ""
    for i, char in enumerate(content):
        if not isPunctuation(char) and not isWhitespace(char):
            tempWord += char
        elif withPunctuation and (isPunctuation(char) or isWhitespace(char)):
            if isEllipses(i, content):
                if not isWhitespace(char):
                    tempWord += char
            elif not isEllipses(i, content):
                if isWhitespace(char) and tempWord != "":
                    words.append(tempWord)
                    tempWord = ""
                elif isPunctuation(char):
                    tempWord += char
                    words.append(tempWord)
                    tempWord = ""
        elif not withPunctuation and tempWord != "":
            words.append(tempWord)
            tempWord = ""
    if tempWord != "":
        words.append(tempWord)
    return words

# A sentence is defined as at least one word followed by ending punctuation.
def getSentences(content: str):
    sentences = []
    tempSentence = ""
    words = getWords(content, True)
    for i, word in enumerate(words):
        # Verify that the sentence contains at least one word
        tempSentence = tempSentence + " " + word
        if containsEndingPunctuation(word) and word[0] != '.':
            # Check for special cases
            if '...' in word:
                pass
            elif word == 'Mr.' or word == 'Mrs.' or word == 'Dr.' or word == 'etc.' or word == 'a.' or word == 'p.' or word == 'm.':
                pass
            else:
                sentences.append(tempSentence)
                tempSentence = ""
            
    return sentences

# A syllable is defined as any word that begins with a vowel, or any vowel following following a consonant. Exception: 'the'
def getNumSyllables(content: str) -> int:
    words = getWords(content, False)
    syllables = 0
    for word in words:
        for i, char in enumerate(word):
            # If the first letter is a vowel, we're starting a syllable.
            if i == 0 and isVowel(char):
                syllables += 1
            # Any vowel after a consonant, other than 'e' at the end of a word.
            elif i > 0 and isVowel(char) and isConsonant(word[i-1]) and not (char == 'e' and i == len(word) - 1):
                syllables += 1
            # Special 'the' case
            elif word == "the":
                syllables += 1
    return syllables

def getFleschIndex(content: str) -> float:
    sentences = getSentences(content)
    words = getWords(content, False)
    return 206.835 - 84.6 * (getNumSyllables(content)/len(words)) - 1.015 * (len(words)/len(sentences))