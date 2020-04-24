import sqlite3
import datetime
import os
import numpy

connection = sqlite3.connect('input_logs.db')
cursor = connection.cursor()


for row in cursor.execute('SELECT * FROM Clicks ORDER BY time'):
    print(row)

for row in cursor.execute('SELECT * FROM Moves ORDER BY time'):
    print(row)

print(cursor.execute('SELECT COUNT(*) FROM Clicks').fetchone()[0])
print(cursor.execute('SELECT COUNT(*) FROM Moves').fetchone()[0])


connection.commit()
connection.close()