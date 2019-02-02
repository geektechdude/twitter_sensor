# geektechstuff
# Twitter Application

import time

# Twython is a Twitter Python library
from twython import Twython

# imports the modules for the sensor
from bmp280 import BMP280
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

# imports the Twitter API keys from a .py file called auth
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# sets up a variable called Twitter that calls the relevent Twython modules
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# sets up the variables for the sensor
bus=SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

def get_temp():
    temperature = bmp280.get_temperature()
    temperature = round(temperature)
    return(temperature)

def get_pressure():
    pressure = bmp280.get_pressure()
    pressure = round(pressure)
    return(pressure)

def write_tweet():
    get_temp()
    get_pressure()
    tweet_to_send = "geektechstuff room currently at",temperature,"degrees celesius and",pressure,"bars"
    twitter.update_status(status=tweet_to_send)
    return

