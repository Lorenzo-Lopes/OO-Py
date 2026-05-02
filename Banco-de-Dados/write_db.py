import sqlite3

conn =sqlite3.connect('escola.db')

cursor = conn.cursor()

# cursor.execute("""
#     INSERT INTO estudantes(nome,idade) VALUES (?,?)
# """,("JOANA",19)
# )

cursor.execute("""
    insert into disciplinas (estudante_id, nome_disciplina) values (?,?)
""",(1, 'Matematica')
)

conn.commit()
conn.close()