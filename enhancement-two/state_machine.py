"""Manages the thermostat's heating, cooling, and off states."""

# For testing purposes
from config import DEBUG
from statemachine import StateMachine, State
from math import floor
from datetime import datetime

DEFAULT_SETPOINT = 72
MIN_SETPOINT = 45
MAX_SETPOINT = 90

class TemperatureMachine(StateMachine):
    
    def __init__(self, redLight, blueLight, sensor, database):
        self.redLight = redLight
        self.blueLight = blueLight
        self.sensor = sensor
        self.database = database
        self.setPoint = DEFAULT_SETPOINT

    # Define the three operating states of the thermostat.
    off = State(initial = True)
    heat = State()
    cool = State()

    # Cycle through the thermostat's operating states.
    cycle = (
        off.to(heat) |
        heat.to(cool) |
        cool.to(off)
    )


    # Action performed when the state machine transitions
    # into the 'heat' state.
    def on_enter_heat(self):
        # Start pulsing the red LED when entering the heat state.
        self.redLight.pulse()

        if DEBUG:
            print("* Changing state to heat")
            

    # Action performed when the state machine transitions
    # out of the 'heat' state.
    def on_exit_heat(self):
        # Stop the red LED when leaving the heat state.
        self.redLight.off()


    # Action performed when the state machine transitions
    # into the 'cool' state.
    def on_enter_cool(self):
        # Start pulsing the blue LED when entering the cool state.
        self.blueLight.pulse()

        if DEBUG:
            print("* Changing state to cool")

    
    # Action performed when the state machine transitions
    # out of the 'cool' state.
    def on_exit_cool(self):
        # Stop the blue LED when leaving the cool state.
        self.blueLight.off()


    # Action performed when the state machine transitions
    # into the 'off' state.
    def on_enter_off(self):
        # Turns off both LEDs when entering the off state.
        self.redLight.off()
        self.blueLight.off()

        if DEBUG:
            print("* Changing state to off")

    
    # Cycle through the thermostat states when the state button is pressed.
    def processTempStateButton(self):
        if DEBUG:
            print("Cycling Temperature State")

        self.cycle()


    # Increase the thermostat setPoint when the temperature-up button is pressed.
    def processTempIncButton(self):
        if DEBUG:
            print("Increasing Set Point")

        if self.setPoint < MAX_SETPOINT:
            self.setPoint += 1
            self.updateLights()


    # Decrease the thermostat setPoint when the temperature-down button is pressed.
    def processTempDecButton(self):
        if DEBUG:
            print("Decreasing Set Point")

        if self.setPoint > MIN_SETPOINT:
            self.setPoint -= 1
            self.updateLights()


    # Determines the current time period for temperature preferences.
    def getTimePeriod(self):
        current_hour = datetime.now().hour

        if 6 <= current_hour < 12:
            return "morning"
        elif 12 <= current_hour < 18:
            return "day"
        else:
            return "night"


    def updateSetPoint(self):
        """Calculate a learned setpoint for the current time period."""

        time_period = self.getTimePeriod()

        period_temperatures = self.database.getTemperatureByPeriod(
            time_period
        )

        # Keep the current setting until at least
        # 5 preferences have been collected for this period.
        if len(period_temperatures) < 5:
            return

        total = sum(temperature[0] for temperature in period_temperatures)
        average = total / len(period_temperatures)

        self.setPoint = round(average)

        if DEBUG:
            print(f"Learned setpoint for {time_period}: {self.setPoint}")
        


    # Update the LED indicators based on the thermostat state and temperature.
    def updateLights(self):
        # Read the current temperature in Fahrenheit
        temp = floor(self.sensor.getFahrenheit())
        self.redLight.off()
        self.blueLight.off()
    
        # Display current values for debugging.
        if DEBUG:
            print(f"State: {self.current_state.id}")
            print(f"setPoint: {self.setPoint}")
            print(f"Temp: {temp}")

        # Set the LED behavior based on the current state and temperature.
        if self.current_state.id == "heat":
            if temp < self.setPoint:
                # Pulse the red LED when the temperature is below the set point.
                self.redLight.pulse()
            else:
                # Keep the red LED on when the set point is reached.
                self.redLight.on()

        elif self.current_state.id == "cool":
            if temp > self.setPoint:
                # Pulse the blue LED when the temperature is above the set point.
                self.blueLight.pulse()
            else:
                # Keep the blue LED on when the set point is reached.
                self.blueLight.on()
                
        elif self.current_state.id == "off":
            self.redLight.off()
            self.blueLight.off()

