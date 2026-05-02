import sqlite3

conn = sqlite3.connect("escola.db")

cursor = conn.cursor()

cursor.execute("""
    select * from estudantes
""")

conn.commit()
estudantes = cursor.fetchall()


print(estudantes)
conn.close()