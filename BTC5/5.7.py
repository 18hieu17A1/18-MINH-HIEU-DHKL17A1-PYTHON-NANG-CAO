import sqlite3

def update_column(db_file, table_name, column_name, new_value):
    # Kết nối đến cơ sở dữ liệu SQLite
    conn = sqlite3.connect(db_file)
    
    # Tạo con trỏ để thực hiện truy vấn
    cursor = conn.cursor()

    # Thực hiện truy vấn cập nhật giá trị cột
    sql_update_query = f"UPDATE {table_name} SET {column_name} = ?"
    cursor.execute(sql_update_query, (new_value,))

    # Lưu thay đổi vào cơ sở dữ liệu
    conn.commit()

    # Kiểm tra số lượng bản ghi bị thay đổi
    rows_updated = cursor.rowcount
    print(f"Số bản ghi đã được cập nhật: {rows_updated}")

    # Đóng kết nối
    conn.close()

# Gọi hàm và truyền vào tên tệp cơ sở dữ liệu, tên bảng, tên cột, và giá trị mới
db_file = 'students.db'  # Tên tệp cơ sở dữ liệu SQLite
table_name = 'Students'  # Tên bảng
column_name = 'age'      # Tên cột cần cập nhật
new_value = 25           # Giá trị mới bạn muốn cập nhật cho cột 'age'

update_column(db_file, table_name, column_name, new_value)
