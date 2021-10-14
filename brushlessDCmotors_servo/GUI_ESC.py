############################################################################
#REQUIRED HARDWARE: 2x BRUSHLESS DC-MOTORS with controllers, 1x Servomotor
############################################################################
#To run this code on Raspberry Pi OS you have to open terminal
#and run this commands: sudo pip3 install guizero

from guizero import App, PushButton, Text, Slider, info
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
import os
os.system ("sudo pigpiod")
import pigpio

#Connect the orange wire of Servo Motor to #PIN 17
GPIO1=4  #Motor1 signal from GPIO PIN #4.
GPIO2=25  #Motor2 signal from GPIO PIN #25.
p1 = pigpio.pi();
p2 = pigpio.pi();
"""
#THIS CODE IS FOR MOTOR CONTROL VIA "import RPi.GPIO as GPIO""
#Dutycycle value range: m1.ChangeDutyCycle(min 7 - max 12)
GPIO.setup(GPIO1, GPIO.OUT)
m1 = GPIO.PWM(GPIO1, 50)
m1.start(0)

GPIO.setup(GPIO2, GPIO.OUT)
m2 = GPIO.PWM(GPIO2, 50)
m2.start(0)
"""

#p.set_servo_pulsewidth(GPIO, 1000)  ->  max.backwards speed
#p.set_servo_pulsewidth(GPIO, 1500)  ->  no speed
#p.set_servo_pulsewidth(GPIO, 2000)  ->  max.forward speed


def motor1(slidervalue):
    while True:
        value = int(slidervalue)*5 + 1500
        p1.set_servo_pulsewidth(GPIO1, value)
        print("pwm in ns:", value)#ns =nanosecond
        break

        """
        value = int(slidervalue)/20 + 7
        if value ==7:
            m1.ChangeDutyCycle(0)
            print("stopped")
        else:
            m1.ChangeDutyCycle(value)
            print("Dutycycle:", value)
        break
       """ 


def motor2(slidervalue):
    while True:
        value = int(slidervalue)*5 + 1500
        p2.set_servo_pulsewidth(GPIO2, value)
        print("pwm in ns:", value)#ns =nanosecond
        break
    
        
        """
        value = int(slidervalue)/20 + 7
        if value ==7:
            m2.ChangeDutyCycle(0)
            print("stopped")
        else:
            m2.ChangeDutyCycle(value)
            print("Dutycycle:", value)
        break
"""
#Servo-motor control via PWM directly from Raspberry Pi GPIO
#Connect the orange servo wire to PIN17
servoPIN = 17  #Motor signal from GPIO PIN 17.

GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(7.5) # Initialization

def servo(slidervalue):
    value = int(slidervalue)/18 + 7.5
    p.ChangeDutyCycle(value)
    
"""
With p.ChangeDutyCycle(value) we can change the servo position by entering the DUTY Cycle value
p.ChangeDutyCycle(2.5)   #duty cycle of 2.5% means -90degree angle
p.ChangeDutyCycle(7.5)   #duty cycle of 7.5% means 0degree angle
p.ChangeDutyCycle(12.5)   #duty cycle of 12.5% means +90degree angle
"""
def stop1():
    """Stop all movement."""
    p1.set_servo_pulsewidth(GPIO1, 0)
    print("Movement stopped")
def stop2():
    """Stop all movement."""
    p2.set_servo_pulsewidth(GPIO2, 0)
    print("Movement stopped")


def close_window():
    stop1()
    stop2()
    app._close_window()
    
    
#GUI window (internal name: app)
app = App(title="Motor Touch Control", width=480, height=320, layout="grid")
#infotext = Text(app, text="Control the speed and direction of the boat", grid=[0,0])
#infotext.text_size=10
#testbutton = PushButton(app, command=testfunc, text="Testbutton", grid=[0,2])
motor1text = Text(app, text="motor1", grid=[0,3])
motor2text = Text(app, text="motor2", grid=[0,5])
servotext = Text(app, text="servo(angle)", grid=[0,7])
motor1_slider = Slider(app,height=35 , width=200, command=motor1, start=-100, end=100, grid=[0,4])
motor2_slider = Slider(app,height=35 ,width=200, command=motor2, start=-100, end=100, grid=[0,6])
servo_slider = Slider(app,height=35 ,width=350, command=servo, start=-90, end=90, grid=[0,8])
motor1stop = PushButton(app, command=stop1, text="Stop motor1", grid=[1,4])
motor2stop = PushButton(app, command=stop2, text="Stop motor2", grid=[1,6])
close = PushButton(app, command=close_window, text="EXIT", grid=[1,8])

app.display()