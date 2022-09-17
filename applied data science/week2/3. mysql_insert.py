import mysql.connector
import sys
import mysql.connector.errorcode
import datetime


config = {"user": "kamyar",
          "password": "Kmz19921371@",
          "host": "192.168.43.128",
          "database": "db2",
          "raise_on_warnings": True}

try:
    cn = mysql.connector.connect(**config)
    cursor = cn.cursor()
except mysql.connector.Error as err:
    if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print('db does not exist')
    else:
        print('unknown error')
        print(err)
        sys.exit(-1)
else:
    print(f"you are connected to {config['database']} ")
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
employee_query = "INSERT INTO employees(birth_date, first_name, last_name, gender, hire_date)" \
                 "VALUES(%s, %s, %s, %s, %s)"

salary_query = "INSERT INTO salaries(emp_no, salary, from_date, to_date)" \
               "VALUES(%s, %s, %s, %s)"  # %s means string
tomorrow = datetime.datetime.now().date() + datetime.timedelta(days=1)   # datetime.datetime.now().date(): just return
# data, not hours and minutes
employee_data = (datetime.date(1992, 5, 30),
                 'kamyar',
                 'mazaher fard',
                 'M',
                 tomorrow
                 )

cursor.execute(employee_query, employee_data)
emp_no = cursor.lastrowid

salary_data = (emp_no,
               25_000_000,
               tomorrow,
               datetime.date(2022, 12, 30))

cursor.execute(salary_query, salary_data)
cn.commit()  # cn has .commit() not cursor
cursor.close()
cn.close()






















