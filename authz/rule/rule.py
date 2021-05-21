class ControllerRule:
	
	__controllers = {
		"get_users": ["admin"],
		"get_user": ["admin","member:user_id"],
		"update_user": ["admin","member:user_id"],
		"delete_user": ["admin"]	
	}
	def get_controller_rules(name):
		return ControllerRule.__controllers.get(name)
