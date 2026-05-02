import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("""
    UPDATE estudantes SET nome = ? WHERE nome =?
""",('Lorenzo','JOANA'))

conn.commit()
conn.close()