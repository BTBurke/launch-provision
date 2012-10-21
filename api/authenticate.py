import yaml
from tornado.web import HTTPError

def authenticate(arguments, file='keys.yaml'):
	# TODO: Update this to store keys and tokens someplace
	# better than a flat yaml file

	key = arguments.get_argument('key', False)
	token = arguments.get_argument('token', False)

	with open(file, 'r') as f:
		key_dict = yaml.load(f)

		if key in key_dict.keys():
			if key_dict[key] == token:
				return True
			else:
				raise HTTPError(401)
		else:
			raise HTTPError(401)
	return HTTPError(401)
