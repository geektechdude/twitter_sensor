# geektechstuff
# Twitter Application

import time

# gpiozero for CPU
from gpiozero import CPUTemperature

import datetime

# Twython is a Twitter Python library
from twython import Twython

# imports the modules for the sensor
from bmp280 import BMP280
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
    
# lux sensor
import ltr559

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

def cpu_temperature():
    cpu = CPUTemperature()
    cpu_temp = cpu.temperature
    cpu_temp = str(cpu_temp)
    return(cpu_temp)

def get_temp():
    temperature = bmp280.get_temperature()
    temperature = round((temperature),2)
    temperature = temperature -2
    temperature = str(temperature)
    return(temperature)

def get_pressure():
    pressure = bmp280.get_pressure()
    pressure = round(pressure)
    pressure = str(pressure)
    return(pressure)

def get_lux():
    lux = ltr559.get_lux()
    for x in range(1,5):
        x_lux = lux
        time.sleep(0.5)
    lux_rounded = round(x_lux,2)
    lux_str = str(lux_rounded)
    return(lux_str)

def write_tweet():
    get_temp()
    get_pressure()
    time_now()
    cpu_temperature()
    get_lux()
    tweet_to_send = "geektechstuff.com room currently at "+get_temp()+" degrees celesius.\nPressure is at "+get_pressure()+"  hectopascals.\nThe time is "+time_now()+"\nCPU temp is "+cpu_temperature()+". Lux level in room "+get_lux()+" .\nCreated in #Python"
    tweet_to_send = str(tweet_to_send)
    twitter.update_status(status=tweet_to_send)
    return()

def time_now():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    now=str(now)
    return(now)

write_tweet()


