import mysql.connector as mysql
def create_db():
    con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
    Eid INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255),
    Gender VARCHAR(10),
    Contact VARCHAR(15),
    DOB VARCHAR(15),
    DOJ VARCHAR(15),
    Pass VARCHAR(255),
    usertype VARCHAR(20),
    Address VARCHAR(255),
    Salary DECIMAL(10, 2)
    ) """)

    con.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Supplier (
        Invoice  INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255),
        Contact VARCHAR(15),
        Description TEXT
    
        ) """)

    con.commit()

    cur.execute(""" 
        CREATE TABLE IF NOT EXISTS Category (
        Cid INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255)
       ) """)
    con.commit()

    cur.execute(""" 
            CREATE TABLE IF NOT EXISTS Product (
            pid INT AUTO_INCREMENT PRIMARY KEY,
            Supplier VARCHAR(255),
            Category VARCHAR(255),
            Name VARCHAR(255),
            price VARCHAR(255),
            qty VARCHAR(255),
            status VARCHAR(255)
           ) """)
    con.commit()


create_db()