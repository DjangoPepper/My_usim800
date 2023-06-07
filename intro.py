from mysim800.uSim800 import Class_Sim800
gsm = Class_Sim800(baudrate=9600,path="/dev/ttyS0")

def init(self):
		
		self._DTMF_STATUS = None
		self._VTD_STATUS = None
		self._RECOG_STATUS = None
		
		self._CMEE_STATUS = None
		self._GETSIM_STATUS = None
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

class Class_introdution:    
    pass
	#print (gsm.info.checkSim())
    # _GETSIM_STATUS = gsm.tools.get_simpin()
    # gsm.tools.set_simpin("0000")
    # gsm.tools.send_dtmf_code("5,1,0,2")
    # gsm.sql.get_appelant(1)
class Class_introdution:    
    pass
	#print (gsm.info.checkSim())
    # _GETSIM_STATUS = gsm.tools.get_simpin()
    # gsm.tools.set_simpin("0000")
    # gsm.tools.send_dtmf_code("5,1,0,2")
    # gsm.sql.get_appelant(1)


def main():
	pass
	# init_modem()
	# main_loop()
	
if __name__ == "__main__":
	main()
