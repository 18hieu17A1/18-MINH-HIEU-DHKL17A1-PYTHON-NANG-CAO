import sqlite3

# Tạo kết nối đến cơ sở dữ liệu SQLite (tạo cơ sở dữ liệu mới nếu chưa tồn tại)
conn = sqlite3.connect('my_database.db')

# Lấy thông tin về phiên bản SQLite
sqlite_version = sqlite3.version

# In ra phiên bản SQLite
print(f"SQLite version: {sqlite_version}")

# Đóng kết nối với cơ sở dữ liệu
conn.close()
