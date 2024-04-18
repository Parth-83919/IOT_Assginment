import dbconn

def update(salary,empid):
    conn = dbconn.get_connection()

    query = f"update emp_info SET salary=%s where empid=%s;"
    val=(salary,empid)

    cursor = conn.cursor()

    cursor.execute(query,val)

    conn.commit()

    cursor.close()

    conn.close()

empid = int(input("Enter the empid : "))
salary = float(input("Enter the salary : "))

update(salary,empid)

