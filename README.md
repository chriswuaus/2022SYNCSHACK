# 2022SYNCSHACK
shack

## Database setup
cd database
docker-compose up

docker exec -it database_psotgres_1 /bin/bash
psql postgres postgres -f /scripts/make_tables.sql
exit

## Flash Setup
pip install flask
sudo apt install libpq-devel python-devel (for linux)
sudo yum install libpq-devel python-devel (for linux)
sudo dnf install libpq-devel python-devel (for linux)
brew install postgresql (for mac users)
pip install psycopg2

