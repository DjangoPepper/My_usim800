from mysim800.uSim800 import Class_Sim800
gsm = Class_Sim800(baudrate=9600, path="/dev/ttyS0")

# kk = gsm.record.size_record(1)
# print(gsm.record.get_data_record(1, kk, 0))

# gsm.tools.check_simpin("0000") must run get sim then set sim functions
if gsm.tools.get_simpin() == False:
    gsm.tools.set_simpin("0000")

# gsm.info.checkSim()

gsm.tools.call("0664018952")
gsm.tools.CallIn
