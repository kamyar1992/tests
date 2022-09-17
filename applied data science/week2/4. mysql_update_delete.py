import mysql.connector
import sys
import mysql.connector.errorcode
config = {'user': 'kamyar',
          'password': 'Kmz19921371@',
          'host': '192.168.43.128'}

try:
    cn = mysql.connector.connect(**config)
    cursor = cn.cursor()
    cursor.execute('USE db2')
except mysql.connector.Error as err:
    if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print('DB does not exist')
        print(err)
        sys.exit(-1)
    else:
        print('unknown error')
        print(err)
else:
    print('db2 is chosen')

update_query = 'UPDATE salaries ' \
               'SET salary=%s ' \
               'WHERE salaries.emp_no=(SELECT emp_no FROM employees WHERE first_name=%s)'

update_data = (100_000_000,
               'dana')


cursor.execute(update_query,update_data)
delete_query = 'DELETE e, s FROM ' \
               'employees as e ' \
               'INNER JOIN salaries as s ' \
               'ON e.emp_no=s.emp_no ' \
               'WHERE first_name= %s'

cursor.execute(delete_query, ('kamyar',))
cn.commit()
cursor.close()
cn.close()






