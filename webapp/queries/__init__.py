import psycopg
import socket

# Determine whether connecting from on/off campus
try:
    socket.gethostbyname("data.cs.jmu.edu")
    DSN = "host=data.cs.jmu.edu user=dr dbname=dr"
except socket.gaierror:
    DSN = "host=localhost user=dr dbname=dr"


def db_connect():
    """Connect to the database server."""
    return psycopg.connect(DSN)