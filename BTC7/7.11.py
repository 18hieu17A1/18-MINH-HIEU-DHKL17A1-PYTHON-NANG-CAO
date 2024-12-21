import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Tạo danh sách các con giáp
animals = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']

# Hàm chuyển đổi năm Dương lịch sang năm Âm lịch
def convert_to_lunar_year():
    try:
        # Lấy năm Dương lịch từ hộp nhập liệu
        year = int(entry_year.get())
        
        # Tính năm Âm lịch tương ứng (âm lịch bắt đầu từ năm 1900)
        lunar_year = (year - 1900) % 12
        animal = animals[lunar_year]

        # Hiển thị kết quả trong một hộp thông báo
        messagebox.showinfo("Kết quả", f"Năm {year} Dương lịch tương ứng với năm {animal} trong Âm lịch.")

        # Hiển thị hình ảnh con giáp
        image_path = f"{animal.lower()}.png"  # Đảm bảo các hình ảnh được đặt tên theo đúng tên con giáp (tý.png, suu.png, ...)
        
        # Mở và hiển thị hình ảnh
        img = Image.open(image_path)
        img = img.resize((200, 200))  # Resize hình ảnh cho phù hợp với cửa sổ
        img = ImageTk.PhotoImage(img)

        # Cập nhật hình ảnh con giáp vào nhãn
        label_image.config(image=img)
        label_image.image = img  # Giữ tham chiếu hình ảnh

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một năm Dương lịch hợp lệ.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển đổi năm Dương lịch sang Âm lịch")

# Đặt kích thước cửa sổ
root.geometry("400x400")

# Thêm nhãn yêu cầu nhập năm Dương lịch
label_prompt = tk.Label(root, text="Nhập năm Dương lịch:")
label_prompt.pack(pady=10)

# Thêm ô nhập liệu năm Dương lịch
entry_year = tk.Entry(root)
entry_year.pack(pady=10)

# Thêm nút chuyển đổi
button_convert = tk.Button(root, text="Chuyển đổi", command=convert_to_lunar_year)
button_convert.pack(pady=10)

# Thêm nhãn để hiển thị hình ảnh con giáp
label_image = tk.Label(root)
label_image.pack(pady=20)

# Chạy vòng lặp chính của Tkinter
root.mainloop()
