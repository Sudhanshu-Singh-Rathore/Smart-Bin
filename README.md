# Smart-Bin
Dust bin based on IoT with multiple smart features. 
IoT model which displays a message on LCD on filling of dust bin and sends message to concerned department and a LED also blinks in absence of light which tells location of smart bin to people. 
This model includes:
    -LCD
    -LED
    -Ultrasonic sensor
    -Motors
    -LDR sensor
    -Raspberry Pi
Connection of pins of Raspberry Pi is as follows:
pin 15 and 16 are connected from echo and trigger pins of ultrasonic sensor(used for person detection) respectively.
pin 18 and 19 are connected from echo and trigger pins of ultrasonic sensor(used for detection of amount of garbage in the bin) respectively.

Two motors have been used to open door of the bin.
pin 7 and 11 are connected to positive and negative pin of motor1(used to open bin).
pin 12 and 13 are connected to positive and negative pin of motor1(used to open bin).

pin 21,22,23,24,26 and 29 are used to connect LCD to raspberry pi where last 4 pins are used as data pins in LCD.
pin 40 is connected to LDR sensor.
pin 35 is  connected to LED.

Do not forget to change sender and receiver's e-mail id in the code.
