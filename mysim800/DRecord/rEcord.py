import time
from mysim800.DCommunication.cOmmunicate_serial import Class_Communicate
from mysim800.DParser.jSonParser import Class_ATJSONObjectParser
from mysim800.DParser.aTParser import Class_Parser

class Class_oldRequest(Class_Communicate):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self._status_code = None
		self._json = None
		self._text = None
		self._content = None
		self._url = None
		self._IP = None

	def init(self):
		self._status_code = None
		self._json = None
		self._text = None
		self._content = None
		self._url = None
		self._IP = None

	@property
	def text(self):
		return self._text

	@property
	def IP(self):
		return self._IP

	@property
	def APN(self):
		return self._APN

	@APN.setter
	def APN(self, APN):
		self._APN = APN

	@property
	def url(self):
		return self._url

	@property
	def content(self):
		return self._content

	@property
	def status_code(self):
		return self._status_code

	def json(self):
		return self._json

	def get(self, url, header=None):
		self.init()
		self._url = url
		self._IP = self._bearer(self._APN)

		cmd = "AT + HTTPINIT"
		self._send_cmd(cmd)
		cmd = 'AT + HTTPPARA="CID",1'
		self._send_cmd(cmd)

		cmd = 'AT + HTTPPARA="URL","{}"'.format(url)
		self._send_cmd(cmd)
		time.sleep(3)
		cmd = "AT +HTTPACTION=0"

		self._send_cmd(cmd)
		time.sleep(2)
		cmd = "AT +HTTPREAD"
		self._send_cmd(cmd, get_decode_data=True)
		data = self._getdata(
			data_to_decode=[], string_to_decode=None, till=b'\n', count=2, counter=0)
		tk = Class_Parser(data)
		token = tk.tokenizer()
		self._content = tk.parser
		if (len(token) == 4):
			self._status_code = token[2]
			read_bytes = token[3]
			string = self._read_sent_data(int(read_bytes)+1000)
			tk = Class_Parser(string)

			self._content = tk.bytesparser
			self._text = tk.parser
			jph = Class_ATJSONObjectParser.ATJSONObjectParser(string)
			self._json = jph.JSONObject
		cmd = "AT +SAPBR=0,1"
		self._send_cmd(cmd)

		return self._status_code

	def post(self, url, data, waittime=4000, bytes_data=None, headers=None):
		bytes_data = len(data) +100
		self.init()
		self._url = url
		self._IP = self._bearer(self._APN)
		cmd = "AT+HTTPINIT"
		self._send_cmd(cmd)
		cmd = 'AT+HTTPPARA="CID",1'
		self._send_cmd(cmd)
		cmd = 'AT+HTTPPARA="URL","{}"'.format(url)
		self._send_cmd(cmd)
		cmd = 'AT+HTTPPARA="CONTENT","application/json"'
		self._send_cmd(cmd)
		cmd = 'AT+HTTPDATA={},{}'.format(bytes_data, waittime)
		self._send_cmd(cmd)
		# self.post.write(data)
		self._send_cmd(data)
		time.sleep(4)
		cmd = 'AT+HTTPACTION=1'
		self._send_cmd(cmd)
		time.sleep(4)
		cmd = 'AT+HTTPREAD'
		self._send_cmd(cmd, get_decode_data=True)
		data = self._getdata(
			data_to_decode=[], string_to_decode=None, till=b'\n', count=2, counter=0)
		tk = Class_Parser(data)
		self._content = tk.parser
		token = tk.tokenizer()
		if (len(token) == 4):
			self._status_code = token[2]
			read_bytes = token[3]
			string = self._read_sent_data(int(read_bytes)+1000)
			tk = Class_Parser(string)
			self._content = tk.bytesparser
			self._text = tk.parser
			jph = Class_ATJSONObjectParser.ATJSONObjectParser(string)
			self._json = jph.JSONObject
		cmd = "AT +SAPBR=0,1"
		self._send_cmd(cmd)

		return self._status_code
class Class_oldInfo(Class_Communicate):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._IMEI = None
		self._ModuleVersion = None
		self._RSSI = None
		self._simoprator = None
		self._simostats = None
		self._APN = None
		self._Latitude , self._Longitude = None,None

	@property
	def APN(self):
		return self._APN

	@property
	def Location(self):
		return self._Latitude , self._Longitude


	@APN.setter
	def APN(self,val):
		self._APN = val

	@property
	def IMEI(self):
		return self._IMEI

	@property
	def simoprator(self):
		return self._simoprator

	@property
	def ModuleVersion(self):
		return self._ModuleVersion

	def getoprator(self):
		# https://stackoverflow.com/questions/39930218/sim800-gsm-module-returns-0-on-atcops
		cmd = "AT+CSPN?"
		data = self._send_cmd(cmd, return_data=True)
		try:
			simoprator = data.decode().split(":")[1].split(",")[
				0].replace('"', "")
		except:
			simoprator = None
		self._simoprator = simoprator
		print("simoprator ->", self._simoprator)
		return self._simoprator

	def getModuleVersion(self):
		"""
		Get the module firmware version.
		"""
		cmd = "AT+CGMR"
		data = self._send_cmd(cmd, return_data=True)
		# print(data)
		try:
			moduleVersion = data.decode().split()[1].split(":")[1].split()[0]
		except:
			moduleVersion = None
		self._ModuleVersion = moduleVersion
		print("ModuleVersion ->", self._ModuleVersion)

	def getIMEI(self):
		"""
		Get the IMEI number of the module
		"""
		cmd = "AT+GSN"
		data = self._send_cmd(cmd, return_data=True)
		# print(data.decode().split())
		try:
			IMEI = data.decode().split()[1]
		except:
			IMEI = None
		self._IMEI = IMEI
		print("IMEI->", self._IMEI)

	def checkSim(self):
		cmd = "AT+CMEE=2"  # enable the extended error codes to get a verbose format
		self._send_cmd(cmd)
		cmd = "AT+cpin?"
		data = self._send_cmd(cmd, return_data=True,t=2)
	   
		try:
			simostats = data.decode().split(":")[1].split()[0]
		except:
			simostats = None
		self._simostats = simostats
		print("_simostats->", self._simostats)

	def getRSSI(self):
		"""
		Get the current signal strength in 'bars'
		"""
		cmd = "AT+CSQ"
		data = self._send_cmd(cmd, return_data=True)    
		try:
			RSSI = data.decode().split(":")[1].split()[0]
		except:
			RSSI = None
		self._RSSI = RSSI
		print("RSSI->", self._RSSI)
	
	def getLoctions(self):
		self._bearer(self._APN)
		cmd = "AT+CIPGSMLOC=1,1"
		data = self._send_cmd(cmd, return_data=True)   
		cmd = "AT+CIPGSMLOC=2,1"
		
		data = self._send_cmd(cmd, return_data=True)   
		try:
			
			self._Latitude , self._Longitude = data.decode().split()[1].split(",")[1] ,data.decode().split()[1].split(",")[2]
		except:
			self._Latitude , self._Longitude = None,None

		cmd = "AT +SAPBR=0,1"
		self._send_cmd(cmd)
		print(self._Latitude , self._Longitude )
	
	def getCBC(self):
		"battery info"
		cmd = "AT+CBC"
		data = self._send_cmd(cmd, return_data=True)  
		battery , voltage =  data.decode().split()[2].split(',')[1] ,data.decode().split()[2].split(',')[2]
		print(battery,int(voltage)/1000)
	
	def all(self):
		self.getCBC()
		self.getLoctions()
		self.getRSSI()
		self.checkSim()
		self.getIMEI()
		self.getModuleVersion()
		self.getoprator()
		
class Class_Record(Class_Communicate):

	#_send_cmd(self, cmd, 
	# 	t=1, 
	# 	bytes=14816, 
	# 	return_data=False, 
	# 	printio=False, 
	# 	get_decode_data=False,
	# 	read=True):

	def init(self):
		self._start_stats = None
		self._stop_stats = None
		self._delete_stats = None
		self._play_record_stats   = None
		self._stop_play_record_stats = None  		
		self._data_record_stats = None
		self._list_record_stats = None
		self._space_record_stats = None
		self._space_record_stats = None

	#1
	def start_record(self,id,form) -> str:
		# AT+CREC=1,1,0 
		# 1,record
		# 1,id
		# 0, amr
		# 1, wav
		cmd = "AT+CREC=1,{},{}".format(id,form)
		data = self._send_cmd(
			cmd,
			return_data=True,
			t=1,
			printio=True,
			get_decode_data=False
			)	
		try:
			_start_stats = (data.decode().split()[-1])
			if "OK" in _start_stats:
				_start_stats = True
		except:
			_start_stats = False
		return _start_stats

	#2
	def stop_record(self) -> str:
		cmd = "AT+CREC=2"
		data = self._send_cmd(
			cmd,
			return_data=True,
			t=1,
			printio=True,
			get_decode_data=False
			)	
		try:
			_stop_stats = (data.decode().split()[-1])
			if "OK" in _stop_stats:
				_stop_stats = True
		except:
			_stop_stats = False
		return _stop_stats
	
	#3
	def delete_record(self,id) -> str:
		cmd = "AT+CREC=3,{}".format(id)
		data = self._send_cmd(
			cmd,
			return_data=True,
			t=1,
			printio=True,
			get_decode_data=False
			)	
		try:
			_delete_stats = (data.decode().split()[-1])
			if "OK" in _delete_stats:
				_delete_stats = True
		except:
			_delete_stats = False
		return _delete_stats
	
	#4
	def play_record(self,id,channel,level) -> str:
		cmd = "AT+CREC=4,{},{},{}".format(id,channel,level)
		data = self._send_cmd(
			cmd,
			return_data=True,
			t=1,
			printio=True,
			get_decode_data=False
			)	
		try:
			_play_record_stats  = (data.decode().split()[-1])
			if "OK" in _play_record_stats :
				_play_record_stats  = True
		except:
			_play_record_stats  = False
		return _play_record_stats 
	
	#5
	def stop_play_record(self) -> str:
		cmd = "AT+CREC=5"
		data = self._send_cmd(
			cmd,
			return_data=True,
			t=1,
			printio=True,
			get_decode_data=False
			)	
		try:
			_stop_play_record_stats  = (data.decode().split()[-1])
			if "OK" in _stop_play_record_stats :
				_stop_play_record_stats  = True
		except:
			_stop_play_record_stats  = False
		return _stop_play_record_stats 
		
	#6
	def get_data_record(self,id,len,offset) -> str:
		cmd = "AT+CREC=6,{},{},{}".format(id,len,offset)
		data = self._send_cmd(
			cmd,
			return_data=True,
			t=1,
			printio=True,
			get_decode_data=False
			)	
		try:
			_play_record_stats  = (data.decode().split()[-1])
			if "OK" in _data_record_stats :
				_data_record_stats  = True
		except:
			_data_record_stats  = False
		return _data_record_stats
	
	#7
	def list_record(self,id) -> str:
		cmd = "AT+CREC=7,{}".format(id)
		data = self._send_cmd(
			cmd,
			return_data=True,
			t=1,
			printio=True,
			get_decode_data=False
			)	
		try:
			_list_record_stats  = (data.decode().split()[-1])
			if "OK" in _list_record_stats :
				_list_record_stats  = True
		except:
			_list_record_stats  = False
		return _list_record_stats 
	
	#a
	def space_record(self) -> str:
		cmd = "AT+CREC=8"
		data = self._send_cmd(
			cmd,
			return_data=True,
			t=1,
			printio=True,
			get_decode_data=False
			)	
		try:
			_space_record_stats  = (data.decode().split()[-1])
			if "OK" in _space_record_stats :
				_space_record_stats  = True
		except:
			_space_record_stats  = False
		return _space_record_stats

	#b
