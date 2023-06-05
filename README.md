usim800
==========================
[![image](https://img.shields.io/badge/build-passing-green.svg)](https://pypi.org/project/usim800/)
[![image](https://img.shields.io/github/license/Bhagyarsh/usim800.svg)](https://pypi.org/project/usim800/)
[![image](https://img.shields.io/pypi/v/usim800.svg)](https://pypi.org/project/usim800/)

from usim800 Python driver module for SIM800 socket . 
Its has easy-to-use api to access GPRS.
Changes made to clarify directoriess, files, classes names for my personnal use and undertstanding.



Quick start :
------------
### Import

``` {.sourceCode .python}
>>> from mysim800.uSim800 import Class_Sim800

>>> import json
>>> gsm = sim800(baudrate=9600,path="/dev/ttyS0")
```
### set APN

``` {.sourceCode .python}
>>> gsm.requests.APN = "www"
```
### get and post request
``` {.sourceCode .python}
>>> gsm.requests.get(url="http://my-json-server.typicode.com/typicode/demo/posts")
>>> r = gsm.requests
>>> r.status_code
'200'
>>> r.content
b'[  {    "id": 1,    "title": "Post 1"  },  {    "id": 2,    "title": "Post 2"  },  {    "id": 3,    "title": "Post 3"  }]'
>>> r.json()
[[{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]]
>>> r.IP
'10.110.188.15'
>>> data = {"name":"somthing...."}
>>> gsm.requests.post(url="http://ptsv2.com/t/usim800/post",data=json.dumps(data))
'201'
>>> r.status_code
'201'
>>> r.content
b'Thank you for this dump. I hope you have a lovely day!'

>>> r.IP
'10.182.199.208'
```
SMS
``` {.sourceCode .python}
>>> gsm.sms.send("8850813167","hi from usim800")
True
```
Future Plan and  improvements
------------
* better error handling
