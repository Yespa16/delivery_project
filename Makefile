DEBUG ?= 1

SOURCES_FOLDER := src
CONNECT_DB_FILE = $(SOURCES_FOLDER)/api/connect_db.py
VIEWS_FILE 		 = $(SOURCES_FOLDER)/api/views.py


.DEFAULT_GOAL := run_api


connect_db:
	python3 $(CONNECT_DB_FILE) ;

run_api:
	fastapi dev $(VIEWS_FILE)
