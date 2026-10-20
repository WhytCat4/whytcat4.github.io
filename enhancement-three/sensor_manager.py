"""Manages the AHT20 temperature sensor for the thermostat."""

# Imports necessary to connect to the AHT20 temperature sensor
# and the I2C bus on the Raspberry Pi.
import adafruit_ahtx0
import board

class SensorManager:

    def __init__(self):
        self.i2c = board.I2C()
        self.thSensor = adafruit_ahtx0.AHTx0(self.i2c)

    # Return the current temperature in Fahrenheit.
    def getFahrenheit(self):
        temperature = self.thSensor.temperature
        return (((9/5) * temperature) + 32)