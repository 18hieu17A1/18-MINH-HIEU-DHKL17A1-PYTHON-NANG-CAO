import tkinter as tk
from tkinter import messagebox

# Hàm xử lý khi người dùng nhấn nút Gửi
def greet_user():
    try:
        # Lấy tên và tuổi từ các hộp văn bản
        name = entry_name.get()
        age = int(entry_age.get())

        # Kiểm tra nếu tuổi >= 18
        if age >= 18:
            message = f"Xin chào {name}!\nBạn đã trưởng thành! ({age} tuổi)"
        else:
            message = f"Xin chào {name}!\nBạn còn nhỏ tuổi! ({age} tuổi)"
        
        # Hiển thị thông báo chào mừng
        messagebox.showinfo("Thông báo", message)
    
    except ValueError:
        # Nếu người dùng nhập tuổi không phải là số nguyên
        messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên hợp lệ cho tuổi.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chào mừng người dùng")

# Đặt kích thước cửa sổ
root.geometry("300x200")

# Thêm nhãn yêu cầu nhập tên
label_name = tk.Label(root, text="Nhập tên của bạn:")
label_name.pack(pady=5)

# Thêm hộp văn bản để người dùng nhập tên
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

# Thêm nhãn yêu cầu nhập tuổi
label_age = tk.Label(root, text="Nhập tuổi của bạn:")
label_age.pack(pady=5)

# Thêm hộp văn bản để người dùng nhập tuổi
entry_age = tk.Entry(root)
entry_age.pack(pady=5)

# Thêm nút Gửi để thực hiện hành động
button_greet = tk.Button(root, text="Gửi", command=greet_user)
button_greet.pack(pady=20)

# Chạy vòng lặp chính của Tkinter
root.mainloop()
