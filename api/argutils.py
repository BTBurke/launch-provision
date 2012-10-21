
class required(object):
	"""
	Implements a required type for specifying which arguments
	are required to be overridden when the method is called.
	"""
	pass


def assert_required_args(args):
	
	for k in args.keys():
		if isinstance(args[k], required):
			return False
	return True

def process_args_or_defaults(args, defaults):
	
	return_args = {}
	for k in defaults.keys():
		arg1 = args.get_argument(k, defaults[k])
		return_args.update({k: arg1})
	return return_args
