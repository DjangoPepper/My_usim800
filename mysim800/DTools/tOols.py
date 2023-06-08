#!/usr/bin/env python
# -*- coding:utf-8 -*-
# All missing at command not in record, sms, info, request,sql code
from mysim800.DCommunication.cOmmunicate_serial import Class_Communicate
from mysim800.DParser.jSonParser import Class_ATJSONObjectParser
from mysim800.DParser.aTParser import Class_Parser
import time
import datetime


class Class_Tools(Class_Communicate):

    def init(self):
        self._CALL_MADE = None
        self._DTMF_STATUS = None
        self._VTD_STATUS = None
        self._RECOG_STATUS = None
        self._CMEE_STATUS = None
        self._GETSIM_STATUS = None
        self._SETSIM_STATUS = None
        self.byte_encoding = "ISO-8859-1"
        self.select_line = 2
        self.select_word = None

    def CreateSoundAMR(_APPELANT_SRV):
        FILENAME = str(_APPELANT_SRV) + "_" + \
            str(datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')) + ".amr"
        return FILENAME

    def CreateSoundFileName(_APPELANT_SRV):
        FILENAME = str(_APPELANT_SRV) + "_" + \
            str(datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')) + ".wav"
        return FILENAME

    def CallCountDown(t):
        # define the countdown func.

        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

    def CallIn(self):  # default FLAGS ARE FALSE
        cmd = "AT+CLCC?"
        data = self._send_cmd(cmd, return_data=True, t=1,
                              printio=True, get_decode_data=False)

        try:
            data = (data.decode().split()[-1])
            length_data = len(data)
            if length_data and data == "OK":
                # try:
                bidir = (data.decode().split()[1]).split(": ")[1].split(",")[0]
                state = (data.decode().split()[1]).split(": ")[1].split(",")[2]
                _CALLIN_STATUS = True
        except:
            bidir = 9
            state = 9
            _CALLIN_STATUS = False
        # else :
        # 	return False

        # 	_status_record_stats  = (data.decode().split()[-1])
        # 	if "OK" in _status_record_stats :
        # 		_status_record_stats  = True
        # except:
        # 	_status_record_stats  = False
        return _CALLIN_STATUS

    def send_dtmf_code(self, recipient_dtmf):

        # AT+CLDTMF=? +CLDTMF:(1-100),(0-9,A,B,C,D,*,#),(10-100)
        # AT+CLDTMF=1,”5,1,0,2”,100
        # AT+CLDTMF reset/stop
        cmd = ("AT+CLDTMF={}".format(recipient_dtmf))
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=1,
            printio=True,
            get_decode_data=False
        )
        # data = (data.decode().split()[-1])
        try:
            _DTMF_STATUS = (data.decode().split()[-1])
            if "OK" in _DTMF_STATUS:
                _DTMF_STATUS = True
        except:
            _DTMF_STATUS = False
        return _DTMF_STATUS

    def set_vtd(self, value):
        # AT+VTD=10 1sec

        cmd = ("AT+VTD={}".format(value))
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=1,
            printio=True,
            get_decode_data=False
        )
        # data = (data.decode().split()[-1])
        try:
            _VTD_STATUS = (data.decode().split()[-1])
            if "OK" in _VTD_STATUS:
                _VTD_STATUS = True
        except:
            _VTD_STATUS = False
        return _VTD_STATUS

    def set_recog(self, value):
        cmd = ("AT+COLP={}".format(value))
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=1,
            printio=True,
            get_decode_data=False
        )
        # data = (data.decode().split()[-1])
        try:
            _RECOG_STATUS = (data.decode().split()[-1])
            if "OK" in _RECOG_STATUS:
                _RECOG_STATUS = True
        except:
            _RECOG_STATUS = False
        return _RECOG_STATUS

    def set_cmee(self, value):
        cmd = ("AT+CMEE={}".format(value))
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=1,
            printio=True,
            get_decode_data=False
        )
        # data = (data.decode().split()[-1])
        try:
            _CMEE_STATUS = (data.decode().split()[-1])
            if "OK" in _CMEE_STATUS:
                _CMEE_STATUS = True
        except:
            _CMEE_STATUS = False
        return _CMEE_STATUS

    def get_simpin(self):
        cmd = ("AT+CPIN?")
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=2,
            printio=True,
            get_decode_data=False,
            get_lines_data=False,
            select_line=False
        )
        # data = (data.decode().split()[-1])
        try:
            _GETSIM_STATUS = (data.decode().split(":")[1].split()[0])
            if "READY" in _GETSIM_STATUS:
                _GETSIM_STATUS = True
        except:
            _GETSIM_STATUS = False

        return _GETSIM_STATUS

    def set_simpin(self, newpin):
        cmd = ("AT+CPIN={}".format(newpin))
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=5,
            printio=True,
            get_decode_data=False
        )
        # data = (data.decode().split()[-1])
        try:
            _SETSIM_STATUS = (data.decode().split()[-1])
            if "OK" in _SETSIM_STATUS:
                _SETSIM_STATUS = True
        except:
            _SETSIM_STATUS = False
        return _SETSIM_STATUS

    def get_registration(self):  # Initial version of network
        cmd = ("AT+CREG?")
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=1,
            printio=True,
            get_decode_data=False,
            get_lines_data=False,  # data to lines True/False
            select_line=False  # extract line False,0,1,2,...
        )
        _REG_STATUS = data
        return _REG_STATUS

    def get_network(self):
        cmd = ("AT+CREG?")
        data = self._send_cmd(
            cmd,  # command
            return_data=True,  # return data
            t=1,  # timeout
            printio=True,  # print output
            get_decode_data=False,  # decode data ?
            get_lines_data=False,  # data to lines True/False
            select_line=False  # extract line False,0,1,2,...
        )
        _CALL_MADE = data
        return _CALL_MADE

    def hangup(self):
        cmd = ("ATH")
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=1,
            printio=True,
            get_decode_data=False
        )
        # data = (data.decode().split()[-1])
        try:
            print(self.data_cmd(data))
        # 	_HANGUP_STATUS = (data.decode().split()[-1])
        # 	if "OK" in _HANGUP_STATUS:
        # 		_HANGUP_STATUS = True
        except:
            _HANGUP_STATUS = False
        return _HANGUP_STATUS

    def call(self, number: str):
        cmd = ("ATD{};".format(number))
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=5,
            printio=True,
            get_decode_data=False,
            get_lines_data=False,  # data to lines True/False
            select_line=False  # extract line False,0,1,2,...
        )
        # data = (data.decode().split()[-1])
        try:
            _CALL_MADE = (data.decode().split()[-1])
            if "OK" in _CALL_MADE:
                _CALL_MADE = True
        except:
            _CALL_MADE = False
        return _CALL_MADE
