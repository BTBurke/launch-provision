from tornado.web import Application, RequestHandler, HTTPError
import yaml
import json
from api.authenticate import authenticate
from api.instancestatus import get_instance_status
from api.instancemodify import change_run_state_instance

class RootHandler(RequestHandler):
	def get(self):
		authenticate(self)
		self.write(yaml.load(open('api.yaml')))


class InstanceActionHandler(RequestHandler):
	def put(self, instance_id, action):
		authenticate(self)
		if action == 'modify':
			pass
		else:
			ret = change_run_state_instance(instance_id, action, self)
			print json.dumps(ret)


class InstanceStatusHandler(RequestHandler):
	def get(self, instance_id):
		authenticate(self)
		status = get_instance_status(instance_id)
		if status:
			self.write(status)
		else:
			raise HTTPError(404)


class InstanceStatusFilterHandler(RequestHandler):
	def get(self, instance_id, filter):
		authenticate(self)
		status = get_instance_status(instance_id, filter=[str(filter)])
		if status['status'] == 200:
			self.write(status)
		else:
			raise HTTPError(status['status'])



app = Application([
	(r"/", RootHandler),
	(r"/v1/", RootHandler),
	(r"/v1/launch", LaunchHandler),
	(r"/v1/(i-[0-9a-zA-Z]*)/(start|stop|modify|reboot|terminate)", InstanceActionHandler),
	(r"/v1/(i-[0-9a-zA-Z]*)/attributes", InstanceStatusHandler),
	(r"/v1/(i-[0-9a-zA-Z]*)/attributes/(.*)", InstanceStatusFilterHandler)
	])