import psycopg2
conn = psycopg2.connect(host = "localhost",port = "5432",user = "dbo",password = '123456',database = "hw04")
cur = conn.cursor()
cur.execute('''
DROP TABLE IF EXISTS hw_a;
CREATE TABLE IF NOT EXISTS hw_a(
    sn    INTEGER,
    name  VARCHAR,
    PRIMARY KEY(sn)
);
''')
cur.execute('INSERT INTO hw_a(sn,name) VALUES(%s,%s)',(10,'A10'))
cur.execute('INSERT INTO hw_a(sn,name) VALUES(%s,%s)',(20,'A20'))
cur.execute('INSERT INTO hw_a(sn,name) VALUES(%s,%s)',(30,'A30'))
cur.execute('INSERT INTO hw_a(sn,name) VALUES(%s,%s)',(40,'A40'))
cur.execute('INSERT INTO hw_a(sn,name) VALUES(%s,%s)',(50,'A50'))
cur.execute('INSERT INTO hw_a(sn,name) VALUES(%s,%s)',(60,'A60'))

ass = conn.cursor()
ass.execute('''
DROP TABLE IF EXISTS hw_b;
CREATE TABLE IF NOT EXISTS hw_b(
    sn    INTEGER,
    name  VARCHAR,
    PRIMARY KEY(sn)
);
''')
cur.execute('INSERT INTO hw_b(sn,name) VALUES(%s,%s)',(40,'B40'))
cur.execute('INSERT INTO hw_b(sn,name) VALUES(%s,%s)',(50,'B50'))
cur.execute('INSERT INTO hw_b(sn,name) VALUES(%s,%s)',(60,'B60'))
cur.execute('INSERT INTO hw_b(sn,name) VALUES(%s,%s)',(70,'B70'))
cur.execute('INSERT INTO hw_b(sn,name) VALUES(%s,%s)',(80,'B80'))

conn.commit()
