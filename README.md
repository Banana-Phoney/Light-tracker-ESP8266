# Light-tracker-ESP8266
Light tracking using micropython on ESP8266

Start of a project to make a sun tracker for a little solarpanel.

The ESP8266 only have one pin to read the input from the light dependandt resistors, so i ended up using GPIO4 and GPIO5 to power the resistors individually.
The only problem was that the readings became a bit unreliable with that setup, by adding 2 diode's the current seemed to become more stable.
To lower the voltage down to 1V a 10k resistor was used towards ground.

Parts so far:

  1 x ESP8266 NodeMCU.
  
  1 X MG90S Servo - generic.
  
  2 X Light dependent resistors.
  
  2 X Diode's.
  
  1 X 10k resistor.
  
  1 X Medium breadboard.
  
  wires.


Connection schematic 
![Schematic2](/Images/Schematic2.png)

The solar panel "construction"
![solarpanel_construction](/Images/solarpanel_construction.jpg)

The electronic parts are cramed in and is held up with double sided tape.
![electronics](/Images/electronics.jpg)

Picture from the top of the setup
![Top](/Images/Top.jpg)

Picture from the side of the setup
![Side](/Images/Side.jpg)
