from boto.ec2.connection import EC2Connection
import os

class ConnectionPool(object):
	
	def __init__(self):

		self.AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
		self.AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
		self.conn = EC2Connection(self.AWS_ACCESS_KEY_ID, self.AWS_SECRET_ACCESS_KEY)



def connection():
	conn = ConnectionPool()
	return conn.conn