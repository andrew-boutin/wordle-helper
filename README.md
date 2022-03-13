# Wordle Helper

A program that can be helpful when playing [Wordle](https://www.nytimes.com/games/wordle/index.html).

The program loads a set of all known words and trims it down to those matching the target length. Then it can further
remove words that contain letters that are known to not be in the target word. It can also remove words that do not have
a given letter at a given index in the word. It also can rule out words that don't contain letters known to be in the
target word but at an unknown position or contain a letter known to be in the target word but at an index where we know
it's not there. Statistics are shown at each step to indicate how many matching words are left, the probability of
guessing the correct word, and the possible words can even be printed out.

Really I just wanted to play around with Python scripting and using a Try since it'd been a while.

## Requirements

* [virtualenv](https://pypi.org/project/virtualenv/)

## Setup

    virtualenv -p python3 wordle-helper-venv
    source wordle-helper-venv/bin/activate
    pip install -r requirements.txt

## Run

    source wordle-helper-venv/bin/activate
    python3 main.py

## Teardown

    deactivate

## Example

    (wordle-helper-venv) aboutin@aboutin-mac wordle-helper % python main.py
    ------ Start ------
    25480 known words to process
    Finding words of length 5
    ------ Stats ------
    3194 words found
    Chance of correct guess 0.03%
    ---- End Stats ----
    Removing words that contain letters known to not be in the word: lump
    Removing words that do not have the following letters at the respective index: {1: 'a'}
    Removing words that either don't contain all of the letters known to be in the word at an unknown location or contain a letter in the target word at an index we know it's not at: {0: 'z'}
    ------ Stats ------
    kazoo
    razor
    jazzy
    3 words found
    Chance of correct guess 33.33%
    ---- End Stats ----
