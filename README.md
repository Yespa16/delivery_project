# This repo contains a final project for SQL my learning course


## Requirements
1. You should have a PostgreSQL server running for connection. Please configure your database credentials in `db_config.json` file.
	* Note that "user" and "password" fields should match PostgreSQL container `POSTGRES_USER` and `POSTGRES_PASSWORD`.


## Run the project
The `Makefile` in root directory have targets for all scenarios.
1. Run `make` to start a FastAPI server.
2. Run `make fill_db` to start a script that inserts a massive data into database with REST API calls (insertion data is get from `src/scripts/` csv files).
3. Run `make query` to start a script that runs sequence of different queries via REST API calls. 