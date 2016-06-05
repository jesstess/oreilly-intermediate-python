import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute("SELECT text, answer, value FROM clue LIMIT 10")
results = cursor.fetchall()

# TODO: process results

connection.close()
