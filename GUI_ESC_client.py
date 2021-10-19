############################################################################
# SOCKET COMMUNICATION: 
# FOR CLIENT !!!
# Remote controlling via GUI
############################################################################
#To run this code on Raspberry Pi OS you have to open terminal
#and run this commands: sudo pip3 install guizero

import socket
import _thread
from guizero import App, PushButton, Text, Slider, info
import time
from adafruit_motorkit import MotorKit
import RPi.GPIO as GPIO
import time

# Socket CLIENT connection
def initialize_client():
    # initialize socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.137.125'
    port = 5560
    # connect to this server
    s.connect((host, port))
    
    return s

def reconnect():
    print("reconnecting...")
    connected = False
    #recreate socket
    s = socket.socket()
    
    while not connected:
        try:
            s.connect(('192.168.137.125', 5560))
            connected = True
            print("sucessfully reconnected")
        except socket.error:
            print("reconnecting failed")
            time.sleep(2)
    


# function to send variable to server
def send():
    #send the all three slidervalues as a list
    #s.send(slidervalue.encode())
    s.sendall(str.encode("\n".join([str(servo_slider.value), str(motor1_slider.value), str(motor2_slider.value)])))
    print(servo_slider.value, motor1_slider.value, motor2_slider.value)


# function to receive message
def receive():
    while 1:
        try:
            data = s.recv(1024)
            msg = data.decode('ascii')
            if msg != "":
                update_chat(msg, 1)
        except:
            pass


"""
#Servo-motor control via PWM directly from Raspberry Pi GPIO
servoPIN = 17    #Servo Motor signal from GPIO PIN 17
Motor1PIN = 4    #Motor1 signal from GPIO PIN 4
Motor1PIN = 25   #Motor2 signal from GPIO PIN 25

With p.ChangeDutyCycle(value) we can change the servo position by entering the DUTY Cycle value
p.ChangeDutyCycle(2.5)   #duty cycle of 2.5% means -90degree angle
p.ChangeDutyCycle(7.5)   #duty cycle of 7.5% means 0degree angle
p.ChangeDutyCycle(12.5)   #duty cycle of 12.5% means +90degree angle
"""
def servo(slidervalue):
    value = int(slidervalue)/18 + 7.5
    p.ChangeDutyCycle(value)
    
#GUI window (internal name: app)
def close_window():
    app._close_window()
    s.close()



def makestop():
    s.sendall(str.encode("\n".join([str(servo_slider.value), str(0), str(0)])))
    
app = App(title="Motor Touch Control", width=480, height=320, layout="grid")
#infotext = Text(app, text="Control the speed and direction of the boat", grid=[0,0])
#infotext.text_size=10
#testbutton = PushButton(app, command=testfunc, text="Testbutton", grid=[0,2])
motor1text = Text(app, text=" both motors", grid=[0,3])
#motor2text = Text(app, text="motor 2", grid=[0,5])
servotext = Text(app, text="servo(angle)", grid=[0,7])
motor1_slider = Slider(app,height=35 , width=200, command=send, start=-50, end=50, grid=[0,4])
motor2_slider = Slider(app,height=35 ,width=200, command=send, start=-100, end=100, grid=[0,6])
servo_slider = Slider(app,height=35 ,width=350, command=send, start=-90, end=90, grid=[0,8])
reconnect = PushButton(app, command=reconnect, text="reconnect", grid=[1,4])
motor1stop = PushButton(app, command=makestop, text="Stop motors", grid=[1,4])
#motor2stop = PushButton(app, command=stop2, text="Stop motor2", grid=[1,6])
close = PushButton(app, command=close_window, text="EXIT", grid=[1,8])


if __name__ == '__main__':
    s = initialize_client()
    app.display()
