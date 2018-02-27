from neopixel import Color
from time import sleep

from setup_lights import strip, colorWipe

MAX_PITCH = 4000.0
MAX_N = 10
MAX_VOLUME = 2000

def get_color_new(pitch):
    decimal_val = int( pitch/MAX_PITCH * (16**6-1) )
    hex_val = "{:0>6}".format( hex(decimal_val)[2:] )
    print(hex_val)

    r = hex_val[:2]
    g = hex_val[2:4]
    b = hex_val[4:6]

    r, g, b = (int(v, 16) for v in (r,g,b))
    
    return Color(r, g, b)

def get_color(pitch):
    ls=[]
    pitch = int(pitch)
    if pitch in range(0, 400):
        ls=[255,255,255]
    elif pitch in range(401, 800):
        ls=[125,0,255]
    elif pitch in range(801, 1200):
        ls=[0,0,255]
    elif pitch in range(1201, 1600):
        ls=[0,125,255]
    elif pitch in range(1601, 2000):
        ls=[0,255,255]
    elif pitch in range(2001, 2400):
        ls=[0,255,0]
    elif pitch in range(2401, 2800):
        ls=[255,255,0]
    elif pitch in range(2801, 3200):
        ls=[255,125,0]
    else:
        ls=[255,0,0]
    
    return Color(*ls)

def get_light_freq(volume):
    n = MAX_N - round(min(volume, MAX_VOLUME)/MAX_VOLUME * MAX_N)
    return n or 1 # if n == 0

def set_light(pitch, volume):
    color = get_color_new(pitch)
    n = get_light_freq(volume)
    print('n is {}'.format(n))

    for i in range(strip.numPixels()):
        if not i % n:
            strip.setPixelColor(i, color)
        else:
            strip.setPixelColor(i, Color(0,0,0))
    strip.show()


for pitch in range(0, 4000, 400):
    print( "Pitch: {}, Color: {}".format(pitch, get_color_new(pitch)) )
#
#n = MAX_N - min(volume, MAX_VOLUME)//MAX_VOLUME * MAX_N
#def set_light(pitch, volume):
#    color = get_color(pitch)
#    for n in range(1,10):
#        if ((volume < (11-n)*(MAX_VOLUME/10)) and (volume > (10-n)*(MAX_VOLUME/10))):
#            for i in range(0, strip.numPixels(), n):
#                if not i % n:
#                    strip.setPixelColor(i, color)
#                else:
#                    strip.setPixelColor(i, Color(0,0,0))
#                strip.show()
#



