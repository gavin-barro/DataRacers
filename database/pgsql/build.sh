# This script rebuilds the entire database.
#
# Create a pgpass file in your home directory for storing the password.
# See https://www.postgresql.org/docs/16/libpq-pgpass.html for details.

export CMD='psql -q -h localhost -U dr dr'

echo Dropping tables...
$CMD < drop.sql

echo Creating tables...
$CMD < create.sql

echo Adding comments...
$CMD < comments.sql

echo Loading data...
$CMD < load.sql

echo Generating data...
python create_shipment.py
python generate.py
#python kitstuff.py

echo Adding constraints...
$CMD < alter.sql

echo Creating views...
$CMD < views.sql
