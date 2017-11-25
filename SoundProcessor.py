from math import exp
import numpy as np

CHUNK_SIZE = 100
STEP_SIZE = 10

SIZE_THRESHOLD = 5000

PITCH_WEIGHT = 1
VOLUME_WEIGHT = 1 

class SoundProcessor:
    """
    >>> sp = SoundProcessor()
    """
    def __init__(self):
        self.raw_pitches = []
        self.raw_volumes = []

        self.pitches = []
        self.volumes = []

    # @TODO: Better naming
    def process_raw_input(self, raw_pitch, raw_volume):
        raw_pitches = self.raw_pitches
        raw_volumes = self.raw_volumes

        raw_pitches.append(raw_pitch)
        raw_volumes.append(raw_volume)

        if len(raw_pitches) % STEP_SIZE == 0:
            self.prune_check()
            self.process_raw_readings()

        if len(raw_pitches) > SIZE_THRESHOLD:
            self.raw_pitches == raw_pitches[-CHUNK_SIZE:]
            self.raw_volumes == raw_volumes[-CHUNK_SIZE:]

    def prune_check(self):
        raw_pitches = self.raw_pitches
        raw_volumes = self.raw_volumes
        pitches = self.pitches
        volumes = self.volumes

        if len(raw_pitches) > SIZE_THRESHOLD:
            assert len(raw_pitches) == len(raw_volumes)

            self.raw_pitches == raw_pitches[-CHUNK_SIZE:]
            self.raw_volumes == raw_volumes[-CHUNK_SIZE:]

        if len(pitches) > SIZE_THRESHOLD:
            assert len(raw_pitches) == len(raw_volumes)

            self.pitches == pitches[-CHUNK_SIZE:]
            self.volumes == volumes[-CHUNK_SIZE:]

    def process_raw_readings(self):
        processed_pitch = self.moving_rms( self.raw_pitches )
        processed_volume = self.moving_rms( self.raw_volumes )

        self.pitches.append(processed_pitch)
        self.pitches.append(processed_volume)
        print(processed_pitch, processed_volume)

    def get_control_values(self):
        pitch_rms  = self.moving_rms( self.pitches )
        volume_rms = self.moving_rms( self.volumes )

        pitch_control = sigmoid( PITCH_WEIGHT * pitch_rms )
        volume_control = sigmoid( VOLUME_WEIGHT * volume_rms )

        return pitch_control, volume_control

    def sigmoid(self, x):
        """
        >>> sp.sigmoid(0)
        0.5
        >>> round( sp.sigmoid(3), 3 )
        0.953
        """
        numerator = 1
        denominator = 1 + exp(-x)

        return numerator / denominator

    def rms(self, values):
        """
        >>> values = list(range(100))
        >>> round( sp.rms(values), 3 )
        57.302
        """
        return np.mean( np.square(values) )**0.5
    
    def moving_rms(self, values, thresh=CHUNK_SIZE):
        """
        Test threshold
        >>> values = list(range(100))
        >>> round( sp.moving_rms(values, thresh=5), 3 )
        97.01
        >>> round( sp.moving_rms(values, thresh=6), 3 )
        96.515

        Test len values < threshold
        >>> round( sp.moving_rms([5, 7], thresh=6), 3 )
        6.083

        Test empty list
        >>> sp.moving_rms([])
        """
        if not values: return None

        return self.rms( values[-thresh:] )


    # actually, don't need this
    def moving_average(self, values, thresh=CHUNK_SIZE):
        """
        Test threshold
        >>> values = list(range(100))
        >>> sp.moving_average(values, thresh=5)
        97.0
        >>> sp.moving_average(values, thresh=6)
        96.5
        >>> sp.moving_average(values, thresh=100)
        49.5

        Test len values < threshold
        >>> sp.moving_average([5, 7], thresh=6)
        6.0
        """
        if not values: return None

        return np.mean( values[-thresh:] )


sp = SoundProcessor()



if __name__ == '__main__':
    from doctest import testmod
    testmod()
