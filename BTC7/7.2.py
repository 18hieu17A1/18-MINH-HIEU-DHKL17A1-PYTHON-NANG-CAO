import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()

# Đặt tiêu đề cho cửa sổ
root.title("Cửa sổ Tkinter với Label")

# Đặt kích thước cửa sổ
root.geometry("400x300")  # Kích thước 400x300 pixels

# Tạo một nhãn (label) và đặt nội dung cho nó
label = tk.Label(root, text="Chào mừng đến với Tkinter!", font=("Arial", 14))
label.pack(pady=50)  # Thêm nhãn vào cửa sổ và đặt khoảng cách

# Chạy vòng lặp chính của Tkinter để cửa sổ hiển thị
root.mainloop()
