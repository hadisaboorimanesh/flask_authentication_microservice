from os import environ

class Config:
		ENV=environ.get("SKOB_AUTHZ_ENV", "production" )
		DBGUG=int(environ.get("SKOB_AUTHZ_DBGUG", "0" ))
		TESTING=int(environ.get("SKOB_AUTHZ_TESTING", "0" ))
		SECRET=environ.get("SKOB_AUTHZ_SEKCET", "VERY-HARD-SECURE-SEKRET-CODE" )
		JWT_ALGO=environ.get("SKOB_AUTHZ_ALGO", "HS512" )
		JWT_TOKEN_LIFETIME=int(environ.get("SKOB_AUTHZ_JWT_TOKEN_LIFETIME", "86400" ))
	 
		#### User Configuration ####
	 
		USER_DEFAULT_ROLE=environ.get("SKOB_AUTHZ_USER_DEFAULT_ROLE", "member")
		USER_DEFAULT_STATUS=environ.get("SKOB_AUTHZ_USER_DEFAULT_STATUS", "inactive")
		
		#### Database Configuration ####
		SQLALCHEMY_DATABASE_URI = environ.get("SKOB_AUTHZ_SQLALCHEMY_DATABASE_URI", None)		
		SQLALCHEMY_TRACK_MODIFICATIONS = TESTING
		
