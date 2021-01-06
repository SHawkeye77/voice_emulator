"""
    Samuel Hohenshell
    01/05/2021
"""

from helpers import split_string_and_clean, get_word_sounds, speak
import sys

def main():
    # Checking user input
    if (len(sys.argv) < 2):
        print("ERROR: Started incorrectly. Use the following format: ")
        print("    > python3 voice_emulator.py AUDIO_DIRECTORY")
        return -1
    
    # Storing audio directory
    audio_dir = sys.argv[1]

    # Printing instructions
    print()
    print(" -------------------------------------------------------------------------- ")
    print("| Welcome to my custom text-to-speech voice emulator!                      |")
    print("| Copy-paste or type a string of words below.                              |")
    print("| Rules:                                                                   |")
    print("|   - Write out numbers (e.g \"five hundred point six\" rather than \"500.6\") |")
    print("|   - No ellipsis (...)                                                    |")
    print(" -------------------------------------------------------------------------- ")

    # Gathering user input and formatting it correctly
    user_input = input("> ")
    words = split_string_and_clean(user_input)

    # Storing pronunciation of each word
    sounds = get_word_sounds(words)  # Each element is a list that represents the sounds of an individual word.

    # Playing the sounds
    retval = speak(sounds, audio_dir)

    return 0


if __name__ == '__main__':
    main()