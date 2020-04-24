import sqlite3
import os

# Initialization of database with common tables.

os.remove("input_logs.db")
connection = sqlite3.connect('input_logs.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE Clicks (Time timestamp, X INTEGER, Y INTEGER, Button TEXT, Pressed INTEGER)")
cursor.execute("CREATE TABLE Moves (Time timestamp, X INTEGER, Y INTEGER)")

connection.commit()
connection.close()
