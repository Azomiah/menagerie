import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='Azomiah@YUNY85', database='menagerie')
c = conn.cursor()

def show():
    c.execute('SHOW DATABASES')
    databases = c.fetchall()
    for db in databases:
        print(db)
def drop_if_exist():
    c.execute("DROP DATABASE IF EXISTS menagerie")
    c.close()
    conn.close()

def show_pet():
    c.execute("DESCRIBE pet;")
    for row in c.fetchall():
        print(row)


def show_pet_data():
    c.execute("SELECT * FROM pet;")
    for row in c.fetchall():
        print(row)

def female_dogs():
    c.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f';")
    for row in c.fetchall():
        print(row)

def name_bDate():
    c.execute("SELECT name, birth FROM pet;")
    for row in c.fetchall():
        print(row)

def num_pets():
    c.execute("SELECT owner, COUNT(*) as num_pets FROM pet GROUP BY owner ;")
    for row in c.fetchall():
        print(row)


def final_display():
    c.execute(""" SELECT name, birth, MONTH(birth) FROM pet; """)
    rows = c.fetchall()
    print(f"{'name':<10}{'birth':<15}{'MONTH(birth)'}")
    for i in rows:
        birth_date = i[1].strftime('%Y-%m-%d') if i[1] else "NULL"
        print(f"{i[0]:<10}{birth_date:<15}{i[2]}")
if __name__ =='__main__':
    final_display()