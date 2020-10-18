# IoT-enabled-Patient-Monitoring-System
This repository contains simulation files of Proteus, embedded C program for the Microcontroller and the Python script to read and upload data to the desired web server.

Open the file named "GPS" in Proteus.
Open the embedded C code in any controller based environment like Arduino IDE or KEIL uvision.
Since there is no provision to simulate a NODE MCU in the Proteus Simulation Suite, we use a Virtual Serial Ports Emulator to create a virtual port in the System through which the Controller would be communicating.
Open the VSPE and configure 2 serial ports, COM1 and COM2 and run the same.
Open the pythonscript in any python IDE and run it.
Now start the simulation in proteus.
You will get the desired results.
Dont forget to replace the GET API URL of my channel with yours.
