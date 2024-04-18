import dbconn

def delete(empid):
    conn = dbconn.get_connection()

    query = f"delete from emp_info where empid=%s;"
    val = (empid,)

    cursor = conn.cursor()
    cursor.execute(query,val)

    conn.commit()

    cursor.close()

    conn.close()

empid = int(input("Enter the empid : "))

delete(empid)