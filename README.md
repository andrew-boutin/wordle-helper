# Wordle Helper

A program that can be helpful when playing [Wordle](https://www.nytimes.com/games/wordle/index.html).

The program loads a set of all known words and trims it down to those matching the target length. Then it can further
remove words that contain letters that are known to not be in the target word. It can also remove words that do not have
a given letter at a given index in the word. Statistics are shown at each step to indicate how many matching words are
left, the probability of guessing the correct word, and the possible words can even be printed out.

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
    Removing words that contain invalid letters: ['r', 's', 't', 'l', 'n', 'e']
    Removing words that do not have the following letters at the respective index: {0: 'a', 4: 'o'}
    ------ Stats ------
    audio
    amoco
    amigo
    3 words found
    Chance of correct guess 33.33%
    ---- End Stats ----
