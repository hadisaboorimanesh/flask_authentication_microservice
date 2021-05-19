from flask_restful import Resource
from authz.controller.user import UserController

USERS = [
   { 
     "id" :  "12345",
     "username" : "admin"
   },
   { 
     "id" :  "12345666",
     "username" : "test"
   },
   {
     "id" :  "123456661",
     "username" : "hadi"
   }
]

class UserResource(Resource):
	
	def get(self,user_id=None):
		if user_id is None:
		  return  UserController.get_users()  # get  user list 
		else:
		  return UserController.get_user(user_id) # get  single  user  
	def post(self):
	   return  UserController.craete_user()       # create New user
	    
	def patch(self,user_id):
	   return UserController.update_user(user_id) # update New user
		
	def delete(self,user_id):
	   return UserController.delete_user(user_id) # delete New user
