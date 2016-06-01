import psycopg2
conn = psycopg2.connect(host = "localhost",port = "5432",user = "dbo",password = '123456',database = "hw04")
cur = conn.cursor()
cur.execute('''SELECT * from  hw_a  where sn not in(select sn from hw_b)''')
rows = cur.fetchall()

print(rows)
cur.close()
conn.commit()