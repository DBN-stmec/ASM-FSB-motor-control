# ASM-FSB-motor-control
Raspberry Pi + Motor Controllers: Controlling various electrical motors (Servo-, DC-, brushless DC-motors) remotly between two Raspberry Pi's
## Purpose of this project
The goal of this project is to control electrical motors with a Raspberry Pi. This includes in the two (brushless) DC motors and a servo motor, whose speed can be changed independently from each other with a grafical user interface (GUI).
The motors, which are implemented to the boot can be controlled remotely via socket communication between two Raspberry Pi's. The server is the hardware on the boat with the motors included and the client is another Raspberry Pi, which can control the servers motors remotely.
The server is designed to act autonomously, if the client is disconnected. Further controls for autonomous driving can be implemented into the servers: GUI_ESC_server.py file.
## Folder structure
The files on this folder level is required to run the final project are: **Controlling Brushless DC.pdf, GUI_ESC_server.py, GUI_ESC_client.py**. The adafruit_DCmotors_servo-folder contains codes for using two DC-motors with an adafruit controller instead. The brushlessDCmotors_servo-folder includes the code for controlling two brushless DC motors and one Servo motor (this is our final setup) directly without remote control. The distance_sensor and sense_HAT includes code to use distance sensors and sensors from the sense_HAT, if these hardware are physically implemented. **The Instructions-folder include all other documetations and instructions as pdf and editable odt.files** 
## HOW TO MAKE IT RUN
1. Set up both Raspberry Pi's operating systems
2. Put the GUI_ESC_server.py on the first Raspberry Pi (server) and the GUI_ESC_client.py on the second Raspberry Pi (client).
3. Set up motors on servers Pi by following the instruction of the Controlling Brushless DC.pdf. *HINT:Instead of using the code from the pdf, use the GUI_ESC_server.py instead.*
4. Find out the wifi routers IP-adress and update YOUR IP-adress within these code: GUI_ESC_server.py, GUI_ESC_client.py. Then connect both RAspberry Pi's to the same wifi network.
5. Run GUI_ESC_server.py first and then the GUI_ESC_client.py
6. Now a GUI must be shown on the client to control.
