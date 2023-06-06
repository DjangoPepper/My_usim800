# from ATRequests import requests
from mysim800.DSms.sMs import Class_Sms
from mysim800.DCommunication.cOmmunicate_serial import Class_Communicate
from mysim800.DRequest.rEquest import Class_Request
from mysim800.DInfo.iNfo import Class_Info
from mysim800.DRecord.rEcord import Class_Record
from mysim800.DTools.tOols import Class_Tools
from mysim800.DSql.sQl import Class_MySql


import serial

class Class_Sim800(Class_Communicate):
    TIMMEOUT = 1

    def __init__(self, baudrate, path):
        self.port = serial.Serial(path, baudrate, timeout=Class_Sim800.TIMMEOUT)
        super().__init__(self.port)
        
        self.requests = Class_Request(self.port)
        self.info = Class_Info(self.port)
        self.sms = Class_Sms(self.port)
        self.record = Class_Record(self.port)
        self.tools = Class_Tools(self.port)
        self.sql = Class_MySql(self.port)