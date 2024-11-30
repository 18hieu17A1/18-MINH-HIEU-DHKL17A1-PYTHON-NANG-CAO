import sqlite3

def list_tables(db_file):
    # Kết nối đến cơ sở dữ liệu SQLite
    conn = sqlite3.connect(db_file)
    
    # Tạo con trỏ để thực hiện truy vấn
    cursor = conn.cursor()
    
    # Thực hiện truy vấn để lấy danh sách các bảng
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    
    # Lấy tất cả các bảng từ kết quả truy vấn
    tables = cursor.fetchall()
    
    # Đóng kết nối
    conn.close()
    
    # In ra danh sách các bảng
    if tables:
        print("Các bảng trong cơ sở dữ liệu:")
        for table in tables:
            print(table[0])  # In tên của từng bảng
    else:
        print("Không có bảng nào trong cơ sở dữ liệu.")

# Gọi hàm và truyền vào đường dẫn đến tệp cơ sở dữ liệu SQLite
db_file = 'duong_dan_toi_file.sqlite'  # Thay thế bằng đường dẫn đúng đến tệp SQLite của bạn
list_tables(db_file)
