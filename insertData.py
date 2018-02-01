import sqlite3
conn = sqlite3.connect('TheBats.db')

c = conn.cursor()

batquote = 'The Bat-Signal is not a Beeper.'

c.execute('INSERT INTO batquote (message) VALUES (?)', (batquote,))

conn.commit()

conn.close()
