from functools import wraps
from flask import  abort,request
from authz import  db
from authz.model import User
from authz.schema import UserSchema
from authz.rule import ControllerRule
from jwt import decode
from authz.config import Config

def auth_required(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		jwt_token = request.headers.get("X-Auth-Token")
		if jwt_token is None:
			abort(401) # X-Auth-Token is not  found
		try:
			data = decode(jwt_token, Config.SECRET,algorithms=[Config.JWT_ALGO])
		except:
			abort(500)
		controller_rules = 	ControllerRule.get_controller_rules(f.__name__)
		if data["user"]["role"] in controller_rules:
			return f(*args, **kwargs)
		elif data["user"]["role"] == "member" and "member:user_id" in controller_rules:
			user_id = args[f.__code__.co_varnames.index("user_id")]
			if data["user"]["id"] == user_id:
				return f(*args, **kwargs)
			else:
				abort(403)	
		else:
				abort(403)
	return wrapper
	
