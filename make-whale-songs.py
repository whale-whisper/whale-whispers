#!/usr/bin/env python3
import os
import sys
import json

def main():
    songs = json.load(open('whale-songs.json'))
    for song in songs:
        # ensure the sentence is passed as one string argument
        os.system(f'./sentence-to-whale-song.py "{song}"')

if __name__ == '__main__':
    main()
