import sqlite3
db = sqlite3.connect('chinook.db')
cursor = db.cursor()

for item in cursor.execute('SELECT id FROM albums'):
    print(item)





