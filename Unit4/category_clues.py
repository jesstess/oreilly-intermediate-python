import sqlite3

connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

cursor.execute("SELECT id, name FROM category ORDER BY RANDOM() LIMIT 1")
results = cursor.fetchall()
category_id, name = results[0]
print(name)


query = """SELECT text, answer, value FROM clue
WHERE category=%s ORDER BY value""" % (category_id,)
cursor.execute(query)
results = cursor.fetchall()

for clue in results:
    text, answer, value = clue
    print("[$%s]" % (value,))
    print("A: %s" % (text,))
    print("Q: What is '%s'" % (answer,))
    print("")

connection.close()
