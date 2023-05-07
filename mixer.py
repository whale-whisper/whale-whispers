# mixes audio files together
import ffmpeg

def concatenate_audio_files(input_files, output_file):
    # Create a list of input streams
    input_streams = []
    for file in input_files:
        input_streams.append(ffmpeg.input(file))
    # Concatenate audio files using the concat filter
    concatenated_audio = ffmpeg.concat(*input_streams, v=0, a=1)
    # Output the concatenated audio to the output file
    (
        ffmpeg.output(concatenated_audio, output_file)
        .overwrite_output()
        .run()
    )

def mix_audio_files(input_files, output_file, weights):
    # Create a list of input streams
    input_streams = []
    for file in input_files:
        input_streams.append(ffmpeg.input(file))
    # Mix audio files using the amix filter
    mixed_audio = ffmpeg.filter(input_streams, 'amix', inputs=len(input_files), duration='longest', dropout_transition=0, weights=weights)
    # Output the mixed audio to the output file
    (
        ffmpeg.output(mixed_audio, output_file)
        .overwrite_output()
        .run()
    )


if __name__ == '__main__':
    files = ['train1.aiff', 'train2.aiff', 'train3.aiff']
    paths = [f'center_sounds/{f}' for f in files]
    concatenate_audio_files(paths, 'concatenated.wav')
    mix_audio_files(paths, 'mixed.wav', [1, 1])
