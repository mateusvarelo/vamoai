import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=grupo2 user=grupo2")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM meubanco")

# Retrieve query results
records = cur.fetchall()