from mysim800.uSim800 import Class_Sim800
# from usim800.Info.info import info
gsm = Class_Sim800(baudrate=9600,path="/dev/ttyS0")
# gsm.sms.send("8850813167","hi from usim800")
# print ("module : ", info.ModuleVersion)
# print ("IMEI is:", info.getIMEI)
# print (gsm.info.checkSim())
# print (gsm.info.all())
#gsm.record.start_record(1,0)
gsm.record.size_record(1)
