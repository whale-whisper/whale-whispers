import os

# Define the path to the center_sounds directory
center_sounds_dir = 'center_sounds'

# Define a mapping from letters to audio file names
letter_to_audio_file = {}

# Define the mapping for letters a-z
for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
    audio_file_name = f'train{i}.aiff'
    audio_file_path = os.path.join(center_sounds_dir, audio_file_name)
    letter_to_audio_file[letter] = audio_file_path

# Define the mapping for the space character
audio_file_name = f'train26.aiff'
audio_file_path = os.path.join(center_sounds_dir, audio_file_name)
letter_to_audio_file[' '] = audio_file_path

# Test the mapping
print(letter_to_audio_file['a'])  # Output: center_sounds/train0.aiff
print(letter_to_audio_file['z'])  # Output: center_sounds/train25.aiff
print(letter_to_audio_file[' '])  # Output: center_sounds/train26.aiff
