"""Manages the thermostat temperature database."""

import sqlite3
from config import DEBUG

DATABASE_NAME = "temperature_database.db"

class DatabaseManager:
    """Manages storing and retrieving thermostat temperature data."""

    def __init__(self):
        """Set up the database."""

        database = None
        
        try:
            # Connect to the SQLite database.
            database = sqlite3.connect(DATABASE_NAME)
            cursor = database.cursor()

            # Create a table to store temperature preference data.
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS temperature_preferences (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    set_temperature INTEGER NOT NULL,
                    timestamp TEXT NOT NULL,
                    time_period TEXT NOT NULL
                )
        ''')

            # Commit changes to the database.
            database.commit()

            if DEBUG:
                print("Database and table created successfully.")

        except sqlite3.Error as e:
            if DEBUG:
                print(f"An error occurred: {e}")

        finally:
            # Close the database connection.
            if database:
                database.close()


    def saveTemperature(self, temperature, timestamp, time_period):
        """Save a temperature preference to the database."""

        database = sqlite3.connect(DATABASE_NAME)

        database.execute("""
            INSERT INTO temperature_preferences
            (set_temperature, timestamp, time_period)
            VALUES (?, ?, ?)
        """, (temperature, timestamp, time_period))

        database.commit()
        database.close()


    def getTemperatures(self):
        """Retrieve saved temperature preferences."""

        database = sqlite3.connect(DATABASE_NAME)

        cursor = database.execute("""
            SELECT set_temperature, timestamp, time_period
            FROM temperature_preferences
        """)

        temperatures = cursor.fetchall()
        database.close()

        return temperatures


    def getTemperatureByPeriod(self, time_period):
        """Retrieve saved temperatures for a specific time period."""

        database = sqlite3.connect(DATABASE_NAME)

        cursor = database.execute("""
            SELECT set_temperature
            FROM temperature_preferences
            WHERE time_period = ?
        """, (time_period,))

        temperatures = cursor.fetchall()
        database.close()

        return temperatures

