import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    database ="" ,
    user = "",
    passworl = "",
    host = "ec2-52-87-161-189.compute-1.amazonaws.com",
    port = ""
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM meubanco")

# Retrieve query results
records = cur.fetchall()