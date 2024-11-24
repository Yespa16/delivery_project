DEBUG ?= 1

SOURCES_FOLDER := src
CREATE_DB_FILE = $(SOURCES_FOLDER)/create_db.py


create_db:
	python3 $(CREATE_DB_FILE) ;