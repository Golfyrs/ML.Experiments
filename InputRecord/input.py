from pynput.mouse import Listener
import logging
import time
import sqlite3
import datetime
import threading


def on_move(x, y):
    moves.append((datetime.datetime.now(), x, y))


def on_click(x, y, button, pressed):
    clicks.append((datetime.datetime.now(),x, y, str(button), pressed))


def refresh():
    print("refresh")
    connection = sqlite3.connect('input_logs.db')
    cursor = connection.cursor()

    if len(clicks) > 0:
        cursor.executemany('INSERT INTO Clicks VALUES(?,?,?,?,?)', clicks)
        clicks.clear()

    if len(moves) > 0:
        cursor.executemany('INSERT INTO Moves VALUES(?,?,?)', moves)
        moves.clear()

    connection.commit()
    threading.Timer(1.0, refresh).start()
    

moves = []
clicks = []

with Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()

# Save data to database every 5 seconds.
threading.Timer(5.0, refresh).start()