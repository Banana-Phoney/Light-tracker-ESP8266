# Light-tracker-ESP8266
Light tracking using micropython on ESP8266

Start of a project to make a sun tracker for a little solarpanel.

The ESP8266 only have one pin to read the input from the light dependandt resistors, so i ended up using GPIO4 and GPIO5 to power the resistors individually.
The only problem was that the readings became a bit unreliable with that setup, by adding 2 diode's the current seemed to become more stable.
To lower the voltage down to 1V a 10k resistor was used towards ground.

Parts so far:

  1 x ESP8266 NodeMCU.
  
  1 X 28BYJ-48 step motor
  
  1 X https://www.clasohlson.com/no/Exibel%2C-solcellelader-med-USB-10-W/p/Pr388533000 This is what i scavenged both solar panels and the usb controller.
  
  1 X The powerbank i use is one that can charge and be used at the same time and i have a few of. https://www.clasohlson.com/no/Clas-Ohlson,-Powerbank-6700-mAh/p/38-9060-1
  
  1 X ULN2003APG step motor driver board.
  
  2 X Light dependent resistors.
  
  2 X Diode's.
  
  1 X 10k resistor.
  
  1 X Medium breadboard.
  
  wires.


Connection schematic (error: wire after the resistor should go to ground not 5v) 
![Schematic2](/Images/Schematic2.png)

The solar panel "construction"
![solarpanel_construction](/Images/solarpanel_construction.jpg)

The electronic parts are cramed in and is held up with double sided tape.
![electronics](/Images/electronics.jpg)

Picture from the top of the setup
![Top](/Images/Top.jpg)

Picture from the side of the setup
![Side](/Images/Side.jpg)
