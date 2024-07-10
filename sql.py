import sqlite3

# ESTABLISH A CONNECTION
connection = sqlite3.connect("data.db")
cursor = connection.cursor()


# QUERY DATA
cursor.execute("SELECT * FROM events")
SELECT_ALL = cursor.fetchall()

cursor.execute("SELECT band FROM events")
q_all_bands = cursor.fetchall()

cursor.execute("SELECT band, date FROM events WHERE date < '2024.10.31'")
q_date_before_nov = cursor.fetchall()


# INSERT NEW ROW (2 ways, using variable or direct)
new_row = ('Gorillaz', 'Melbourne', '2025.03.28')
cursor.execute("INSERT INTO EVENTS VALUES(?,?,?)", new_row)
connection.commit()

cursor.execute("INSERT INTO EVENTS VALUES('High n Low','Berlin','2025.02,16')")
connection.commit()


# INSERTING MULTIPLE ROWS
new_rows = [('The Killers', 'Paris', '2024.12.12'),
            ('The Carpenters', 'Milan', '2025.01.12'),
            ('Parody', 'London', '2024.08.17')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()
