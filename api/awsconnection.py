from boto.ec2.connection import EC2Connection
import os

class ConnectionPool(object):
	
	def __init__(self):
		try:
			self.AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
			self.AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
			self.conn = EC2Connection(self.AWS_ACCESS_KEY_ID, self.AWS_SECRET_ACCESS_KEY)
		except Exception, e:
			raise e, "AWS destination not reachable or key error"


def connection():
	conn = ConnectionPool()
	return conn.conn