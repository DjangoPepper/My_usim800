from mysim800.uSim800 import Class_Sim800
gsm = Class_Sim800(baudrate=9600,path="/dev/ttyS0")

def init(self):
	
	self._CMEE_STATUS = None
	self._MODE_RECORD_STATUS = None
	self._SIGNAL_STATUS = None
	self._GETSIM_STATUS = None
	self._GETREG_STATUS = None
	
	self._RECOG_STATUS = None
	self._VTD_STATUS = None

	self._DTMF_STATUS = None
	self._SETSIM_STATUS = None
	self._FLAG_ONLINE = False
	self._FLAG_CONNECTED = False
	self._CHK_CALLIN_STATUS = None
	self._FLAG_CAN_RECORD = False		
	self._FLAG_RECORDED = False
	self._FLAG_CALLCOUNTDOWN = False		
	self._USER_ID = None
	self._DTMF_SONG = ""
	self._APPELANT_SRV = None
	self._PIN_NUMBER = "0000"
	self._TELM = "0664018952"
	self._TELB = "0800943376"
	self._TEL = self.TELB
	self.byte_encoding = "ISO-8859-1"
	# self.select_line = 1

class Class_Introduction:    
	pass
	#print (gsm.info.checkSim())
	# _GETSIM_STATUS = gsm.tools.get_simpin()
	# gsm.tools.set_simpin("0000")
	# gsm.tools.send_dtmf_code("5,1,0,2")
	# gsm.sql.get_appelant(1)

class Class_Tests:    
	pass
	# gsm.tools.check_callinprogress()
	gsm.tools.get_network()
	gsm.tools.get_registration()
	
# class Class_Init:
# 	_CMEE_STATUS = gsm.tools.set_cmee(2)
# 	_MODE_RECORD_STATUS = gsm.record.set_mode_record(2)
# 	_SIGNAL_STATUS = gsm.info.getRSSI() #doir avoir une value
# 	_GETSIM_STATUS = gsm.tools.get_simpin()
# 	_GETREG_STATUS = gsm.tools.get_registration()#doit y avoir une value en return
# 	_RECOG_STATUS = gsm.tools.set_recog(0)
# 	_VTD_STATUS = gsm.tools.set_vtd(10)
# 	_FLAG_ONLINE = gsm.tools.hangup()
	
def main():
	pass
	#get dtmf song
	#force offline
	#check offline
	# make vocal server call
	# checkpoint A
	# wait 4sec
	# # if not check answering call
	# # 	 goto pointA(5try) then
	# # if ok answering 
	#		if can record 
	#			send dtmf
	#			max record time during 120s
	#			hangup,
	# 			stop record
	# 			create record name
	# 			send record
	#							
	
if __name__ == "__main__":
	main()
