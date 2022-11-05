## Problem Statement

- In LNMIIT we always carry our Institute ID with us thus if we need to board a college bus from the main gate we have to show our bus pass and well as our college ID.
- We can make our bus pass redundant if we can make smart use of our college ID.
- In this project, I intend to build an RFID Powered Smart Pass Access Control System using Raspberry Pi microprocessor.
- We have already seen this kind of services implemented in big hospitals or companies and even in different colleges across the world, e.g, in National Ilan University, we might have seen how they used RFID based locks to restrict access to certain areas.
- The same system can be used in other systems like RFID based door lock or RFID based access management system and even in Smart Card payments.

## Proposal 

- At present, there are generally two methods for access control: recording on the paper or managing with technology.
- However, managing with paper-based technology has a critical drawback, they can get lost, can get easily destroyed with external conditions and cost an environment damage with cutting down of tree for making pulp to produce paper.
- RFID technology is stronger in its ability to withstand harsh environment, fast access time are its key component.
- This project is clearly useful in the scenario of LNMIIT, where there is a huge rush outside the gate whenever the college bus arrives from the city to get their bus pass punched.
- Our college ID’s are embedded with a RFID identification chip inside with a unique code allotted to all the students thus if we combine with server containing the details to process students faster.

## Solution Tech 

- Build a real-time system RFID powered smart pass access control system using EM-18 RFID Module and Raspberry-pi.
- Implement a server in FLASK framework with dedicated SQL database maintaining all the user’s information.
- Establish the interfacing between the Raspberry pi and the Remote Server. 

## Tech Stack

__POS-END:__ Python, Request , Python Json

__Backend:__ Python 2.7, Flask Framework, SQLAlchemy, Bootstrap Framework 

## Control Flow 

1. Student taps its RFID card in the RFID scanner.
2. The Information (unique rfid_no) is transmitted to the Raspberry pi via serial port.
3. The Raspberry pi encodes the information (rfid_no) into the Json format and transmit it to the Server.
4. The Server parses the information and check the statement balance regarding that rfid_no in SQL database and return a Boolean response signifying whether to grant access or not.
5. The response is transmitted back to the Raspberry pi via WIFI and it parses the information and takes the appropriate step


![Flowchart](/Screenshots/Flowchart.png "Flowchart")


## Circuit Diagram 

![Flowchart](/Screenshots/CircuitDiagram.png "Circuit Diagram")

