import tkinter as tk

# Hàm kiểm tra xem tất cả các trường đã được điền hay chưa
def check_entries():
    # Lấy giá trị từ các hộp văn bản
    name = entry_name.get()
    student_id = entry_id.get()
    password = entry_password.get()
    
    # Kiểm tra xem tất cả các trường đã được điền
    if name and student_id and password:
        # Nếu có đủ thông tin, hiển thị nút gửi
        submit_button.pack(pady=20)
    else:
        # Nếu không đủ thông tin, ẩn nút gửi
        submit_button.pack_forget()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Thông tin Sinh viên")

# Đặt kích thước cửa sổ
root.geometry("400x300")

# Thêm nhãn cho tên sinh viên
label_name = tk.Label(root, text="Tên Sinh viên:")
label_name.pack(pady=5)

# Thêm hộp văn bản cho tên sinh viên
entry_name = tk.Entry(root)
entry_name.pack(pady=5)
entry_name.bind("<KeyRelease>", lambda event: check_entries())  # Kiểm tra khi người dùng nhập

# Thêm nhãn cho ID sinh viên
label_id = tk.Label(root, text="ID Sinh viên:")
label_id.pack(pady=5)

# Thêm hộp văn bản cho ID sinh viên
entry_id = tk.Entry(root)
entry_id.pack(pady=5)
entry_id.bind("<KeyRelease>", lambda event: check_entries())  # Kiểm tra khi người dùng nhập

# Thêm nhãn cho mật khẩu
label_password = tk.Label(root, text="Mật khẩu:")
label_password.pack(pady=5)

# Thêm hộp văn bản cho mật khẩu
entry_password = tk.Entry(root, show="*")  # Sử dụng show="*" để ẩn mật khẩu
entry_password.pack(pady=5)
entry_password.bind("<KeyRelease>", lambda event: check_entries())  # Kiểm tra khi người dùng nhập

# Thêm nút gửi, nhưng không hiển thị ban đầu
submit_button = tk.Button(root, text="Gửi", command=lambda: print("Thông tin đã được gửi"))
# submit_button.pack(pady=20)  # Ban đầu nút không hiển thị

# Chạy vòng lặp chính của Tkinter
root.mainloop()
