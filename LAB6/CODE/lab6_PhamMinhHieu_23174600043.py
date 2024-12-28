import tkinter as tk
from tkinter import messagebox
import sqlite3

# Kết nối cơ sở dữ liệu SQLite
def connect_db():
    conn = sqlite3.connect('products.db')  # Tạo file products.db nếu chưa có
    cursor = conn.cursor()
    return conn, cursor

# Tạo bảng sản phẩm nếu chưa có
def create_table():
    conn, cursor = connect_db()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Hàm thêm sản phẩm vào cơ sở dữ liệu
def add_product_to_db(product_name):
    conn, cursor = connect_db()
    cursor.execute('INSERT INTO products (name) VALUES (?)', (product_name,))
    conn.commit()
    conn.close()

# Hàm lấy tất cả sản phẩm từ cơ sở dữ liệu
def get_all_products():
    conn, cursor = connect_db()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products

# Hàm xóa sản phẩm theo ID
def delete_product_from_db(product_id):
    conn, cursor = connect_db()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()

# Hàm cập nhật tên sản phẩm theo ID
def update_product_name(product_id, new_name):
    conn, cursor = connect_db()
    cursor.execute('UPDATE products SET name = ? WHERE id = ?', (new_name, product_id))
    conn.commit()
    conn.close()

# Hàm xử lý sự kiện khi bấm nút thêm sản phẩm
def add_product():
    product_name = entry.get()
    if product_name:
        add_product_to_db(product_name)
        update_product_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a product name.")

# Hàm xử lý sự kiện khi bấm nút xóa sản phẩm
def delete_product():
    try:
        selected_product_index = listbox.curselection()
        if selected_product_index:
            product_id = listbox.get(selected_product_index[0]).split(" - ")[0]  # Lấy ID sản phẩm từ Listbox
            delete_product_from_db(product_id)
            update_product_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a product to delete.")
    except Exception as e:
        messagebox.showerror("Error", f"Error while deleting product: {e}")

# Hàm xử lý sự kiện khi bấm nút sửa tên sản phẩm
def update_product():
    try:
        selected_product_index = listbox.curselection()
        if selected_product_index:
            product_id = listbox.get(selected_product_index[0]).split(" - ")[0]
            new_name = entry.get()
            if new_name:
                update_product_name(product_id, new_name)
                update_product_listbox()
                entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a new product name.")
        else:
            messagebox.showwarning("Selection Error", "Please select a product to update.")
    except Exception as e:
        messagebox.showerror("Error", f"Error while updating product: {e}")

# Cập nhật danh sách sản phẩm trong Listbox
def update_product_listbox():
    listbox.delete(0, tk.END)
    products = get_all_products()
    for product in products:
        listbox.insert(tk.END, f"{product[0]} - {product[1]}")  # Hiển thị ID và tên sản phẩm

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản Lý Sản Phẩm")

# Tạo Label
label = tk.Label(root, text="Nhập tên sản phẩm:")
label.pack(pady=10)

# Tạo Entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Tạo nút thêm sản phẩm
add_button = tk.Button(root, text="Thêm Sản Phẩm", command=add_product)
add_button.pack(pady=5)

# Tạo Listbox để hiển thị danh sách sản phẩm
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Tạo nút xóa sản phẩm
delete_button = tk.Button(root, text="Xóa Sản Phẩm", command=delete_product)
delete_button.pack(pady=5)

# Tạo nút sửa tên sản phẩm
update_button = tk.Button(root, text="Sửa Tên Sản Phẩm", command=update_product)
update_button.pack(pady=5)

# Khởi tạo cơ sở dữ liệu và bảng sản phẩm
create_table()

# Cập nhật danh sách sản phẩm khi khởi động
update_product_listbox()

# Khởi chạy ứng dụng
root.mainloop()
