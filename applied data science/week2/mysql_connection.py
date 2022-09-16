# my sql users:
# demouser P@ssw0rd
# kamyar Kmz19921371@

# databases :
# demodb
# dayche
# remember to grant user access
import mysql.connector
from mysql.connector import connection
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
          'password': 'Kmz19921371@',
          'host': '192.168.43.128',
          'database': 'dayche',
          'raise_on_warnings': True}
cn = connection.MySQLConnection(**config)  # *important remember ** before parameter
cn.close()




















































