"""
    Samuel Hohenshell
    Contains all helper functions for my voice emulator project
"""

import pronouncing               # Library for getting ARPAbet pronunciations
import re                        # For parsing input
import time                      # For sleeping between words
from playsound import playsound  # For playing audio


TIME_BETWEEN_WORDS = 0.5           # Number of seconds to pause between words
PAUSE_TOKEN        = "pause_here"  # The token we add to say that we should wait in the speech

def speak(sounds, audio_dir):
    print("Saying the following sounds: ")
    to_play  = []
    for word in sounds:
        # Deal with a punctuation pause
        if (word == PAUSE_TOKEN):
            to_play.append(PAUSE_TOKEN)
            continue
        phonemes = word.split(' ')
        for phoneme in phonemes:
            print(phoneme, end=" ")
            file = audio_dir + "/" + phoneme + ".mp3"
            to_play.append(file)

    print("",flush=True)

    for sound in to_play:
        if (sound == PAUSE_TOKEN):
            time.sleep(TIME_BETWEEN_WORDS)
        else:
            playsound(sound)

    return 0



# Split given string up to list based on delimiters below and then clean up all the words
def split_string_and_clean(user_input):
    pause_delimiters = [",", "!", "?", ":", ";", "."]
    
    # Splitting by delimiters that don't require a pause in speech
    word_list = re.split(r" |\n|\t|\"", user_input)

    # Adding a "pause_here" marker each time we hit a delimeter that causes a pause in speech
    idx = 0
    while (idx != len(word_list)):
        # If punctuation indicating pausing is detected, remove it and add a pause token
        if (word_list[idx][-1] in pause_delimiters):
            word_list[idx] = word_list[idx][:-1]
            word_list.insert(idx+1, PAUSE_TOKEN) 
            idx += 1
        idx += 1


    # Clean up any null characters
    clean = False
    rem1 = ''
    rem2 = ' '
    while (not clean):
        clean = True
        for word in word_list:
            if word == rem1:
                word_list.remove(rem1)
                clean = False
            elif word == rem2:
                word_list.remove(rem2)
                clean = False
    
    # Make everything lowercase
    word_list = [word.lower() for word in word_list]

    return word_list

def get_word_sounds(words):
    pronunciations = [] 
    # Going through each word in the list of words the user requested
    for word in words:
        # Dealing with any pauses
        if (word == PAUSE_TOKEN):
            pronunciations.append(PAUSE_TOKEN)
            continue

        # Getting the first pronunciation from the CMU pronunciations
        try:
            orig_pronun = pronouncing.phones_for_word(word)[0]
        except IndexError:
            print("Didn't recognize word \"" + word + "\". Skipping...")
            continue
        # Removing stress letters (without doing this would greatly increase number of necessary sounds for minimal return)
        updated_pronun = ""
        for letter in orig_pronun:
            if (not letter.isdigit()):
                updated_pronun += letter

        # Adding to our list of ARPAbet pronunciations
        pronunciations.append(updated_pronun)

    return pronunciations
