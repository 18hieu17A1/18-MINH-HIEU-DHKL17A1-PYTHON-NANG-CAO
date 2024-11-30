import sqlite3

def delete_record(db_file, table_name, column_name, value):
    # Kết nối đến cơ sở dữ liệu SQLite
    conn = sqlite3.connect(db_file)
    
    # Tạo con trỏ để thực hiện truy vấn
    cursor = conn.cursor()

    # Thực hiện câu lệnh xóa bản ghi dựa trên điều kiện
    sql_delete_query = f"DELETE FROM {table_name} WHERE {column_name} = ?"
    cursor.execute(sql_delete_query, (value,))

    # Lưu thay đổi vào cơ sở dữ liệu
    conn.commit()

    # Kiểm tra số lượng bản ghi bị xóa
    rows_deleted = cursor.rowcount
    print(f"Số bản ghi đã bị xóa: {rows_deleted}")

    # Đóng kết nối
    conn.close()

# Gọi hàm và truyền vào tên tệp cơ sở dữ liệu, tên bảng, tên cột và giá trị để xóa
db_file = 'students.db'   # Tên tệp cơ sở dữ liệu SQLite
table_name = 'Students'   # Tên bảng
column_name = 'id'        # Tên cột (ở đây giả sử là cột 'id')
value = 2                 # Giá trị bạn muốn xóa (ví dụ: xóa bản ghi có id = 2)

delete_record(db_file, table_name, column_name, value)
