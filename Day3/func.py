import dbconn

def print_all():
    conn = dbconn.get_connection()

    query = f"select * from emp_info;"

    cursor = conn.cursor()

    cursor.execute(query)

    records = cursor.fetchall()
    for r in records:
        print(r)

    cursor.close()

    conn.close()


def print_depart():
    conn = dbconn.get_connection()
    department = input("Enter the department name to print those employees: ")

    query = f"select * from emp_info where department=%s"
    val = (department,)

    cursor = conn.cursor()

    cursor.execute(query,val)

    records = cursor.fetchall()
    for r in records:
        print(r)

    cursor.close()

    conn.close()

def emp_salary_highest():
    conn = dbconn.get_connection()

    query = f"select * from emp_info order by salary DESC LIMIT 1;"

    cursor = conn.cursor()

    cursor.execute(query)

    records = cursor.fetchall()
    print("Highest salary : ")
    print(records)

    cursor.close()
    conn.close()

def emp_salary_lowest():
    conn = dbconn.get_connection()

    query = f"select * from emp_info order by salary ASC LIMIT 1;"

    cursor = conn.cursor()

    cursor.execute(query)

    records = cursor.fetchall()
    print("Lowest salary : ")
    print(records)

    cursor.close()
    conn.close()

print_all()
print()
print_depart()
print()
emp_salary_highest()
print()
emp_salary_lowest()