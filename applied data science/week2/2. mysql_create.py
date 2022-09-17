import sys
import mysql.connector
from mysql.connector import errorcode


def create_db(cur, db_name):
    try:
        cur.execute('CREATE DATABASE {}'.format(db_name))

    except mysql.connector.Error as err:
        print('could not create database')
        print(err)
        sys.exit(-1)


DB_NAME = 'db2'

TABLES = dict()
TABLES['employees'] = (
    "CREATE TABLE employees ("
    " emp_no INT(11) NOT NULL AUTO_INCREMENT,"
    " birth_date DATE NOT NULL,"
    " first_name VARCHAR(14) NOT NULL,"
    " last_name VARCHAR(14) NOT NULL,"
    " gender ENUM('M', 'F') NOT NULL,"
    " hire_date DATE NOT NULL,"
    " PRIMARY KEY (emp_no)"
    " ) ENGINE=InnoDB"
)

TABLES['salaries'] = (
    "CREATE TABLE salaries("
    "emp_no INT(11) NOT NULL,"
    "salary INT(11) NOT NULL,"
    "from_date DATE NOT NULL,"
    "to_date DATE NOT NULL,"
    "PRIMARY KEY (emp_no, from_date), KEY emp_no (emp_no),"
    "CONSTRAINT salaries_ibfk_1 FOREIGN KEY (emp_no) "
    "   REFERENCES employees (emp_no) ON DELETE CASCADE"
    ") ENGINE = InnoDB"
)

TABLES['dept_manager'] = ("CREATE TABLE dept_manager ( "
                          " dept_no VARCHAR(4) NOT NULL,"
                          " emp_no INT(11) NOT NULL,"
                          " from_date date NOT NULL,"
                          " to_date DATE NOT NULL"
                          ") ENGINE=InnoDB;")

config = {"user": 'kamyar',
          'password': 'Kmz19921371@',
          'host': '192.168.43.128',
          # 'database': 'db2',
          'raise_on_warnings': True}

try:
    cn = mysql.connector.connect(**config)
    cursor = cn.cursor()

except mysql.connector.Error as err:
    print(err)

try:
    cursor.execute('USE {}'.format(DB_NAME))
except mysql.connector.Error as error_1:
    if error_1.errno == errorcode.ER_BAD_DB_ERROR:  # *important pppppaaaaayyyyyyy attention to erno!!!!!!!!!!
        create_db(cursor, DB_NAME)
        print('Create database {}'.format(DB_NAME))
    else:
        print('unknown error occurred')
        print(error_1)
        sys.exit(-1)
else:
    print('database change to {}'.format(DB_NAME))

for item in TABLES:
    query_text = TABLES[item]
    try:
        cursor.execute(query_text)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print(f'{item} already exists')
        else:
            print(err)
            sys.exit(-1)
    else:
        print(f'table {item} successfully created')

# cursor.execute("CREATE TABLE employee()")
