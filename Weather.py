#!/usr/bin/python

import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from pyowm import OWM

import time
import datetime
import pyowm

owm = OWM('61c13cb0f5214ba6c1e584ec076b9478',language='de') #set language
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

x = str(datetime.datetime.now().time())
x = x[:-10]
observation = owm.weather_at_place('Berlin,de') # set location
w = observation.get_weather()


# Weather details, removing unnecessary text
temp = str(w.get_temperature('celsius')).replace("{'temp_max': ", "")
temp = temp.replace("'temp_kf': None, 'temp': ", "")
temp = temp.replace("'temp_min': " , "")
temp = temp.replace("}","")
temp = temp.replace(",","")
temp = temp[5:]
temp = temp[:-4]
temp = temp.replace("-","")

feuc = w.get_humidity()

stat = w.get_detailed_status()

font = ImageFont.load_default()



draw.rectangle((0,0,127,63), outline=255, fill=0)
draw.text((2, 5), "Berlin",  fill=255)
draw.text((2, 15), "Temperature *C = " + str(temp), fill=255)
draw.text((2, 25), "Humidity = "+str(feuc)+"%", fill =255)
draw.text((2, 35), stat, fill =255)
disp.image(image)
disp.display()


while 1:
    time.sleep(1)


