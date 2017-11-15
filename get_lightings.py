from random import random

CHUNK_SIZE = 100

def rms(l):
    total = 0
    for el in l:
        total += el**2

    return (total / len(l))**0.5

def get_lightings(pitches, volumes):
    pitch_segments = []
    volume_segments = []
    for start in range(0, len(pitches) - CHUNK_SIZE, 10):
        end = start + CHUNK_SIZE
        pitch_segments.append( pitches[start:end] )
        volume_segments.append( volumes[start:end] )

    intensities = []
    for volume_segment in volume_segments:
        intensities.append( rms(volume_segment) )

    return intensities

def better_get_lightings(pitches, volumes):
    lightings = []

    for start in range(0, len(pitches) - CHUNK_SIZE, 10):
        end = start + CHUNK_SIZE
        lighting = ( rms(pitches[start:end]), rms(volumes[start:end]) )
        lightings.append(lighting)

    return lightings


get_rand_vals = lambda: [ random()*100 for i in range(200) ]
pitches, volumes = get_rand_vals(), get_rand_vals()

# print(get_lightings(pitches, volumes))
volumes = [1 for i in range(200)]

print(get_lightings(pitches, volumes))
print(better_get_lightings(pitches, volumes))
