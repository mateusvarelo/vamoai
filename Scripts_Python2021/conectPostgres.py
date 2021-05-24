import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    database ="grupo2" ,
    user = "grupo2",
    password = "albaniatangerinajoaninha",
    host = "ec2-52-87-161-189.compute-1.amazonaws.com",
    port = "5432"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM Steam  limit 1")

# Retrieve query results
records = cur.fetchall()
for i in records:
    print(reco)

