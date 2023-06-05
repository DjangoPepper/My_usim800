# from ATRequests import requests
from mysim800.DSms import Csms
from mysim800.Communicate_serial import  Ccommunicate
from mysim800.DRequest import request
from mysim800.DInfo import info
import serial

class Csim800(communicate):
    TIMMEOUT = 1

    def __init__(self, baudrate, path):
        self.port = serial.Serial(path, baudrate, timeout=sim800.TIMMEOUT)
        super().__init__(self.port)
        self.requests = request(self.port)
        self.info = info(self.port)
        self.sms = sms(self.port)

