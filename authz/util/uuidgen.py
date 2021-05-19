from uuid import uuid4

def uuidgen():
	"""Generate New UUID for  resource id  field in database"""
	return uuid4().hex
