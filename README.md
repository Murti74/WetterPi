# WetterPi

This small project will show you on displaying weather statistics on an OLED Display with the use of the Raspberry Pi (WH) and python .



First you need to install the necessary libraries for the oled display.

```
sudo python -m pip install --upgrade pip setuptools wheel
sudo pip install Adafruit-SSD1306
```

Install Pyowm with 

```
$ pip install pyowm
```


In order to be able to use pyowm, you need to create an account at 
```
https://openweathermap.org/api
```

and get your own unique API Key.


After these steps clone this repository with

```
$ git clone https://github.com/Murti74/WetterPi.git
```

and insert your unique API Key into to python file.


Before you run the code, you must obviously connect the oled display properly with your Raspberry PI GPIOs. 
Connect Vcc with the 3.3V GPIO Pin 1, Gnd with any Ground Pin, SDA with GPIO 3 and SCL with GPIO 5

Use 
```
sudo raspi-config
```
and enable the I2C Interface.

With the command
```
i2cdetect -y 1
```

you can check if your module is being detected



Run the code with
```
sudo python Weather.py
```


The End result should look like this ( I used the German language for displaying the information)


![IMG_20200112_193110](https://user-images.githubusercontent.com/59802903/72223774-e6073f80-3572-11ea-86c5-6ffc32b6b5b5.jpg)

