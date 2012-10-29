from tornado.web import Application, RequestHandler, HTTPError
import yaml
import json
from api.authenticate import authenticate
from api.instancestatus import InstanceStatusHandler, InstanceStatusFilterHandler
from api.instancemodify import LaunchHandler, InstanceActionHandler

class RootHandler(RequestHandler):
	def get(self):
		authenticate(self)
		self.write(yaml.load(open('api.yaml')))


app = Application([
	(r"/", RootHandler),
	(r"/v1", RootHandler),
	(r"/v1/launch", LaunchHandler),
	(r"/v1/(i-[0-9a-zA-Z]*)/(start|stop|modify|reboot|terminate)", InstanceActionHandler),
	(r"/v1/(i-[0-9a-zA-Z]*)/attributes", InstanceStatusHandler),
	(r"/v1/(i-[0-9a-zA-Z]*)/attributes/(.*)", InstanceStatusFilterHandler)
	])