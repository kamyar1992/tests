import sqlite3
import datetime
print(datetime.date.today())
db = sqlite3.connect('employee')
cursor = db.cursor()

for i in cursor.execute('SELECT * FROM salary'):
    print(i)

print('=' * 50)
salary_query = cursor.execute('SELECT * FROM salary')

for item in salary_query:
    print(item)

print('=' * 50)

for item in salary_query:  # *important this for print nothing because cursor is a generator and, it does not rest
    print(item)
print('second for print nothing')
print('=' * 50)

salary_query = cursor.execute('SELECT * FROM salary')
print(salary_query.fetchone())
print(salary_query.fetchone())
print(salary_query.fetchone())
print(salary_query.fetchone())  # be careful when run code each time salary_query vale is defined again
print('=' * 50)
salary_query = cursor.execute('SELECT * FROM salary')
print(cursor.rowcount)
print(salary_query.fetchall())  # it returns a list
print(salary_query.fetchall())  # it does not return anything
print('=' * 50)

cursor.execute('UPDATE salary SET amount=? WHERE id=?', (13000000, 1002))
print(cursor.rowcount)





