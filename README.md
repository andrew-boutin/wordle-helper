# Wordle Helper

A program that can be helpful when playing [Wordle](https://www.nytimes.com/games/wordle/index.html).

* See the number of valid words given a state.
* See the probability of guessing the correct word given a state.
* See the valid word choices given a state.

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
