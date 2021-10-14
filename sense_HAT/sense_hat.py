#################################################################################################
# SENSE HAT (B): Code to access gyroscope, temperature, humidity, pressure and color sensor

# Requirements! Open your linux terminal an execute this command: sudo apt-get install sense-hat

################################################################################################
import sys
from sense_hat import SenseHat
sense = SenseHat()


#temperature
temp = sense.get_temperature()
print("Temperature: %s C" % temp)

#humidity
humidity = sense.get_humidity()
print("Humidity: %s %%" % humidity)

#pressure
pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)

#orientation
orientation = sense.get_orientation()
print("Orientation: %s %%" % orientation)

#compass
compass = sense.get_compass()
print("Compass: %s %%" % compass)


