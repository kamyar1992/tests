import sqlite3
import datetime
print(datetime.date.today())
db = sqlite3.connect('employee')

employee_query = db.execute('SELECT * FROM people')
print(employee_query)  # it returns a cursor object

for item in employee_query:  # important: every item is a tuple
    print(item)

id_query = db.execute('SELECT id, name FROM people')
for item in id_query:
    print(item)

print('=' * 30)
salary_query = db.execute('SELECT * FROM salary')
for item in salary_query:
    print(item)







