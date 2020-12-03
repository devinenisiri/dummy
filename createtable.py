import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real, category text, uesd_for real)"
cursor.execute(create_table)

connection.commit()

connection.close()
