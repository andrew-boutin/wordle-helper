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
