import json
from tornado.web import RequestHandler, HTTPError
from boto.exception import EC2ResponseError
from api.awsconnection import connection
from api.instancestatus import get_instance_obj
from api.argutils import assert_required_args, process_args_or_defaults, required


class LaunchHandler(RequestHandler):
	def put(self):
		authenticate(self)
		ret = launch_instance(self)
		self.set_status(ret['status'])
		self.write(json.dumps(ret['body']))

class InstanceActionHandler(RequestHandler):
	def put(self, instance_id, action):
		authenticate(self)
		if action == 'modify':
			modify_instance(instance_id, self)
		else:
			ret = change_run_state_instance(instance_id, action, self)
            self.set_status(ret['status'])
			self.write(json.dumps(ret['body']))


def change_run_state_instance(instance_id, action, args):
	default = {
	'force': False
	}
	kwargs = process_args_or_defaults(args, default)

	i = get_instance_obj(instance_id)
	
	if not i:
		return {'status': 404, 'body': 'Instance not found'}

	try:
		if action == 'stop':
			i.stop()
		elif action == 'terminate':
			i.terminate()
		elif action == 'reboot':
			i.reboot()
		elif action == 'start':
			i.start()
		else:
			pass	
	except Exception, e:
		return {'status': 408, 'body': 'Error while trying to stop instance via EC2 API. ' + str(e) }

	return {'status': 200, 'body': instance_id + ' ' + action}

def modify_instance(instance_id, args):
	default = {
	'attribute': required(),
	'value': required()
	}

	kwargs = process_args_or_defaults(args, defaults)
	if assert_required_args(kwargs):
		instance_obj = get_instance_obj(instance_id)
		if not instance_obj:
			return {'status': 404, 'body': 'Instance not found'}
		else:
			success = instance_obj.modify_attribute(kwargs['attribute'], kwargs['value'])
			if success:
				return {'status': 200, 'body': 'Instance modification succeeded'}
			else:
				return ('status': 408, 'body': 'Instance modification failed.')
	else:
		return {'status': 408, 'body': 'Required arguments attribute and value not provided'}

def launch_instance(args):
	default = {
	'instance_type': required(),
	'image_id': required(),
	'min_count': 1,
	'max_count': 1,
	'key_name': 'scalacity-dev1',
	'security_groups': ['SSH'],
	'user_data': '',
	'placement': 'us-east-1b',
	'placement_group': '',
	'instance_initiated_shutdown_behavior': 'terminate',
	'ebs_optimized': False
	}

	kwargs = process_args_or_defaults(args, default)

	reservation = None
	if assert_required_args(kwargs):
		conn = connection()
		arg = kwargs.pop('image_id')
		try:
			reservation = conn.run_instances(arg, **kwargs)
		except EC2ResponseError, e:
			ret = {'status': 408, 'body': 'Error while trying to run instance.  Possible malformed request or unavailable endpoint.'}
	else:
		ret = {'status': 400, 'body': 'Required arguments not provided.'}

	if not reservation:
		return ret
	else:
		inst_ids = [i.id for i in reservation.instances]
		return {'status': 200, 'body': inst_ids}

def modify_instance(instance_id, args):
	pass


