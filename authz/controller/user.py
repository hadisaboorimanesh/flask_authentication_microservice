from flask import abort, request

from authz import db
from authz.model import User
from authz.schema import UserSchema
from authz.decorator import auth_required

class UserController:
	
	def craete_user():
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
		if user is not None:
			abort(409) # user is already registered
		user = User(username=data["username"],password=data["password"]) # create  new  username 
		db.session.add(user) # add  to  database  session
		try:
			db.session.commit() # database  create  query
		except:
			db.session.rollback()
			abort(500) # database  error.	
		user_schema = UserSchema()
		return {
				"user" : user_schema.dump(user)
		}, 201
	@auth_required		
	def get_users():
		try:
			users = User.query.all()
		except:
			abort(500) # database error	
		user_schema = UserSchema(many=True)
		return {
		  "users": user_schema.dump(users)
	    },200
	  
	@auth_required    
	def get_user(user_id):
		try:
			user = User.query.get(user_id) #select  the  user
		except:
			abort(500) # database  error
		if user is  None:
			abort(400)
		user_schema = UserSchema()
		return{
			"users": user_schema.dump(user)
		}, 200
	@auth_required   
	def update_user(user_id):
		if request.content_type != "application/json":
			abort(415)
		user_schema = UserSchema(only=["password"])
		try:
			data = user_schema.load(request.get_json()) #validation request data
		except:
			abort(400)
		if not data["password"]:
			abort(400)
		try:	
			user = User.query.get(user_id) #select  the  user
		except:
			abort(500) # database error	
		if user is None:
			abort(400)
		user.password = data["password"]
		try:
			db.session.commit() # database update query.
		except:
			db.session.rollback()
			abort(500) # database error
		user_schema = UserSchema()
		return{
			"user": user_schema.dump(user)
		}, 200		
		 
	@auth_required
	def delete_user(user_id):
		try:
			user=User.query.get(user_id)
		except:
			abort(500) # database  erorr	
		if user is None:
			abort(404)
		db.session.delete(user)	
		try:	
			db.session.commit()
		except:
			db.session.rollback()
			abort(500)
		return {}, 204	
