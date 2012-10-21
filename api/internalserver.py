from tornado.web import Application, RequestHandler, HTTPError
import yaml
from api.authenticate import authenticate
from api.instancestatus import get_instance_status

class RootHandler(RequestHandler):
	def get(self):
		authenticate(self)
		self.write(yaml.load(open('api.yaml')))
	def put(self):
		raise HTTPError(403)
	def post(self):
		raise HTTPError(403)
	def delete(self):
		raise HTTPError(403)

class InstanceActionHandler(RequestHandler):
	def put(self, instance_id, action):
		authenticate(self)
		print instance_id, action

	def get(self):
		raise HTTPError(403)

class InstanceStatusHandler(RequestHandler):
	def get(self, instance_id):
		authenticate(self)
		status = get_instance_status(instance_id)
		if status:
			self.write(status)
		else:
			raise HTTPError(404)

	def post(self, instance_id):
		raise HTTPError(403)
	def delete(self, instance_id):
		raise HTTPError(403)
	def put(self, instance_id):
		raise HTTPError(403)

class InstanceStatusFilterHandler(RequestHandler):
	def get(self, instance_id, filter):
		authenticate(self)
		status = get_instance_status(instance_id, filter=[str(filter)])
		if status:
			self.write(status)
		else:
			raise HTTPError(404)

	def post(self, instance_id):
		raise HTTPError(403)
	def delete(self, instance_id):
		raise HTTPError(403)
	def put(self, instance_id):
		raise HTTPError(403)

class LaunchHandler(RequestHandler):
	def put(self):
		authenticate(self)


app = Application([
	(r"/", RootHandler),
	(r"/v1/", RootHandler),
	(r"/v1/launch", LaunchHandler),
	(r"/v1/(i-[0-9a-zA-Z]*)/(start|stop|modify)", InstanceActionHandler),
	(r"/v1/(i-[0-9a-zA-Z]*)/attributes", InstanceStatusHandler),
	(r"/v1/(i-[0-9a-zA-Z]*)/attributes/(.*)", InstanceStatusFilterHandler)
	])