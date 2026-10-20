"""Manages the 16x2 LCD display for the thermostat."""
 
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import board


class DisplayManager:

    def __init__(self):

        # Configure GPIO lines for the LCD display.

        self.lcd_rs = digitalio.DigitalInOut(board.D17)
        self.lcd_en = digitalio.DigitalInOut(board.D27)
        self.lcd_d4 = digitalio.DigitalInOut(board.D5)
        self.lcd_d5 = digitalio.DigitalInOut(board.D6)
        self.lcd_d6 = digitalio.DigitalInOut(board.D13)
        self.lcd_d7 = digitalio.DigitalInOut(board.D26)

        self.lcd_columns = 16
        self.lcd_rows = 2 

        # Initialize the LCD.
        self.lcd = characterlcd.Character_LCD_Mono(self.lcd_rs, self.lcd_en, 
                    self.lcd_d4, self.lcd_d5, self.lcd_d6, self.lcd_d7, 
                    self.lcd_columns, self.lcd_rows)

        # Clear the LCD screen before we start.
        self.lcd.clear()


    # Clear the display and release the GPIO resources.
    def cleanupDisplay(self):
        self.lcd.clear()
        self.lcd_rs.deinit()
        self.lcd_en.deinit()
        self.lcd_d4.deinit()
        self.lcd_d5.deinit()
        self.lcd_d6.deinit()
        self.lcd_d7.deinit()

        
    # Clear the LCD display.
    def clear(self):
        self.lcd.clear()


    # Update the LCD with the supplied message.
    def updateScreen(self, message):
        self.lcd.clear()
        self.lcd.message = message