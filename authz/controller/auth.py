from flask import abort, request
from jwt import encode
from authz import db
from time import time
from authz.config import Config
from authz.model import User
from authz.schema import UserSchema
from authz.util import now

class AuthTokenController:
	
	def create_token():
		if request.content_type != "application/json":
			abort(415) # Bad Media Type
		user_schema = UserSchema(only=["username","password"])
		try:
			data = user_schema.load(request.get_json()) #validation request data
		except:
			abort(400) # invalid request
		if not data["username"]	or not data["password"]:
		   abort(400) # empty Data
		try:
			user = User.query.filter_by(username=data["username"]).first() # select a user from db
		except:
			abort(500) # database error	
		if user is None:
			abort(404) # user is not found
		if user.password != data["password"]:
			user.last_failed_at = now()
			try:
				db.session.commit()
			except:
				db.session.rollback()
				abort(500) # database error
			abort(403)	
		current_time = time()
		try:
			jwt_token = encode(
				{
					"nbf": current_time,
					"exp": current_time + Config.JWT_TOKEN_LIFETIME,
					"user": {
						"id": user.id,
						"username": user.username,
						"role": user.role,
					}
				},
				Config.SEKRET,
				algorithm=Config.JWT_ALGO	
			) # create  new jwt token
		except:
			abort(500) # jwt encode error 
		user_schema = UserSchema()
		return {
			"user": user_schema.dump(user) 
		}, 201, {"X-Subject-Token": jwt_token}
