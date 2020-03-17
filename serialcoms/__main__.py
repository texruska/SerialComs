#!/usr/bin/env python3

"""SerialComs package"""

from typing import Callable

import serial

class SerialComs:
    """SerialComs class"""
    def __init__(self, port: str, baud: int) -> None:
        """Connect to serial port"""
        self.serial = serial.Serial(port=port, baudrate=baud)

    def sendln(self, line: str) -> None:
        """Send line over port"""

    def register_callback(self, func: Callable) -> None:
        """Register callback to call when a line is received"""
