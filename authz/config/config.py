from os import environ

class Config:
		ENV=environ.get("SKOB_AUTHZ_ENV", "production" )
		DBGUG=int(environ.get("SKOB_AUTHZ_DBGUG", "0" ))
		TESTING=int(environ.get("SKOB_AUTHZ_TESTING", "0" ))
	 
		
