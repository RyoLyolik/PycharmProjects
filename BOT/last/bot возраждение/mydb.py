import sqlite3

conn = sqlite3.connect('mydatabase.sqlite')
cursor = conn.cursor()
# c.execute('''CREATE TABLE users (id int auto_increment primary key,name varchar, money varchar)''')
# c.execute("INSERT INTO users (name,money) VALUES ('admin','99999')")
cursor.execute("insert into users values (Null, 'A Aagrh!', '2') ")

# Если мы не просто читаем, но и вносим изменения в базу данных - необходимо сохранить транзакцию
conn.commit()

# Проверяем результат
cursor.execute("SELECT Name FROM users ORDER BY Name LIMIT 3")
results = cursor.fetchall()
print(results)  # [('A Aagrh!',), ('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',)]
conn.commit()
cursor.close()
conn.close()
# print(c)