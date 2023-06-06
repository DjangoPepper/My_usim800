import serial
import time
import re
import json

class Class_Communicate:
    cmd_list = []

    def __init__(self, port):
        self._port = port

    def _setcmd(self, cmd, end='\r\n'):
        end = '\r\n'
        return (cmd + end)

    def _readtill(self,till="OK"):
        v_RCV = self._port.read(14816)
        v_RCVD = v_RCV.decode()
        while "OK" not in v_RCVD: 
            v_RCVD += v_RCV.decode()
            v_RCV = self._port.read(14816)
        return v_RCVD
    
    def _ATcmd(self):
        self._port.write(self._setcmd("AT").encode())
        v_RCV = self._port.read(14816)

    def _send_cmd(self, cmd, t=1, bytes=14816, return_data=False, 
                printio=False, get_decode_data=False,read=True):
        cmd = self._setcmd(cmd)
        self._port.write(cmd.encode())
        if read:
            time.sleep(t)
            if not get_decode_data:
                v_RCV = self._port.read(bytes)
            else:
                v_RCV = None

            if printio:
                try :
                    print(v_RCV.decode())
                except:
                    print("v_RCV Nothing to print")
            
            if return_data:
                return v_RCV

    def _read_sent_data(self, numberOfBytes):
        v_RCV = self._port.read(numberOfBytes)
        return v_RCV

    def _bearer(self,APN):
        self._ATcmd()
        
        cmd = "AT +SAPBR=0,1"
        self._send_cmd(cmd)
        
        self._ATcmd()
        
        cmd = 'AT + SAPBR=3,1,"CONTYPE","GPRS"'
        self._send_cmd(cmd)
        
        cmd = 'AT + SAPBR=3,1,"APN","{}"'.format(APN)
        self._send_cmd(cmd)
        
        cmd = "AT + SAPBR=1,1"
        self._send_cmd(cmd)
        
        cmd = "AT + SAPBR=2,1"
        data = self._send_cmd(cmd,return_data=True)
        
        try :
           IP = data.decode().split()[4].split(",")[-1].replace('"','')
        except:
            IP = None
        return IP

    def _getdata(self, data_to_decode=[], 
                 string_to_decode=None, 
                 till=b'\n', 
                 count=2, 
                 counter=0
                 ):

        v_RCV = self._port.read(1)

        if v_RCV == till:
            counter += 1
            if counter == count:
                data_to_decode.append(v_RCV)
                return b"".join(data_to_decode)
            else:
                data_to_decode.append(v_RCV)
                return self._getdata(data_to_decode, string_to_decode, till, count, counter)
        else:
            data_to_decode.append(v_RCV)
            return self._getdata(data_to_decode, string_to_decode, till, count, counter)
