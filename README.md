# ardget
Temperature + Mode + Python Script Data Sync - Web control panel on Django for Arduino .
ru: Веб-панель управления на Django для Arduino.

# Screenshot
![Image 1](https://github.com/shumdeveloper/ardget/raw/643c88b10a6c59ac34f28ba33c4be59f1aa0e0dc/screenshot1.png)
1

# How to use
Very simple!

0. Connect your db (Standard db will go) 
1. Copy ardget_app to your (Django 3.1.5) Project
2. Add in your project urls file - path('', include('ardget_app.urls')),
3. Add "ardget_app" to your apps in settings 
4. Good! You can use my app :)


# Language Web Panel Note
Half of panel text writted on English. If you need to translate ALL text to English - it well be very simple (Very few text).

# Arduino Project Notes
Views:
/ arduinofin - Home
/ arduinofin / weathr - Weather for 2 arduino modules in the format (Sun, Cloudy, Rain) / DONE
/ arduinofin / nfcodes - Output for arduinofin nfc codes from the database in the form of code, code, code - MAXIMUM 3 CODES / DONE
/ arduinofin / links - Only for the py script, Output of custom links in the format: pc1 # https: //example.com / DONE
/ arduinofin /? temperature = 24 & mode = 0 - Get requests from the main arduinki / DONE
/ arduinofin / arcustomtext - OUTPUT TO ARDUINO 2 FOR OUTPUT USER TEXT WHICH IS IN THE SITE PANEL // DONE
/ arduinofin / modes

What does arduino alone do:
Sends modes from the remote
Sends temperature
Sends mode

What arduino does two:
Receives the temperature from the server and in mode 1 shows it on the LCD
Receives weather from the server and displays it in mode 2
After scanning nfc tags, it takes / nfcodes and checks for a match, if there is one - displays custom text from the server

What the script does on two PCs:
Opens the links that are indicated in the panel on the site for each pc separately
Outputs custom text as a result of getting mode


Equipment list:
Arduino Home:
Layout
Green ice
2 Red Ice
temperature sensor
IR sensor
3 resistors
6 long wires
8 short wires
WIFI MODULE


Arduino 2:
LCD display and everything for its connection
WIFI module
RFID NFC Module
NFC: Resistor, wiring and green light.


