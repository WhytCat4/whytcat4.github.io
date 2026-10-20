"""
Thermostat Application

Author: Whytney Caton
Version: 2.0
Purpose: Raspberry Pi thermostat application that monitors temperature,
         manages heating and cooling states, and displays system
         information to the user.
"""


# Runs the main functions for the thermostat.

from time import sleep
from datetime import datetime
from math import floor

# Import required to handle the buttons and PWMLED devices.
from gpiozero import Button, PWMLED

from sensor_manager import SensorManager
from state_machine import TemperatureMachine
from display_manager import DisplayManager
from database import DatabaseManager
from config import DEBUG

# Create the hardware components.
REDLIGHTGPIO = 18
BLUELIGHTGPIO = 23

redLight = PWMLED(REDLIGHTGPIO)
blueLight = PWMLED(BLUELIGHTGPIO)

GREENBUTTONGPIO = 24
REDBUTTONGPIO = 12
BLUEBUTTONGPIO = 25

greenButton = Button(GREENBUTTONGPIO)
redButton = Button(REDBUTTONGPIO)
blueButton = Button(BLUEBUTTONGPIO)

# Create the application components.
sensor = SensorManager()
database = DatabaseManager()
thermostat = TemperatureMachine(redLight, blueLight, sensor, database)
display = DisplayManager()


# Connect the buttons to the thermostat behavior.
greenButton.when_pressed = thermostat.processTempStateButton
redButton.when_pressed = thermostat.processTempIncButton
blueButton.when_pressed = thermostat.processTempDecButton

# Store the current time period so the program can detect
# when the period changes
currentTimePeriod = thermostat.getTimePeriod()

displayCounter = 1

# Repeat until the user creates a keyboard interrupt (CTRL-C).
repeat = True

while repeat:
    try:
        # Display processing message for debugging.
        if DEBUG:
            print("Processing Display Info...")

        # Grab the current time. 
        current_time = datetime.now()

        # Check whether the time period has changed.
        newTimePeriod = thermostat.getTimePeriod()

        if newTimePeriod != currentTimePeriod:
            # save the setpoint used during the completed period.
            timestamp = datetime.now().isoformat()

            database.saveTemperature(
                thermostat.setPoint,
                timestamp,
                currentTimePeriod
            )

            # Update the learned setpoint for the new period.
            currentTimePeriod = newTimePeriod
            thermostat.updateSetPoint()
    

        # Display the current date and time on the first line.
        lcd_line_1 = current_time.strftime('%b %d  %H:%M:%S\n')

        # Alternate the second line between temperature and thermostat state.
        if (displayCounter < 6):
            lcd_line_2 = f"Temp: {floor(sensor.getFahrenheit())} F"

            displayCounter += 1
        else:
            if thermostat.current_state.id == "off":
                lcd_line_2 = "SYSTEM OFF"
            else: 
                lcd_line_2 = f"{thermostat.current_state.id.upper()} Set: {thermostat.setPoint} F"

            displayCounter += 1

            if(displayCounter >= 11):
                    displayCounter = 1

        # Update the LCD display.
        display.updateScreen(lcd_line_1 + lcd_line_2)

        # Update the thermostat LED indicators.
        thermostat.updateLights()

        # Wait one second before updating again.
        sleep(1)

    except KeyboardInterrupt:
        # Exit cleanly.
        print("Cleaning up. Exiting...")

        # Stop the loop.
        repeat = False

        # Clear and clean up the LCD.
        display.cleanupDisplay()