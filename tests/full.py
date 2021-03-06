import importlib.util
__spec = importlib.util.spec_from_file_location("audiosegment", "../audiosegment.py")
asg = importlib.util.module_from_spec(__spec)
__spec.loader.exec_module(asg)
import os
import sys

#testsuites
import casa
import fft
import normalize
import read_from_file
import resample
import serde
import silence
import spectrogram
import trim
import vad
import visualize

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE:", sys.argv[0], os.sep.join("path to wave file.wav".split(' ')))
        exit(1)

    seg = read_from_file.test(sys.argv[1])

    # Print some information about the AudioSegment
    print("Information:")
    print("Channels:", seg.channels)
    print("Bits per sample:", seg.sample_width * 8)
    print("Sampling frequency:", seg.frame_rate)
    print("Length:", seg.duration_seconds, "seconds")

    resampled = resample.test(seg)
    #casa.test()
    normalized = normalize.test(resampled)
    serde.test(normalized)
    slices = trim.test(normalized)
    fft.test(normalized)
    spectrogram.test(normalized)
    silence.test(normalized)
    vad.test(normalized)
