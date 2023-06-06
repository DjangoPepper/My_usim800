import mysql.connector
MYSQL_CONNECT_PARAMS = {
  'user': 'root', #racine
  'password': 'pepper',#mylittledog
  'host': '127.0.0.1',#localip
  'database': 'stem_db',#jobets_db
  'raise_on_warnings': True
}

class Class_MySql(object):
	def get_appelant(userid):
		request = "SELECT code FROM identité WHERE id={}".format(userid)
		with mysql.connector.connect(**MYSQL_CONNECT_PARAMS) as db :
			with db.cursor() as c:
				c.execute(request)
				while True:
					APPELANT_SRV = c.fetchone()
					if APPELANT_SRV is None:
						print("sql error")
						return "nobody"
						break
						

					APPELANT_SRV = APPELANT_SRV[0]
					print("{} can call server".format(APPELANT_SRV))
					LIST_OF_DIGIT = [int(x) for x in str(APPELANT_SRV)]
					# print("Singing DTMF")
					DTMF_MSG =('1,"' + \
								str(LIST_OF_DIGIT[0]) + ',' + \
								str(LIST_OF_DIGIT[1]) + ',' + \
								str(LIST_OF_DIGIT[2]) + ',' + \
								str(LIST_OF_DIGIT[3]) + \
								'",100')
					return DTMF_MSG, APPELANT_SRV
