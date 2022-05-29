import sqlite3

con = sqlite3.connect('attendproject.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE studentattendance (name text, time  text , date  text )''')
# Save (commit) the changes
con.commit()

print("done")