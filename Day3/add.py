import dbconn

def add():
    conn = dbconn.get_connection()

    empid = int(input("Enter the employee id : "))
    name = input("Enetr the name : ")
    department = input("Enter the department : ")
    email = input("Enter the email : ")
    salary = float(input("Enter the salary : "))
    dob = input("Enter the date of joining : ")

    query = f"insert into emp_info value({empid},'{name}','{department}','{email}',{salary},'{dob}');"

    cursor = conn.cursor()

    cursor.execute(query)

    conn.commit()

    cursor.close()

    conn.close()

add()