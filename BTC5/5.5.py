import sqlite3

def create_and_insert(db_file):
    # Kết nối đến cơ sở dữ liệu SQLite (nếu tệp không tồn tại, nó sẽ được tạo mới)
    conn = sqlite3.connect(db_file)
    
    # Tạo con trỏ để thực hiện truy vấn
    cursor = conn.cursor()

    # Tạo bảng mới
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    );
    ''')

    # Chèn một số bản ghi vào bảng
    cursor.execute("INSERT INTO Students (name, age) VALUES ('John Doe', 22);")
    cursor.execute("INSERT INTO Students (name, age) VALUES ('Jane Smith', 24);")
    cursor.execute("INSERT INTO Students (name, age) VALUES ('Alice Johnson', 21);")

    # Lưu các thay đổi
    conn.commit()

    # Chọn tất cả các bản ghi từ bảng và hiển thị chúng
    cursor.execute("SELECT * FROM Students;")
    rows = cursor.fetchall()
    
    # Hiển thị các bản ghi
    print("Danh sách sinh viên trong bảng:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

    # Đóng kết nối
    conn.close()

# Gọi hàm và truyền vào tên tệp cơ sở dữ liệu SQLite
db_file = 'students.db'  # Thay đổi tên tệp nếu cần
create_and_insert(db_file)
