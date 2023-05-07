# mixes audio files together
import os
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


def crossfade_audio_files(input_files, output_file, crossfade_duration=1):
    # Combine the input files into a single concatenated stream
    streams = [ffmpeg.input(file) for file in input_files]
    stream = ffmpeg.concat(*streams, v=0, a=1)

    # Add crossfade effect between audio files
    combined = None
    for i, s in enumerate(streams[:-1]):
        # Duration of the current audio
        duration = float(ffmpeg.probe(input_files[i])['format']['duration'])

        # Ensure crossfade_duration is less than or equal to the shortest audio duration
        actual_crossfade_duration = min(duration, crossfade_duration)

        # Calculate fade out start time for the current audio
        fade_out_start = max(0, duration - actual_crossfade_duration)

        # Apply fade out effect to the current audio
        faded_out = s.filter('afade', type='out', start_time=fade_out_start, duration=actual_crossfade_duration)

        # Apply fade in effect to the next audio
        faded_in = streams[i + 1].filter('afade', type='in', duration=actual_crossfade_duration)

        # Mix the faded audios
        mixed = ffmpeg.filter([faded_out, faded_in], 'amix')

        if combined is None:
            combined = mixed
        else:
            # Concatenate the current mixed audio with the previous ones
            combined = ffmpeg.concat(combined, mixed, v=0, a=1)

    # Save the crossfaded audios to the output file
    ffmpeg.output(combined, output_file).run()

if __name__ == '__main__':
    files = [
        '6102101F_segment0_3sec.wav',
        '7500103V_segment0_3sec.wav',
        '7501400X_segment0_3sec.wav',
    ]
    paths = [f'data/center_sounds/{f}' for f in files]
    #concatenate_audio_files(paths, 'concatenated.wav')
    #mix_audio_files(paths, 'mixed.wav', [1, 1])
    crossfade_audio_files(paths, 'crossfaded.wav', 1)
