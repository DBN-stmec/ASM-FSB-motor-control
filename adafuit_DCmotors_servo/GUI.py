"""GUI and code for controlling adafruit_motorkit with two DC motors
and one Servo Motor

REQUIREMENTS BEFORE RUNNING THIS CODE

1)To run this code on Raspberry Pi OS you have to open terminal
and run these commands:

sudo pip3 install guizero
sudo pip3 install adafruit-circuitpython-motorkit

2)To build up a connection between Raspberry Pi and the adafruit_motorkit hardware with I2C,
use these terminal commands:  (https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)

sudo apt-get install -y python-smbus
sudo apt-get install -y i2c-tools
sudo raspi-config

After the last command a User Interface appears. Go to "Interfacing Options"
or "Advanced"(on older versions). 
Then go to "I2C" and select "yes" to enable ARM I2C Interface.

Open terminal to see all connected hardware:

sudo i2cdetect -y 1

3)AFTER THAT YOU HAVE TO GO TO THE FOLDER-DIRECTORY (here:examplefolder), IN WHICH THE CODE LIES AND RUN IT

cd examplefolder/
python3 GUI.py

"""

from guizero import App, PushButton, Text, Slider, info
import time
from adafruit_motorkit import MotorKit
import RPi.GPIO as GPIO


def close_window():
    app._close_window()

#DC-Motor control with Adafruit HAT
kit = MotorKit()

def motor1(slidervalue):
    value = int(slidervalue) / 100
    kit.motor1.throttle = value
    print(value)

def motor2(slidervalue):
    value = int(slidervalue) / 100
    kit.motor2.throttle = value
    print(value)

def stop1():
    #Stop all movement.
    kit.motor1.throttle = 0
    print("Movement value:",kit.motor1.throttle)
def stop2():
    #Stop all movement.
    kit.motor2.throttle = 0
    print("Movement value:", kit.motor1.throttle)
    
#Servo-motor control via PWM directly from Raspberry Pi GPIO
#Connect the orange servo wire to PIN17
servoPIN = 17  #Motor signal from GPIO PIN 17.
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(7.5) # Initialization

"""
With p.ChangeDutyCycle(value) we can change the servo position by entering the DUTY Cycle value
p.ChangeDutyCycle(2.5)   #duty cycle of 2.5% means -90degree angle
p.ChangeDutyCycle(7.5)   #duty cycle of 7.5% means 0degree angle
p.ChangeDutyCycle(12.5)   #duty cycle of 12.5% means +90degree angle
"""
def servo(slidervalue):
    value = int(slidervalue)/18 + 7.5
    p.ChangeDutyCycle(value)
    
#GUI window (internal name: app)
app = App(title="Motor Touch Control", width=480, height=320, layout="grid")
#infotext = Text(app, text="Control the speed and direction of the boat", grid=[0,0])
#infotext.text_size=10
#testbutton = PushButton(app, command=testfunc, text="Testbutton", grid=[0,2])
motor1text = Text(app, text="motor1", grid=[0,3])
motor2text = Text(app, text="motor2", grid=[0,5])
servotext = Text(app, text="servo(angle)", grid=[0,7])
motor1_slider = Slider(app,height=35 , width=200, command=motor1, start=-50, end=100, grid=[0,4])
motor2_slider = Slider(app,height=35 ,width=200, command=motor2, start=-50, end=100, grid=[0,6])
servo_slider = Slider(app,height=35 ,width=350, command=servo, start=-90, end=90, grid=[0,8])
motor1stop = PushButton(app, command=stop1, text="Stop motor1", grid=[1,4])
motor2stop = PushButton(app, command=stop2, text="Stop motor2", grid=[1,6])
close = PushButton(app, command=close_window, text="EXIT", grid=[1,8])

app.display()



