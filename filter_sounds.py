import os
import wave
import shutil

def filter_and_move_wav_files(source_directory, target_directory, max_duration_seconds):
    # Create the target directory if it doesn't exist
    os.makedirs(target_directory, exist_ok=True)
    
    # List all files in the source directory
    files = os.listdir(source_directory)
    
    # Filter out .wav files longer than max_duration_seconds and move them to the target directory
    for file in files:
        if file.endswith('.wav'):
            file_path = os.path.join(source_directory, file)
            with wave.open(file_path, 'rb') as wav_file:
                # Calculate the duration of the .wav file
                frames = wav_file.getnframes()
                sample_rate = wav_file.getframerate()
                duration_seconds = frames / sample_rate
                
                # Check if the duration exceeds the maximum allowed duration
                if duration_seconds > max_duration_seconds:
                    # Move the file to the target directory
                    target_file_path = os.path.join(target_directory, file)
                    shutil.move(file_path, target_file_path)

# Specify the source directory containing the .wav files
source_directory = 'audio/cis.whoi.edu/science/B/whalesounds/WhaleSounds'

# Specify the target directory to move the .wav files to
target_directory = 'whales_bytes'

# Specify the maximum allowed duration in seconds
max_duration_seconds = 3

# Filter and move .wav files longer than 3 seconds
filter_and_move_wav_files(source_directory, target_directory, max_duration_seconds)
