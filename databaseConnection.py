import sqlite3

def create_table():
    conn=sqlite3.connect('employee.db')
    cursor=conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS employeeData(
                     id INT PRIMARY KEY,
                     name TEXT,
                     des TEXT,
                     gender TEXT,
                     status TEXT)
            ''')
    conn.commit()
    conn.close()

def fetch_data():
     conn=sqlite3.connect('employee.db')
     cursor=conn.cursor()
     cursor.execute('SELECT * FROM employeeData')
     emp=cursor.fetchall()
     conn.close()
     return emp
    #insering data

def insert_data(id,name,des,gender,status):
     conn=sqlite3.connect('employee.db')
     cursor=conn.cursor()
     cursor.execute('INSERT INTO employeeData (id ,name ,des ,gender ,status) VALUES (?,?,?,?,?)',(id,name,des,gender,status))
     conn.commit()
     conn.close()
    
def delete_data(id):
     conn=sqlite3.connect('employee.db')
     cursor=conn.cursor()
     cursor.execute('DELETE FROM employeeData WHERE id =?',(id,))
     conn.commit()
     conn.close()

def update_data(new_name,new_des,new_gender,new_status,id):
     conn=sqlite3.connect('employee.db')
     cursor=conn.cursor()
     cursor.execute("UPDATE employeeData SET name=?,des=?,gender=?,status=? WHERE id=?",(new_name,new_des,new_gender,new_status,id))
     conn.commit()
     conn.close()
#to check id
def id_exists(id):
     conn=sqlite3.connect('employee.db')
     cursor=conn.cursor()
     cursor.execute('SELECT COUNT(*) FROM employeeData WHERE id=?',(id,)) 
     res=cursor.fetchone()
     conn.close()
     return res[0] > 0  

create_table()
     
     




