# A set of English words containing lower-case letters; with punctuation.
from english_words import english_words_lower_set
import re, json

# A pattern for only 5 lowercase letters.
pattern = re.compile("^[a-z]{5}$")

# Base try which is a tuple of a dictionary and a boolean. The boolean indicates if this level is a word ending.
wordTry = ({}, False)

# Prints out stats such as words found, chance of guessing the correct word, and total matching words.
def printStats(print_words=False):
    totalWords = walkTry(wordTry, "", print_words)
    guessChangePercentage = 100 / totalWords

    print("------ Words ------")
    print(str(totalWords) + " words found")
    print("Chance of correct guess " + str(round(guessChangePercentage, 2)) + "%")
    print("---- End Words ----")

# Recursive helper for printing words and tallying up the total number of them.
def walkTry(curWordTry, prefix, print_words):
    curTotal = 0

    if curWordTry[1]:
        if print_words:
            print(prefix)
        return 1

    for key, value in curWordTry[0].items():
        curTotal += walkTry(value, prefix + key, print_words)

    return curTotal

# Prints the current state of the try.
def printTry():
    print("------ Try ------")
    print(json.dumps(wordTry, sort_keys=True, indent=4))
    print("---- End Try ----")

# Adds a word to the try.
def addWord(word):
    addWordHelper(wordTry, word)

# Recursive helper for adding a word to the try.
def addWordHelper(curTry, curWord):
    # Sanity check no empty input.
    if len(curWord) == 0:
        return

    curLetter = curWord[0]
    nextWord = curWord[1:]

    # When a new letter is encountered initialize a try for it.
    if curLetter not in curTry[0]:
        curTry[0][curLetter] = ({}, False)

    # If we've reached a word ending then flag it and recurse up.
    if len(nextWord) == 0:
        tmpList = list(curTry[0][curLetter])
        tmpList[1] = True
        curTry[0][curLetter] = tuple(tmpList)
        return

    # Recurse down into the appropriate try with the remainder of the word.
    addWordHelper(curTry[0][curLetter], nextWord)

# Build up our try of 5 letter words from a known word set to start with.
for word in english_words_lower_set:
    # Skip words that do not match our pattern.
    if not pattern.match(word):
        continue

    # Add each matching word to our try.
    addWordHelper(wordTry, word)

# Pretty formatting.
print()
# The initial try is quite large so don't print it out by default.
#printTry()
# Print out some stats on our current try.
printStats()
#printStats(print_words=True)