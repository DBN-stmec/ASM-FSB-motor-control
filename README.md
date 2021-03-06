# ASM-FSB-motor-control
Raspberry Pi: Controlling Servo- and brushless DC-motors remotely between two Raspberry Pi's
## Purpose of this project
The goal of this project is to control electrical motors with a Raspberry Pi. This includes in the two (brushless) DC motors and a servo motor, whose speed can be changed independently from each other with a grafical user interface (GUI).
The motors, which are implemented to the boot can be controlled remotely via socket communication between two Raspberry Pi's. The server is the hardware on the boat with the motors attached and the client is another Raspberry Pi, which can control the servers motors remotely.
The server is designed to act autonomously, if the client is disconnected. Further controls for autonomous driving can be implemented into the servers: GUI_ESC_server.py file for future work.
## Folder structure
The files on this folder level is required to run the final project: **Controlling Brushless DC.pdf, GUI_ESC_server.py, GUI_ESC_client.py**. *The brushlessDCmotors_servo*-folder includes the code for controlling two brushless DC motors and one Servo motor (this is our final setup) directly without remote control. The *adafruit_DCmotors_servo*-folder contains codes for using two DC-motors with an adafruit controller instead. The *distance_sensor* and *sense_HAT* folders include codes to use distance sensors and sensors from the sense_HAT hardware, if these hardware are physically implemented. **The Instructions-folder include all other documetations and instructions as pdf and editable odt.files** 
## HOW TO MAKE IT RUN
1. Set up both Raspberry Pi's operating systems
2. Put the GUI_ESC_server.py on the first Raspberry Pi (server) and the GUI_ESC_client.py on the second Raspberry Pi (client).
3. Set up motors on servers Pi by following the instruction: **Controlling Brushless DC.pdf** here in this github repository. *HINT: Instead of using the code from the pdf, use the GUI_ESC_server.py instead.*
4. Connect both Raspberry Pi's to the same wifi network.
5. Open the folder: "Instructions" and follow the **remote_control.pdf** instruction to connect both Raspberry Pi's via SSH. Find out the IP-adress of your **"executer Raspberry Pi"**, on which the motors are connected. Then update the **"executer Raspberry Pi's"** IP-adress within the code: "GUI_ESC_client.py".
6. Now on the "controller Raspberry Pi" the terminal should be open and able to control the "executer Raspberry Pi via SSH.
7. Run GUI_ESC_server.py via SSH first and then the GUI_ESC_client.py
8. Now a GUI must be shown on the client to control.
