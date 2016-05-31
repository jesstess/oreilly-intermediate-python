# Goal:
# Select a random game and print all of the categories from that game.

# SQL to get a random game:
# SELECT game FROM category ORDER BY RANDOM() LIMIT 1

# SQL to get the categories for a particular game:
# """SELECT name, round FROM category
#    WHERE game=%d ORDER BY round""" % (game_id,)

import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

# Get a random game.
cursor.execute("SELECT game FROM category ORDER BY RANDOM() LIMIT 1")
results = cursor.fetchall()
game_id = results[0][0]
print("Categories for game #%d:" % (game_id,))

# Get the categories for that game.
query = """SELECT name, round FROM category
WHERE game=%d ORDER BY round""" % (game_id,)
cursor.execute(query)
results = cursor.fetchall()

# TODO: process results.

connection.close()
