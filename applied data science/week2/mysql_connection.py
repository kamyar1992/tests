# my sql users:
# demouser P@ssw0rd
# kamyar Kmz19921371@

# databases :
# demodb
# dayche
# remember to grant user access
import mysql.connector
from mysql.connector import connection
from mysql.connector import errorcode
# cn = mysql.connector.connect(user='admin',
#                              password='P@ssw0rd',
#                              host='192.168.43.128',
#                              database='db2',
#                              )

# cn = connection.MySQLConnection(user='kamyar',
#                                 password='Kmz19921371@',
#                                 host='192.168.43.128',
#                                 database='dayche')

config = {"user": 'kamyar',
          'password': 'mz19921371@',
          'host': '192.168.43.128',
          'database': 'db2',
          'raise_on_warnings': True}
# cn = connection.MySQLConnection(**config)  # *important remember ** before parameter
# cn.close()

try:
    cn = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:   # *important : pay attention to err.errno
        print('access is denied')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('database does not exist')
    elif err.errno == errorcode.ER_USERNAME:
        print('username or password in incorrect')
    else:
        print(err)
else:
    cn.close()



















































