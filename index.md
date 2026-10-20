---
title: CS-499 Computer Science Capstone ePortfolio
---

# Whytney Caton | CS-499 Computer Science Capstone

Welcome to my Computer Science capstone ePortfolio. This page presents my professional self-assessment, code review, and three enhancements to a thermostat application originally developed for CS-350: Emerging Systems Architectures and Technologies.

## Table of Contents

- [Professional Self-Assessment](#professional-self-assessment)
- [Capstone Project Overview](#capstone-project-overview)
- [Original Artifact](#original-artifact)
- [Code Review](#code-review)
- [Enhancement One: Software Design and Engineering](#enhancement-one-software-design-and-engineering)
- [Enhancement Two: Algorithms and Data Structures](#enhancement-two-algorithms-and-data-structures)
- [Enhancement Three: Databases and Security](#enhancement-three-databases-and-security)
- [Course Outcomes](#course-outcomes)

---

## Professional Self-Assessment

Throughout my Computer Science program, I have taken many interesting classes that challenged me and opened my eyes to the different opportunities in the field. Although I have developed an interest in several areas of computer science, data handling, analysis, and databases have interested me the most. I discovered this interest during my first class, Introduction to Structured Database Environments, where I was introduced to SQL and data manipulation. My interest grew after taking Role of Data Analysis in Organizations, which highlighted how organizations use data analysis to make informed, data-driven decisions. To deepen my understanding, I also took Data Valid: Getting Right Data. This course taught me how to evaluate whether available data could address an organization’s problems and identify what additional information might be needed. It also emphasized the communication and collaboration required to obtain the appropriate data. These experiences helped shape my career goal of pursuing data analytics. They also showed me the importance of combining technical skills with critical thinking and an understanding of organizational needs.

Throughout the program, I have developed skills in software engineering, databases, algorithms, data structures, and security. My coursework taught me to consider how computing solutions are designed, how information is organized and retrieved, and how algorithms can be applied to solve problems efficiently. I have also learned the importance of writing maintainable code, protecting data, and considering the needs of the people who will use a solution. Through programming assignments, database projects, reports, and technical documentation, I have practiced applying these concepts and explaining my decisions. These experiences have helped me understand that successful computing solutions must be reliable, maintainable, secure, and useful to their intended audience. They have also strengthened my ability to evaluate problems, consider different approaches, and make thoughtful technical decisions.

Communication and collaboration have been important throughout my experience in the Computer Science program. Many of my courses required me to write reports, explain the reasoning behind my findings, and describe how I approached and completed projects. These assignments helped me develop the ability to communicate technical information clearly and explain my decisions to others. One specific example was my Software Development Lifecycle course, where I learned about the Agile development process and Scrum. As part of the coursework, I collaborated with classmates who were assigned different roles, including Product Owner and Scrum Master. We communicated our findings, shared information, and worked through the assigned activities together. This experience helped me understand how different roles contribute to a development team and how effective communication supports collaboration and decision-making. It also reinforced the importance of understanding project goals, considering the needs of others, and explaining technical information in a way that supports a shared objective. Together, these experiences taught me that successful computer science projects require not only technical skills but also the ability to communicate, collaborate, and work effectively with others.

My experiences throughout the program have helped me recognize the importance of accuracy, thoughtful problem-solving, clear communication, and responsible data handling. Although data analytics is my primary career interest, I also recognize that the skills I have developed can be applied to related areas, including data engineering and software development. I want to continue improving my skills in areas such as Python, SQL, and data visualization while building a strong foundation for my career. My goal is to use technology and data to help organizations better understand problems and make informed decisions.

The artifacts in my ePortfolio demonstrate how I have developed and applied these skills throughout the Computer Science program. For my capstone, I chose to enhance a thermostat project I originally completed in Emerging Systems Architectures and Technologies. The original project used a Raspberry Pi, sensors, and Python to create a working thermostat prototype. I chose this project because it provided an opportunity to build on an existing solution and demonstrate how improvements in software design, algorithms, and databases can make an application more useful and maintainable. Rather than creating an entirely new project, I wanted to show how an existing solution could be improved through the application of the skills I developed throughout the program.

My first enhancement focused on Software Design and Engineering. I reorganized the original thermostat application into separate modules and classes to make the code easier to understand, maintain, and expand. Separating responsibilities into components helped create a more organized structure and made individual parts of the application easier to manage. This enhancement allowed me to apply software design principles and recognize the value of writing code that can be maintained and modified as requirements change. It also reinforced the importance of clear documentation and organizing code in a way that supports future development and collaboration.

My second enhancement focused on Algorithms and Data Structures. I developed an approach for using saved temperature preferences to calculate a preferred setpoint for different times of the day. The goal was to allow the thermostat to use previously recorded preferences rather than relying entirely on a manually selected temperature. Organizing preferences by time period allows the application to use relevant information when calculating a setpoint. This enhancement helped me apply algorithmic thinking to a practical problem and consider how data organization and decision-making logic can improve an application’s functionality.

My third enhancement focused on Databases. I implemented an SQLite database and created a database management component to store and retrieve temperature preferences, timestamps, and time periods. This allowed the thermostat to retain information that the original application did not save for future use. I also considered how to manage database access, use parameterized queries, handle database errors, and limit the information collected. This enhancement demonstrated the importance of designing a database that meets an application’s needs while considering data integrity, privacy, and security.

Together, these enhancements demonstrate my ability to evaluate an existing computing solution and improve it through software design, algorithm development, and database implementation. Each enhancement addresses a different area, but they work together to create a more organized and useful application. The experience also helped me understand how design decisions affect maintainability, how algorithms can use stored information to support decisions, and how databases make it possible to retain and retrieve information for future use.

Completing my Computer Science coursework and developing my ePortfolio have helped me recognize my strengths and clarify my professional goals. I have learned that I enjoy working with data and understanding how it can be used to solve problems, but I have also gained skills that can be applied across the broader computer science field. My ePortfolio provides examples of how I have applied these skills and grown as a student and developing professional. As I prepare to enter the workforce, I plan to continue building my technical knowledge, strengthening my communication and collaboration skills, and pursuing opportunities in data analytics. I believe the knowledge and experience I have gained throughout this program will provide a strong foundation for my career and allow me to continue learning as technology and industry needs evolve.

---

## Capstone Project Overview

For my capstone, I enhanced an existing thermostat application in three areas:

1. **Software Design and Engineering:** Refactored the original application into separate modules for the main program, sensor management, display management, and thermostat state management.
2. **Algorithms and Data Structures:** Added logic to organize temperature preferences by time period and calculate a learned setpoint from previous selections.
3. **Databases and Security:** Added SQLite persistence through a `DatabaseManager`, parameterized SQL operations, database error handling, and more appropriate production debugging settings.

Together, these changes build on the original project rather than replacing it. They demonstrate how thoughtful design, useful data, and secure data handling can improve a working application.

## Original Artifact

The original artifact was developed for CS-350: Emerging Systems Architectures and Technologies. It was written in Python for a Raspberry Pi and used an AHT20 temperature sensor, a state machine, physical buttons, red and blue LEDs, an LCD display, and serial communication with a simulated thermostat server.

The thermostat supports off, heat, and cool states. The user can cycle between states and raise or lower the setpoint. The LCD displays system information, while the LEDs indicate heating or cooling behavior based on the current temperature and setpoint.

The original project was functional, but it had several limitations that made it a good candidate for enhancement:

- Most of the application’s responsibilities were contained in one Python file, making it harder to maintain and expand.
- The thermostat used a default setpoint of 72 degrees and did not retain a history of the user's temperature choices.
- It did not have a database for persistent storage, so user preferences were not available for later sessions.
- Serial communication with the simulated server added a component that was not needed for the enhanced local database design.
- Debugging output and hardware details needed clearer configuration and organization.

The capstone addresses these limitations through modular design, a preference-based algorithm, and a database layer.

## Code Review

I reviewed the original thermostat code to identify its existing functionality, design limitations, and opportunities for improvement. The review helped me plan the three enhancements and explain why each change would improve the project.

**Watch my code review:** [Thermostat Application Code Review and Enhancements on YouTube](https://www.youtube.com/watch?v=PxmpgpeLgCo)

---

## Enhancement One: Software Design and Engineering

### Purpose and changes

The first enhancement focused on improving the organization and maintainability of the thermostat application. Rather than keeping the sensor, display, state machine, and application logic together, I separated those responsibilities into individual modules:

- `main.py` coordinates the application and hardware components.
- `sensor_manager.py` handles temperature-sensor access.
- `display_manager.py` manages the LCD display.
- `state_machine.py` manages the thermostat’s operating states and setpoint behavior.
- `config.py` provides a shared debugging setting.

This structure makes the code easier to navigate and gives each module a clearer responsibility. It also provides a more manageable foundation for the later algorithm and database enhancements.

### Example code

The enhanced main program imports the separate modules rather than implementing every responsibility in one file:

```python
from sensor_manager import SensorManager
from state_machine import TemperatureMachine
from display_manager import DisplayManager
from config import DEBUG
```

The state machine also uses named constants for the default and allowed setpoint range:

```python
DEFAULT_SETPOINT = 72
MIN_SETPOINT = 45
MAX_SETPOINT = 90
```

These changes make the program’s structure and configuration easier to understand. The setpoint limits also make the intended temperature range explicit.

### Reflection

This enhancement helped me understand the difference between making software work and designing software well. Refactoring required me to understand how the original components interacted before separating them. I learned that maintainability involves clear responsibilities and deliberate design decisions, not just comments or shorter files.

### Course outcomes addressed

- **Outcome 1:** Considered how clearer organization and documentation help other developers and stakeholders understand the system and participate in future decisions. I recognize that this outcome is not demonstrated as strongly through this enhancement alone.
- **Outcome 2:** Documented the design and explained the reasoning behind the changes.
- **Outcome 4:** Applied software development and modular design practices to improve an existing computing solution.

### Full Narrative

The artifact I selected for my ePortfolio is a thermostat application I originally created earlier this year in CS-350: Emerging Systems Architectures and Technologies. I created the project as a course assignment using a Raspberry Pi, sensors, and Python to develop a functioning thermostat prototype. The project allowed me to apply software and hardware concepts together to create a working computing solution. I selected this artifact because revisiting it during my capstone allowed me to demonstrate how my approach to software development has changed throughout the Computer Science program.

When I originally created the thermostat, my primary focus was getting the hardware and software to work together successfully. The application was functional, but much of its functionality was contained within one Python module. Revisiting the project allowed me to evaluate it from a different perspective. Instead of focusing only on whether the program worked, I considered whether the code was organized in a way that would make it easier for another developer to understand, maintain, troubleshoot, and expand. The different components of the artifact also showcase several of my software development skills, including using Python to control hardware, working with a temperature sensor, implementing state machine to manage the thermostat’s behavior, handing user input through buttons, and displaying information through an LCD. This led to my Software Engineering and Design enhancement, which focused on separating the responsibilities of the original program into a Sensor Manager, State Machine, Display Manager, and main program.

The most important thing I learned from this process was the difference between making software work and designing software well. I learned that maintainability involves more than adding comments or making code easier to read. Software should also be organized so that individual components have clear responsibilities and can be modified without unnecessarily affecting other parts of the application. Revisiting code I had written earlier also showed me how much my understanding of software has grown. I was able to recognize design decisions that made sense when I was first learning but could now be improved using concepts I have developed throughout the program.

In Module One, I planned for this enhancement to support course outcomes 1, 2, and 4. I identified modular software design, separation of responsibilities, code organization, maintainability, technical communication, and collaboration as skills I wanted to demonstrate. I believe I made significant progress toward these outcomes. Outcome 4 was demonstrated through applying software development techniques to improve an existing computing solution. Outcome 2 was demonstrated through documenting the design and explaining the reasoning behind the changes. Outcome 1 was addressed by considering how clearer organization and documentation can help other developers and stakeholders understand the system and participate in decisions about future changes.

However, I recognize that Outcome 1 is not demonstrated as strongly through this enhancement as the other outcomes. I will continue addressing that outcome through my code review, documentation, and other capstone deliverables. My overall outcome-coverage plan has not changed. I will use my Algorithms and Data Structures enhancement to demonstrate algorithmic problem solving and my Database enhancement to demonstrate data management and security. This allows each enhancement to demonstrate different skills rather than trying to force every outcome into one artifact.

One of the biggest challenges I faced was determining how to separate the origin code without changing the thermostat’s behavior. Because multiple responsibilities were contained in one file, I first had to understand how the different parts interacted before deciding where they belonged. This taught me that refactoring requires more than moving code between files. It requires understanding the relationship between components and making deliberate decisions. I also learned the importance of planning before modifying an existing system.

Overall, enhancing this artifact helped me become more intentional about software development. I learned to consider maintainability, organization, communication, and future expansion instead of focusing only on whether a program functions. This experience demonstrates my growth as a computer science student and provides a strong foundation for the remaining enhancements to the thermostat.

---

## Enhancement Two: Algorithms and Data Structures

### Purpose and changes

The second enhancement allows the thermostat to use previous temperature preferences to calculate a learned setpoint for the current time period. The application identifies a time period, retrieves the preferences associated with it, and calculates an average when enough records are available.

I organized preferences into three periods of the day so the thermostat can use relevant choices instead of treating all preferences as interchangeable. The implementation keeps the existing setpoint until at least five preferences have been collected for the current period. This avoids relying on a very small amount of data. I also chose to save meaningful preferences rather than creating a record for every individual button press.

### Example code

The state machine retrieves preferences for the current period and waits until enough data is available:

```python
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
```

The algorithm uses a straightforward average because it is understandable and relatively easy to test. It also handles the case where there is not yet enough historical information by leaving the current setting unchanged.

### Reflection

This enhancement strengthened my understanding of how data collection and data organization affect algorithm design. I learned that an algorithm needs meaningful input to produce useful results. Saving every button press could create multiple records for one adjustment, so saving a preference at the end of a time period provides a more useful representation of the user's behavior.

### Course outcomes addressed

- **Outcome 2:** Explained the algorithm and the reasoning behind how preferences are collected, organized, and used.
- **Outcome 3:** Designed an algorithm that uses collected temperature data to solve a practical problem.
- **Outcome 4:** Applied Python, database retrieval, and algorithmic logic to improve the thermostat.

### Full Narrative

The artifact I selected for my ePortfolio is a thermostat application I originally created earlier this year in CS-350: Emerging Systems Architectures and Technologies. I created the project as a course assignment using a Raspberry Pi, sensors, and Python to develop a functioning thermostat prototype. The project allowed me to apply software and hardware concepts together to create a working computing solution. I selected this artifact because I identified an opportunity to improve the thermostat by allowing it to learn from user preferences and automatically select a temperature based on those preferences. By collecting the user’s selected temperature and the time period in which it was used, I was able to organize the data into three periods of the day and develop an algorithm that calculates the average preferred temperature for each period. Once enough data has been collected for a period, the thermostat can use the calculated average to automatically adjust the temperature. Developing this enhancement allowed me to strengthen my skills in data-handling, data organization, data analysis, and algorithmic decision-making. More importantly, the process helped me understand how collected data can be transformed into information that a program can use to make decisions rather than simply storing data without purpose.

One of the most important things I learned from this enhancement was that designing an algorithm requires more than determining how to calculate a result. I had to consider how the data would be collected, how it would be organized, and how the thermostat should respond when there was not yet enough information to make a reliable decision. For example, I initially considered saving a temperature every time the user pressed a button, but I realized this could create multiple records for a single temperature adjustment. I instead decided to save one temperature preference at the end of each time period. This approach provided more meaningful data because it represented the temperature the user actually used during that period rather than every individual button press. This experience helped me better understand the importance of considering how data is collected before determining how an algorithm will process it.

I believe I met the course outcomes I planned to address with this enhancement. The development process strengthened Outcome 3 by requiring me to design and evaluate an algorithm that uses collected temperature data to solve a practical problem. Rather than simply setting a fixed temperature, the thermostat now analyzes previous user preferences and uses those results to make a decision. I also addressed Outcome 4 by applying Python, database techniques, and algorithmic logic to improve an existing computing solution. Outcome 2 was addressed through the documentation and explanation of the algorithm, including the reasoning behind how the data is collected, organized, and used. At this time, I do not plan to change my outcome-coverage plan because the enhancement continues to demonstrate the outcomes identified in Module One.

Overall, this enhancement helped me develop a better understanding of how algorithmic thinking can be applied to a practical computing problem. I learned that an effective solution requires more than writing code that produces the desired result; it also requires making thoughtful decisions about what information is meaningful and how that information should be used. Working through the challenges of collecting and organizing the thermostat data helped me become more intentional about the decisions I make when designing algorithms. This experience will help me approach future projects with greater consideration for how data, logic, and user needs work together to create useful computing solutions.

---

## Enhancement Three: Databases and Security

### Purpose and changes

The third enhancement adds persistent storage using SQLite. The `DatabaseManager` class creates and accesses a table for temperature preferences, including the selected temperature, timestamp, and time period. Separating database operations from the rest of the thermostat keeps data-access responsibilities in one place and supports the preference algorithm from the second enhancement.

I also used parameterized SQL operations, limited stored information to what the application needs, and added error handling around database operations. The production configuration turns debugging output off.

### Example code

The database uses placeholders for inserted values rather than building SQL by concatenating user data:

```python
database.execute("""
    INSERT INTO temperature_preferences
    (set_temperature, timestamp, time_period)
    VALUES (?, ?, ?)
""", (temperature, timestamp, time_period))
```

In the third enhancement, the database operation is also wrapped in error handling and the connection is closed in a `finally` block:

```python
database = None

try:
    database = sqlite3.connect(DATABASE_NAME)
    database.execute("""
        INSERT INTO temperature_preferences
        (set_temperature, timestamp, time_period)
        VALUES (?, ?, ?)
    """, (temperature, timestamp, time_period))
    database.commit()

except sqlite3.Error as e:
    if DEBUG:
        print(f"An error occurred: {e}")

finally:
    if database:
        database.close()
```

The shared configuration sets debugging off for the final version:

```python
DEBUG = False
```

### Reflection

This enhancement taught me that database development involves more than storing information. I had to decide what data the thermostat actually needed, how to organize it, how the application should access it, and what should happen if a database operation failed. I also considered which security practices were appropriate for a small local application, including parameterized queries, limiting data collection, and controlling database access.

### Course outcomes addressed

- **Outcome 2:** Documented the database design and explained the decisions behind it.
- **Outcome 4:** Applied database and software development techniques to add persistent storage to the thermostat.
- **Outcome 5:** Considered data protection and privacy through parameterized queries, controlled database access, limited data collection, and error handling.

### Full Narrative

The artifact I selected for my ePortfolio is a thermostat application I originally created earlier this year in CS-350: Emerging Systems Architectures and Technologies. I created the project as a course assignment using a Raspberry Pi, sensors, and Python to develop a functioning thermostat prototype. For this enhancement, I focused on adding a database to the thermostat so that it could store and retain user temperature preferences for future use. The database stores the selected temperature, timestamp, and time period, which allows the thermostat to retain information that can be used by the application over time.

I selected this artifact because adding a database allowed me to build on the functionality of the thermostat while demonstrating skills that are important in software development and data management. The original thermostat could display the current temperature, thermostat state, and setpoint, but it did not store that information for future use. I improved the artifact by creating a SQLite database and a DatabaseManager class that controls how the thermostat stores and retrieves information. I also organized the stored preferences by time period so that the algorithm from my second enhancement could retrieve the appropriate information. Using a separate database manager helped keep database operations separate from the rest of the thermostat logic. I also used parameterized queries and limited the information stored to what the application actually needs. These changes helped me strengthen my skills in database design, data persistence, data retrieval, and secure data management.

I believe I met the course outcomes I planned to address with this enhancement. The database enhancement supports Outcome 4 by requiring me to apply database techniques and software development practices to improve an existing computing solution. Adding persistent storage gives the thermostat functionality that the original application did not have and allows information to be retained between uses. I also addressed Outcome 2 through the documentation and explanation of the database design and the decisions I made when modifying the application. Finally, this enhancement supports Outcome 5 by requiring me to consider how the user’s data should be protected. I used practices such as parameterized database queries, limiting database access to the DatabaseManager, storing only necessary information, and using database constraints and application logic to help ensure that the data being stored is appropriate. I do not currently plan to change my outcome-coverage plan because the enhancement continues to address the outcomes I intended it to.

One of the most important things I learned from this enhancement was that adding a database is more than simply creating a place to store information. I had to think about what information the thermostat actually needed, how that information should be organized, and how the rest of the application should interact with the database. I also learned the importance of considering errors that could occur during database operations. Adding error handling to the database methods helped me understand that a computing solution should account for problems that may occur rather than assuming every operation will succeed. Another challenge was determining what security measures were appropriate for this project. I initially considered different ways to protect the data, but I realized that not every security feature is necessary for a small, local thermostat application. Instead, I focused on practices that addressed actual risks, such as parameterized queries, controlled database access, limited data collection, and appropriate error handling. This process helped me understand that good database design involves making decisions based on the needs and risks of the application rather than adding complexity simply for the sake of adding features.

---

## Course Outcomes

The capstone enhancements collectively demonstrate the five CS-499 course outcomes:

1. Employ strategies for building collaborative environments that enable diverse audiences to support organizational decision making in the field of computer science
2. Design, develop, and deliver professional-quality oral, written, and visual communications that are coherent, technically sound, and appropriately adapted to specific audiences and contexts
3. Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution, while managing the trade-offs involved in design choices
4. Demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals
5. Develop a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources

## Project Files and Navigation

The following folders contain the original thermostat project and the three enhanced versions developed for my capstone. Each version demonstrates the progression of the application as I improved its organization, added temperature-preference logic, and implemented persistent database storage.

### Original Artifact

The original project was developed for CS-350: Emerging Systems Architectures and Technologies.

- [View Original Thermostat Files](https://github.com/WhytCat4/whytcat4.github.io/tree/main/original-artifact)

### Enhancement One: Software Design and Engineering

This version separates the thermostat's responsibilities into modules to improve organization, readability, and maintainability.

- [View Enhancement One Files](https://github.com/WhytCat4/whytcat4.github.io/tree/main/enhancement-one)

### Enhancement Two: Algorithms and Data Structures

This version introduces the temperature-preference algorithm, allowing the thermostat to use previous preferences organized by time period.

- [View Enhancement Two Files](https://github.com/WhytCat4/whytcat4.github.io/tree/main/enhancement-two)

### Enhancement Three: Databases and Security

This version adds SQLite database functionality to store and retrieve temperature preferences while incorporating database access controls and error handling.

- [View Enhancement Three Files](https://github.com/WhytCat4/whytcat4.github.io/tree/main/enhancement-three)

---

[Return to the top of the page](#whytcat4-computer-science-capstone)
