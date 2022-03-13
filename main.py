# A set of English words containing lower-case letters; with punctuation.
from english_words import english_words_lower_set
import re, json

# TODO: Account for letters that are known to be in the word, but at an unknown position.
# TODO: Make interactive, take in input, clean up global variables.
# A list of letters that are known to not be in the word.
known_invalid_letters = ['r', 's', 't', 'l', 'n', 'e']
# A dict of word index with known letter.
known_position_letters = {0: 'a', 4: 'o'}
word_set = english_words_lower_set
print()
print("------ Start ------")
print(str(len(word_set)) + " known words to process")
word_length = 5

# A pattern for only X lowercase letters.
pattern = re.compile("^[a-z]{" + str(word_length) + "}$")

# Base try which is a tuple of a dictionary and a boolean. The boolean indicates if this level is a word ending.
wordTry = ({}, False)

# Prints out stats such as words found, chance of guessing the correct word, and total matching words.
def printStats(print_words=False):
    print("------ Stats ------")
    totalWords = walkTry(wordTry, "", print_words)
    guessChangePercentage = 100 / totalWords
    print(str(totalWords) + " words found")
    print("Chance of correct guess " + str(round(guessChangePercentage, 2)) + "%")
    print("---- End Stats ----")

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

# Recursively add a word to the try.
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

def findWordsOfGivenLength():
    print("Finding words of length " + str(word_length))

    # Build up our try of words from a known word set to start with.
    for word in word_set:
        # Skip words that do not match our pattern.
        if not pattern.match(word):
            continue

        # Add each matching word to our try.
        addWordHelper(wordTry, word)

# Remove words with invalid letters and that don't have the correct known letter at a given index.
def applyKnownInfo(invalidLetters=[], known_position_letters=[]):
    print("Removing words that contain invalid letters: " + str(invalidLetters))
    print("Removing words that do not have the following letters at the respective index: " + str(known_position_letters))
    applyKnownInfoHelper(invalidLetters, wordTry, 0)

# Helper for recursively removing words with invalid letters and that don't have the correct known letter at a given index.
def applyKnownInfoHelper(invalidLetters, curWordTry, curIndex):
    # Track what letters/sub-trys to remove along the way.
    letters_to_delete = []

    # Check the current level's letters for invalid ones.
    for letter, innerTry in curWordTry[0].items():
        # See if the letter is invalid.
        if letter in invalidLetters:
            # Store it for later as we can't modify during iteration.
            letters_to_delete.append(letter)
            continue

        # See if we know the correct letter for the current index.
        if curIndex in known_position_letters:
            correctLetter = known_position_letters[curIndex]

            # Track this letter for removal if it doesn't match the known good letter for the index.
            if letter != correctLetter:
                letters_to_delete.append(letter)
                continue

        # Recurse to check sub-try since so far it's still valid.
        applyKnownInfoHelper(invalidLetters, innerTry, curIndex + 1)

    # Remove all found invalid parts.
    for letter in letters_to_delete: del curWordTry[0][letter]

findWordsOfGivenLength()
# The initial try is quite large so don't print it out by default.
#printTry()
# Print out some stats on our current try.
printStats()
#printStats(print_words=True)

applyKnownInfo(known_invalid_letters, known_position_letters)
#printStats()
printStats(print_words=True)
