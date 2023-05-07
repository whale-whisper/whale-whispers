import os

# Define the path to the center_sounds directory
center_sounds_dir = 'data/center_sounds'

# Define a mapping from letters to audio file names
MAPPING = {}

files = sorted(os.listdir(center_sounds_dir))

def letter_to_audio_file():
    global MAPPING
    if len(MAPPING) > 0:
        return MAPPING

    # Define the mapping for letters a-z
    for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz '):
        audio_file_name = files[i]
        audio_file_path = os.path.join(center_sounds_dir, audio_file_name)
        MAPPING[letter] = audio_file_path

    return MAPPING

if __name__ == '__main__':
    # Test the mapping
    m = letter_to_audio_file()
    for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz '):
        print(i, letter, m[letter])
