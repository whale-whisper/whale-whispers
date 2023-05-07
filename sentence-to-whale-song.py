#!/usr/bin/env python3
# Creates audio output from input sentance.
import sys

from process import letter_to_audio_file
from mixer import concatenate_audio_files

def make_whale_noises(sentance):
    
    # make output name all lowercase and no spaces:
    output_filename = 'output/'+sentance.lower().replace(" ", "_") + ".wav"

    files = []
    # create audio file for each letter in sentance:
    for letter in sentance:
        f = letter_to_audio_file().get(letter, None)
        if f:
            files.append(f)

    # combine audio files into one:
    concatenate_audio_files(files, output_filename)

if __name__ == "__main__":
    make_whale_noises(sys.argv[1])
