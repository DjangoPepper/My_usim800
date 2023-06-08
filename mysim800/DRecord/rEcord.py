import time
from mysim800.DCommunication.cOmmunicate_serial import Class_Communicate
from mysim800.DParser.jSonParser import Class_ATJSONObjectParser
from mysim800.DParser.aTParser import Class_Parser


class Class_Record(Class_Communicate):

    # _send_cmd(self, cmd,
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
        self._play_record_stats = None
        self._stop_play_record_stats = None
        self._data_record_stats = None
        self._list_record_stats = None
        self._space_record_stats = None
        self._status_record_stats = None
        self._mode_record_stats = None
        self._size_record_stats = None

    # 1
    def start_record(self, id, form):
        # AT+CREC=1,1,0
        # 1,record
        # 1,id
        # 0, amr
        # 1, wav
        cmd = "AT+CREC=1,{},{}".format(id, form)
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

    # 2
    def stop_record(self):
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

    # 3
    def delete_record(self, id):
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

    # 4
    def play_record(self, id, channel, level):
        cmd = "AT+CREC=4,{},{},{}".format(id, channel, level)
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=1,
            printio=True,
            get_decode_data=False
        )
        try:
            _play_record_stats = (data.decode().split()[-1])
            if "OK" in _play_record_stats:
                _play_record_stats = True
        except:
            _play_record_stats = False
        return _play_record_stats

    # 5
    def stop_play_record(self):
        cmd = "AT+CREC=5"
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=1,
            printio=True,
            get_decode_data=False
        )
        try:
            _stop_play_record_stats = (data.decode().split()[-1])
            if "OK" in _stop_play_record_stats:
                _stop_play_record_stats = True
        except:
            _stop_play_record_stats = False
        return _stop_play_record_stats

    # 6
    def get_data_record(self, id, len, offset):
        cmd = "AT+CREC=6,{},{},{}".format(id, len, offset)
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=1,
            printio=True,
            get_decode_data=False
        )
        try:
            _play_record_datas = (data.decode().split()[-1])
            # # if "OK" in _data_record_stats:
            # if len._play_record_datas > 0:
            #     _data_record_stats = True
            # else:
            #     _data_record_stats = False
        except:
            # _data_record_stats = False
            _play_record_datas = False
        return _play_record_datas  # _data_record_stats

    # 7
    def list_record(self, id):
        cmd = "AT+CREC=7,{}".format(id)
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=1,
            printio=True,
            get_decode_data=False
        )
        try:
            _list_record_stats = (data.decode().split()[-1])
            if "OK" in _list_record_stats:
                _list_record_stats = True
        except:
            _list_record_stats = False
        return _list_record_stats

    # a
    def space_record(self):
        cmd = "AT+CREC=8"
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=1,
            printio=True,
            get_decode_data=False
        )
        try:
            _space_record_stats = (data.decode().split()[-1])
            if "OK" in _space_record_stats:
                _space_record_stats = True
        except:
            _space_record_stats = False
        return _space_record_stats

    # b
    def status_record(self):
        cmd = "AT+CREC?"
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=1,
            printio=True,
            get_decode_data=False
        )
        try:
            _status_record_stats = (data.decode().split()[-1])
            if "OK" in _status_record_stats:
                _status_record_stats = True
        except:
            _status_record_stats = False
        return _status_record_stats

    # c
    def set_mode_record(self, mode):
        cmd = "AT+DTAM={}".format(mode)
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=1,
            printio=True,
            get_decode_data=False
        )
        try:
            _mode_record_stats = (data.decode().split()[-1])
            if "OK" in _mode_record_stats:
                _mode_record_stats = True
        except:
            _mode_record_stats = False
        return _mode_record_stats

    # d
    def size_record(self, id):
        cmd = "AT+CREC=7,{}".format(id)
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=1,
            printio=False,  # only _size_record_stats will output
            get_decode_data=False
        )
        try:
            _size_record_stats = (data.decode().split(": ")[1]).split(",")[2]
        except:
            _size_record_stats = 0

        # if _size_record_stats > 0 :
        # 	# _size_record_stats  = True
        # 	_size_record_stats = 0
        # else :
        # 	_status_record_stats  = False

        return _size_record_stats

    def StartRecordAndSendAudio(self):
        # <mode>     1 Start record, to stop send anything on uart
        # <interval> range 1-50, unit is 20ms 50*20 = 1000ms soit 1s
        # <crcmode>  Data form 0 UART data is the audio data
        cmd = "AT+CRECORD=1,50,0"
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=1,
            printio=True,
            get_decode_data=False
        )
        return data

    def StopRecordAndSendAudio(self):
        cmd = "AT+CRECORD=0"
        data = self._send_cmd(
            cmd,
            return_data=True,
            t=1,
            printio=True,
            get_decode_data=False
        )
        return data
