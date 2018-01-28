import sqlite3
conn = sqlite3.connect('TheBats.db')

c = conn.cursor()

quotes = (
        'Perhaps the lady is just what the doctor ordered?',
        'The Bat-Signal is not a Beeper.',
        'Look Bruce, Im a part of this whether you like it not.'
)

batquote = ('I own a batcave, what have you got?')


c.execute('INSERT INTO batquote (message) VALUES(?)', (batquote,))
#cursor.execute('INSERT INTO images            VALUES(?)', (img,))

conn.commit()

conn.close()
