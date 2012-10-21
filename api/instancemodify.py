from boto.exception import EC2ResponseError
from api.awsconnection import connection
from api.instancestatus import get_instance_obj
from api.argutils import assert_required_args, process_args_or_defaults, required

def start_instance(instance_id):
	default = {
	'blocking': False
	}


def change_run_state_instance(instance_id, action, args):
	default = {
	'force': False
	}
	kwargs = process_args_or_defaults(args, default)

	i = get_instance_obj(instance_id)
	print i, type(i)
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


