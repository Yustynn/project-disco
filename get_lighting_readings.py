from random import random

# don't worry about the following 2 lines, they just generate sample inputs
pitches = [random()*100 for i in range(200)]
volumes = [1 for i in range(200)]

# input volumes (list of 200)
# chunk it into chunks of 100, spaced by 10 ( 0-100, 10-110, ... 100-20[0 )
# apply rms to each chunk
# return new list of rms'd chunks

def rms(ls):
    total = 0
    for n in ls:
        total += n**2

    mean = total / len(ls)
    # mean = total / 200

    return mean**0.5


CHUNK_SIZE = 100
STEP = 10

def get_lighting_readings_vol_only(volumes):
    # STEP 1: CHUNKING

    num_volumes = len(volumes)
    # 10
    # 20
    # 30
    # ... num_volumes - CHUNK_SIZE

    chunks = []
    for i in range(0, (num_volumes - CHUNK_SIZE)/10 + 1):
        start = i*10
        end = start + CHUNK_SIZE

        chunk = volumes[start:end]
        chunks.append(chunk)

    # STEP 2: Apply RMS to each chunk
    values = []
    for chunk in chunks:
        value = rms(chunk)
        values.append(value)

    return values

def get_lighting_readings(pitches, volumes):
    num_volumes = len(volumes)
    num_pitches = num_volumes

    values = []
    for i in range(0, (num_volumes - CHUNK_SIZE)/10 + 1):
        start = i*10
        end = start + CHUNK_SIZE

        pitch_chunk = pitches[start:end]
        vol_chunk = volumes[start:end]

        pitch_rms = rms(pitch_chunk)
        volume_rms = rms(vol_chunk)
        value = [pitch_rms, volume_rms]

        values.append(value)

    return values

values = get_lighting_readings(pitches, volumes)

print(values, len(values))
