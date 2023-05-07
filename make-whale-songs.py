#!/usr/bin/env python3
import os
import csv
import sys
import json

def main():
    f = open('output/metadata.csv', 'w')
    o = csv.writer(f)
    o.writerow(['file_name', 'transcription'])
    songs = json.load(open('whale-songs.json'))
    for song in songs:
        output_filename = song.lower().replace(" ", "_") + ".wav"
        o.writerow([output_filename, song])
        # ensure the sentence is passed as one string argument
        os.system(f'./sentence-to-whale-song.py "{song}"')

if __name__ == '__main__':
    main()
