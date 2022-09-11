import sqlite3
import datetime

db = sqlite3.connect('employee')
cursor = db.cursor()
create_query = 'CREATE TABLE IF NOT EXISTS people(' \
               'id INTEGER PRIMARY KEY,' \
               'name TEXT NOT NULL,' \
               'phone TEXT,' \
               'department DEFAULT UNKNOWN)'

db.execute(create_query)

create_q2 = 'CREATE TABLE IF NOT EXISTS salary(' \
           'id INTEGER,' \
           'amount INTEGER NOT NULL,' \
           'date TIMESTAMP)'
db.execute(create_q2)

# db.execute('INSERT INTO people(id, name, phone, department)'
#            'VALUES(1001, "Kamyar Mazaheri Fard", "091212345678910", "IT");')


# db.execute('INSERT INTO people'
           # ' VALUES(1002, "Saba Mazaheri Fard", "091212345678910", "Graphic")')

today = datetime.date.today()
# db.execute('INSERT INTO salary'
#            f' VALUES(1001, 15000, {today})')
# db.execute('INSERT INTO salary'
#            f' VALUES(1002, 16000, {today})')
# db.execute('INSERT INTO salary'
#            f' VALUES(1003, 17000, {today})')

# db.execute('DELETE FROM salary WHERE id=1001')
# db.execute('DELETE FROM salary WHERE id=1002')
# db.execute('DELETE FROM salary WHERE id=1003')

# db.execute('INSERT INTO salary'
#            f' VALUES(1001, 15000, {str(today)})')
# db.execute('INSERT INTO salary'
#            f' VALUES(1002, 16000, {str(today)})')
# db.execute('INSERT INTO salary'
#            f' VALUES(1003, 17000, {str(today)})')

# db.execute('UPDATE salary SET amount=2500000 WHERE id=1002')


# *important : .executescript() may cause SQL injection that leads to serious problems for example if the user enter:
# ;drop table salary
# because .executescript() execute more than one query!!!!!
# salary_id = input('please enter your id: ')
# cursor.executescript(f'UPDATE salary SET amount=100000000 WHERE id = {salary_id}')

# replacement field:
# when your program get data from user instead of using string formatting (.format()) use replacement field:
# replacement field is used in query with ? for SQLite:
salary_id = input('please enter user id: ')
amount_salary = 100000000
db.execute('UPDATE salary SET amount=? WHERE id=?', (amount_salary, salary_id))
db.commit()
db.close()
























































