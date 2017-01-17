#!/usr/bin/env python
import sys
import mysql.connector
import logging
from readconfig import read_db_config

def select_query(query):
	db_config = read_db_config()
	result = True
	logging.info(query)
	try:
		conn = mysql.connector.connect(**db_config)
		if conn.is_connected():
			logging.info('Connected to MySQL database')
			cursor = conn.cursor()
			cursor.execute(query)
			result = []
			for row in cursor:
				result.append(row)

	except Exception as e:
		logging.error(e)
		result = False
	finally:
		cursor.close()
		conn.close()
		return result