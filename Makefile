DEBUG ?= 1

SOURCES_FOLDER := ./src

.DEFAULT_GOAL := run_api


run_api:
	@fastapi dev $(SOURCES_FOLDER)/api/views.py


fill_db:
	python3 $(SOURCES_FOLDER)/scripts/fill_db.py $(SOURCES_FOLDER)/scripts/

query:
	python3 $(SOURCES_FOLDER)/scripts/query.py