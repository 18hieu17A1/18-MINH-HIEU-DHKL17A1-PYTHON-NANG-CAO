import sqlite3

def count_records(db_file, table_name):
    # Kết nối đến cơ sở dữ liệu SQLite
    conn = sqlite3.connect(db_file)
    
    # Tạo con trỏ để thực hiện truy vấn
    cursor = conn.cursor()

    # Thực hiện truy vấn đếm số bản ghi trong bảng
    cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
    
    # Lấy kết quả và in ra
    count = cursor.fetchone()[0]
    
    print(f"Số bản ghi trong bảng {table_name}: {count}")

    # Đóng kết nối
    conn.close()

# Gọi hàm và truyền vào tên tệp cơ sở dữ liệu và tên bảng
db_file = 'students.db'  # Thay đổi tên tệp cơ sở dữ liệu nếu cần
table_name = 'Students'  # Thay đổi tên bảng nếu cần
count_records(db_file, table_name)
