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
    letter_to_audio_file()
    print(MAPPING['a'])  # Output: center_sounds/train0.aiff
    print(MAPPING['z'])  # Output: center_sounds/train25.aiff
    print(MAPPING[' '])  # Output: center_sounds/train26.aiff
