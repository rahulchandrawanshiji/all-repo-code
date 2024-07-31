export PGUSER="postgres"
psql -c "create database inventory"

psql -c "create extension if not exists \"uuid-ossp"\"