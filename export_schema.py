import duckdb

conn = duckdb.connect("C:\\Users\\Ben Sylve\\Documents\\git_sf\\sf-pipeline\\db\\race_analytics.duckdb", read_only=True)

schema = conn.execute("SELECT sql FROM duckdb_tables()").fetchall()

with open('schema.sql', 'w') as f:
    for row in schema:
        f.write(row[0] + ';\n\n')

print("Done")