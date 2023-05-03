import duckdb

# Connect to a database file
con = duckdb.connect('mydatabase.db')

# Creating a table
con.execute("CREATE TABLE mytable (id INTEGER PRIMARY KEY, name VARCHAR(50), age INTEGER)")

# Inserting data into the table
con.execute("INSERT INTO mytable (id, name, age) VALUES (1, 'Lea', 21)")
con.execute("INSERT INTO mytable (id, name, age) VALUES (2, 'Kevin', 22)")
con.execute("INSERT INTO mytable (id, name, age) VALUES (3, 'Hung', 31)")

# Printing our data
result = con.execute("SELECT * FROM mytable")
for row in result.fetchall():
    print(row)