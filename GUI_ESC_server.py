############################################################################
# SOCKET COMMUNICATION: 
# FOR SERVER !!!
# REQUIRED HARDWARE: 2x BRUSHLESS DC-MOTORS with controllers, 1x Servomotor
############################################################################
#To run this code on Raspberry Pi OS you have to open terminal
#and run this commands: sudo pip3 install guizero

import socket
import logging
from guizero import App, PushButton, Text, Slider, info
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
import os
os.system ("sudo pigpiod")
import pigpio

#Connect the orange wire of Servo Motor to #PIN 17
GPIO1=4  #Motor1 signal from GPIO PIN #4.
GPIO2=25  #Motor2 signal from GPIO PIN #25.
p1 = pigpio.pi();
p2 = pigpio.pi();

# Socket server connection
def initialize_server():
    # initialize socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    host = ''
    port = 5560
    # initialize this server
    s.bind((host, port))
    print("Socket bind comlete.")
    # set number of clients
    s.listen(1)
    # accept the connection from client
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    
    return conn


# check socket connection is down (True/False)
logger = logging.getLogger(__name__)

def is_socket_closed(sock: socket.socket) -> bool:
    try:
        # this will try to read bytes without blocking and also without removing them from buffer (peek only)
        data = sock.recv(16, socket.MSG_DONTWAIT | socket.MSG_PEEK)
        if len(data) == 0:
            print("not connected")
            return True
    except BlockingIOError:
        print("connected")
        return False  # socket is open and reading from it would block  
    except ConnectionResetError:
        print("not conected")
        return True  # socket was closed for some other reason
    except Exception as e:
        logger.exception("unexpected exception when checking if a socket is closed")
        print("connected")
        return False
    return False


# function to send message
def send():
    #get the messsage
    msg = textbox.get("0.0", END)
    #update chatlog of
    update_chat(msg, 0)
    #send the message
    conn.send(msc.encode('ascii'))
    textbox.delete("0.0", END)
    
  
# function to receive data and control motors
def receive():
    #while True:
    while is_socket_closed(conn) is False:
        try:
            #data = conn.recv(1024)
            #msg = data.decode('ascii')
                    
            #receive all three slidervalues
            sv, m1, m2 = [int(i) for i in conn.recv(1024).decode().split('\n')]
            print("servovalue:",sv , " motorvalue1:",m1 , " motorvalue2=", m2)
            motor1(m1)
            motor2(m1)
            servo(sv)
             
        except:
            print("Connection is lost")
            #Stop all motors when connection is lost
            motor1(0)
            motor2(0)
            #receive()
            #break
            #conn.close()
            #initialize_server()
           

# BRUSHLESS MOTOR 1&2 with electronic speed controller (ESC)

#p.set_servo_pulsewidth(GPIO, 1000)  ->  max.backwards speed
#p.set_servo_pulsewidth(GPIO, 1500)  ->  no speed
#p.set_servo_pulsewidth(GPIO, 2000)  ->  max.forward speed

def motor1(slidervalue):
    while True:
        value = int(slidervalue)*5 + 1500
        p1.set_servo_pulsewidth(GPIO1, value)
        p2.set_servo_pulsewidth(GPIO2, value)
        #print("pwm in ns:", value)#ns =nanosecond
        break

def motor2(slidervalue):
    while True:
        value = int(slidervalue)*5 + 1500
        p2.set_servo_pulsewidth(GPIO2, value)
        #print("pwm in ns:", value)#ns =nanosecond
        break


# SERVO MOTOR
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
    # Stop both motors
    p1.set_servo_pulsewidth(GPIO1, 0)
    p2.set_servo_pulsewidth(GPIO2, 0)
    print("Movement stopped")
def stop2():
    # Stop motor 2
    p2.set_servo_pulsewidth(GPIO2, 0)
    print("Movement stopped")


def close_window():
    stop1()
    stop2()
    conn.close()
    app._close_window()
    
"""    
# GUI
app = App(title="Motor Touch Control", width=480, height=320, layout="grid")

motor1text = Text(app, text="motors", grid=[0,3])
#motor2text = Text(app, text="motor2", grid=[0,5])
servotext = Text(app, text="servo(angle)", grid=[0,7])

motor1_slider = Slider(app,height=35 , width=200, command=motor1, start=-100, end=100, grid=[0,4])
#motor2_slider = Slider(app,height=35 ,width=200, command=motor2, start=-100, end=100, grid=[0,6])
servo_slider = Slider(app,height=35 ,width=350, command=servo, start=-90, end=90, grid=[0,8])

motor1stop = PushButton(app, command=stop1, text="Stop motors", grid=[1,4])
#motor2stop = PushButton(app, command=stop2, text="Stop motor2", grid=[1,6])
close = PushButton(app, command=close_window, text="EXIT", grid=[1,8])
"""

if __name__ == '__main__':
    conn = initialize_server()
    receive()
    app.display()
