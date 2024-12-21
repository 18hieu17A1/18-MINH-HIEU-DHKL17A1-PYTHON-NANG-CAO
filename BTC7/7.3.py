import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()

# Đặt tiêu đề cho cửa sổ
root.title("Chương trình với Nhãn và Phông chữ")

# Đặt kích thước cửa sổ
root.geometry("400x300")  # Kích thước cửa sổ là 400x300 pixels

# Tạo một nhãn (label) với phông chữ tùy chỉnh
label = tk.Label(root, 
                 text="Chào mừng bạn đến với Tkinter!", 
                 font=("Helvetica", 16, "bold"))  # Tên phông chữ, kích thước, độ đậm

# Thêm nhãn vào cửa sổ và đặt khoảng cách
label.pack(pady=50)

# Chạy vòng lặp chính để cửa sổ hiển thị
root.mainloop()
