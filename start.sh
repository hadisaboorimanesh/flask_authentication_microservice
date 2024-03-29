#!/bin/bash

flask db upgrade

gunicorn -b $SKOB_AUTHZ_BIND_ADDRESS \
	 -w $SKOB_AUTHZ_NUM_WORKERS \
	 --error-logfile - --access-logfile -  "authz:create_app()"
