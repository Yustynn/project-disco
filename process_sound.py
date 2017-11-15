# This is a simple demonstration on how to stream
# audio from microphone and then extract the pitch
# and volume directly with help of PyAudio and Aubio
# Python libraries. The PyAudio is used to interface
# the computer microphone. While the Aubio is used as
# a pitch detection object. There is also NumPy
# as well to convert format between PyAudio into
# the Aubio.
import aubio
import numpy as np
import pyaudio
import sys

from collections import namedtuple

SoundReading = namedtuple('SoundReading', ['pitch', 'volume'])

# Some constants for setting the PyAudio and the
# Aubio.
BUFFER_SIZE             = 2048
CHANNELS                = 1
FORMAT                  = pyaudio.paFloat32
METHOD                  = "default"
SAMPLE_RATE             = 44100
HOP_SIZE                = BUFFER_SIZE//2
PERIOD_SIZE_IN_FRAME    = HOP_SIZE

def main(args):

    pA = pyaudio.PyAudio()
    mic = pA.open(format=FORMAT, channels=CHANNELS,
        rate=SAMPLE_RATE, input=True,
        frames_per_buffer=PERIOD_SIZE_IN_FRAME)

    pDetection = aubio.pitch(METHOD, BUFFER_SIZE,
        HOP_SIZE, SAMPLE_RATE)
    pDetection.set_unit("Hz")
    pDetection.set_silence(-40)

    readings = []

    while True:
        data = mic.read(PERIOD_SIZE_IN_FRAME)
        samples = np.fromstring(data,
            dtype=aubio.float_type)
        pitch = pDetection(samples)[0]
        volume = np.sum(samples**2)/len(samples)
        volume = "{:2f}".format(volume*1E4)

        readings.append( SoundReading(pitch, volume) )

        print( "Vol: {:10}    ||||||     Pitch: {:<10}".format(volume, pitch) )

if __name__ == "__main__": main(sys.argv)
