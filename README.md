# What is this
Project Disco is part of the IEEE/3DC Project Jarvis collaboration.

The aim is to create room-scale lighting that changes in hue and brightness to visualize live sound. The sound and the light are completely detached, meaning that the sound can be coming from anywhere in the world (with proper equipment setup) and the lights will still function in reaction to that sound.

# Circuitry
Note the need for an external power source for the Neopixels (there are too many for the Raspberry Pi to power on its own)

Components are:
- Raspberry Pi
- Level converter
- Power supply for neopixels
- Neopixels
- Breadboard
- Relevant wires for connections

Wiring from here
http://learn.adafruit.com/neopixels-on-raspberry-pi/wiring

# Setup
# Comments
We use Python 3, because we're not ridiculous.

## Requirements
### Raspberry Pi
- Install the neopixel package (e.g. `pip3 install neopixel`)

### Computer with laptop
- Install aubio (We recommend using Anaconda to avoid unnecessary complication: `conda install -c conda-forge aubio `)
- Install the PyAudio package (e.g. `pip install pyaudio`)

## Running
### Raspberry Pi (start this first)
- Configure the `IP_ADDRESS` and `PORT` variables in `server.py` as needed
- Run `sudo python3 server.py` (note the `sudo`)

### Computer
- Configure `HOST` and `PORT` in `client.py` to match the Raspberry Pi's settings
- Run `python process_sound.py`
