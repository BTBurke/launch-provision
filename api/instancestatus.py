from boto.exception import EC2ResponseError
from api.awsconnection import connection

def get_instance_status(instance_id, filter=None):
	instance_obj = get_instance_obj(str(instance_id))
	i = instance_obj.__dict__

	return_map = ('id', 'public_dns_name', 'private_dns_name', 
	'key_name', 'instance_type', 'launch_time',
	'image_id', 'private_ip_address', 'ip_address')

	status = {k: i[k] for k in return_map}
	status.update({'state': i['_state'].name})
	status.update({'state_code': i['_state'].code})
	status.update({'placement': i['_placement'].zone})
	status.update({'placement_group': i['_placement'].group_name})

	if filter:
		filter_status = {k: status[k] for k in filter if k in status.keys()}
		return filter_status
	else:
		return status

def get_instance_obj(instance_id):
	instance_id = str(instance_id)
	conn = connection()
	try:
		reservation = conn.get_all_instances(instance_ids=instance_id)
	except EC2ResponseError:
		return False
	return reservation[0].instances[0]

if __name__ == '__main__':
	print get_instance_status('i-a8e4d0d5', ['instance_type'])

