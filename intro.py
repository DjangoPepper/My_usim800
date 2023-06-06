from mysim800.uSim800 import Class_Sim800
gsm = Class_Sim800(baudrate=9600,path="/dev/ttyS0")

def init(self):
		self._chkcallin_stats = None
		self._dtmf_stats = None
		self._vtd_stats = None
		self._recog_stats = None
		self._cmee_stats = None
		self._getsim_stats = None
		self._setsim_stats = None

class Class_introdution:    
    #print (gsm.info.checkSim())
    _getsim_stats = gsm.tools.get_simpin()
    # gsm.tools.set_simpin("0000")
    # gsm.tools.send_dtmf_code("5,1,0,2")
    gsm.sql.get_appelant(1)
