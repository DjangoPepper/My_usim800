# from ATRequests import requests
from mysim800.DSms import Class_Sms
from mysim800.cOmmunicate_serial import  Class_Communicate
from mysim800.DRequest import Class_Request
from mysim800.DInfo import Class_Info
import serial

class Class_Sim800(Class_Communicate):
    TIMMEOUT = 1

    def __init__(self, baudrate, path):
        self.port = serial.Serial(path, baudrate, timeout=Class_Sim800.TIMMEOUT)
        super().__init__(self.port)
        self.requests = Class_Request(self.port)
        self.info = Class_Info(self.port)
        self.sms = Class_Sms(self.port)

