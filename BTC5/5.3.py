import sqlite3

# Tạo kết nối tới cơ sở dữ liệu SQLite (cơ sở dữ liệu mới sẽ được tạo ra nếu chưa tồn tại)
conn = sqlite3.connect('my_database.db')

# Tạo một con trỏ để thực thi các câu lệnh SQL
cursor = conn.cursor()

# Tạo bảng 'users' trong cơ sở dữ liệu
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# Commit thay đổi (lưu lại các thay đổi vào cơ sở dữ liệu)
conn.commit()

# In ra thông báo xác nhận tạo bảng thành công
print("Bảng 'users' đã được tạo thành công trong cơ sở dữ liệu.")

# Đóng kết nối với cơ sở dữ liệu
conn.close()
