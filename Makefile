DEBUG ?= 1

SOURCES_FOLDER := src
CREATE_DB_FILE = $(SOURCES_FOLDER)/connect_db.py
VIEWS_FILE 		 = $(SOURCES_FOLDER)/views.py


.DEFAULT_GOAL := run_api


create_db:
	python3 $(CREATE_DB_FILE) ;

run_api:
	fastapi dev $(VIEWS_FILE)
