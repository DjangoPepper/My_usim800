#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
from mysim800.DCommunication.cOmmunicate_serial import Class_Communicate
from mysim800.DParser.jSonParser import Class_ATJSONObjectParser
from mysim800.DParser.aTParser import Class_Parser
import time, datetime

class Class_Tools(Class_Communicate):

	
	def init(self):
		self._chkcallin_stats = None
		self._dtmf_stats = None
		self._vtd_stats = None
		self._recog_stats = None
		self._cmee_stats = None
		self._getsim_stats = None
		self._setsim_stats = None
		
	def CreateSoundAMR(_APPELANT_SRV):
		FILENAME = str(_APPELANT_SRV) + "_" + str(datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')) + ".amr"
		return FILENAME

	def CreateSoundFileName(_APPELANT_SRV):
		FILENAME = str(_APPELANT_SRV) + "_" + str(datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')) + ".wav"
		return FILENAME

	def CallCountDown(t):
		# define the countdown func.
		
		while t:
			mins, secs = divmod(t, 60)
			timer = '{:02d}:{:02d}'.format(mins, secs)
			print(timer, end="\r")
			time.sleep(1)
			t -= 1

	def check_callinprogress(self): #default FLAGS ARE FALSE
		cmd = "AT+CLCC"
		data = self._send_cmd(
			cmd,
			return_data=True,
			t=1,
			printio=True,
			get_decode_data=False
			)	
		
		try:
			data = (data.decode().split()[-1])
			length_data = len(data)
			if length_data and data == "OK":
			# try:
				bidir = (data.decode().split()[1]).split(": ")[1].split(",")[0]
				state = (data.decode().split()[1]).split(": ")[1].split(",")[2]
				_chkcallin_stats = True
		except:
				bidir = 9
				state = 9
				_chkcallin_stats = False
		# else : 
		# 	return False

		# 	_status_record_stats  = (data.decode().split()[-1])
		# 	if "OK" in _status_record_stats :
		# 		_status_record_stats  = True
		# except:
		# 	_status_record_stats  = False
		return _chkcallin_stats

	def send_dtmf_code(self, recipient_dtmf):
		
		#AT+CLDTMF=? +CLDTMF:(1-100),(0-9,A,B,C,D,*,#),(10-100)
		#AT+CLDTMF=1,”5,1,0,2”,100
		#AT+CLDTMF reset/stop
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
			_dtmf_stats = (data.decode().split()[-1])
			if "OK" in _dtmf_stats:
				_dtmf_stats = True
		except:
			_dtmf_stats = False
		return _dtmf_stats
	
	def set_vtd(self, value):
		#AT+VTD=10 1sec
		
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
			_vtd_stats = (data.decode().split()[-1])
			if "OK" in _vtd_stats:
				_vtd_stats = True
		except:
			_vtd_stats = False
		return _vtd_stats

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
			_recog_stats = (data.decode().split()[-1])
			if "OK" in _recog_stats:
				_recog_stats = True
		except:
			_recog_stats = False
		return _recog_stats
	
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
			_cmee_stats = (data.decode().split()[-1])
			if "OK" in _cmee_stats:
				_cmee_stats = True
		except:
			_cmee_stats = False
		return _cmee_stats

	def get_simpin(self):
		cmd = ("AT+CPIN?")
		data = self._send_cmd(
			cmd,
			return_data=True,
			t=1,
			printio=True,
			get_decode_data=False
			)
		# data = (data.decode().split()[-1])		
		try:
			# simostats = data.decode()
			# simostats = simostats.split(":")[1]
			# simostats = simostats.split()[0]
			_getsim_stats = (data.decode().split(":")[1].split()[0])
			if "READY" in _getsim_stats:
				_getsim_stats = True
		except:
			_getsim_stats = False
			
		return _getsim_stats

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
			_setsim_stats = (data.decode().split()[-1])
			if "OK" in _setsim_stats:
				_setsim_stats = True
		except:
			_setsim_stats = False
		return _setsim_stats

