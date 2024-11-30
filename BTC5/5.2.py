import sqlite3

# Tạo kết nối tới cơ sở dữ liệu SQLite trong bộ nhớ
conn = sqlite3.connect(':memory:')

# Lấy thông tin về phiên bản SQLite
sqlite_version = sqlite3.version
print(f"SQLite version: {sqlite_version}")

# Tạo một bảng trong cơ sở dữ liệu
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Chèn dữ liệu vào bảng
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))

# Lấy và in ra tất cả dữ liệu trong bảng
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Dữ liệu trong bảng users:")
for row in rows:
    print(row)

# Đóng kết nối với cơ sở dữ liệu
conn.close()
