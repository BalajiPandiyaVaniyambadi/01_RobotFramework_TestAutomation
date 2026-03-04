# UART Serial Testing using Robot Framework

This project provides an automated testing framework to validate UART serial communication using **Robot Framework** and **pyserial**.

It is designed for embedded firmware validation, hardware-in-loop testing, and regression automation.

---

## Features

- Open and close UART port
- Send and receive serial data
- Validate command/response
- Timeout handling
- Stress/loop testing
- CLI parameter override support

---

## Project Structure
uart-robot-tests/
│
├── tests/
│ ├── uart_basic.robot
│ └── uart_stress.robot
│
├── libraries/
│ └── SerialLibrary.py
│
├── requirements.txt
└── README.md