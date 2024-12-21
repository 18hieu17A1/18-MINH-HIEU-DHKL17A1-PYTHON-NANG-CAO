import tkinter as tk

# Hàm đảo ngược chuỗi
def reverse_string():
    input_string = entry.get()  # Lấy chuỗi từ hộp văn bản
    reversed_string = ""
    
    # Duyệt qua từng ký tự của chuỗi từ cuối đến đầu và xây dựng chuỗi ngược lại
    for char in input_string:
        reversed_string = char + reversed_string  # Thêm ký tự vào đầu chuỗi kết quả
    
    # Hiển thị chuỗi ngược lại trong nhãn
    label_result.config(text="Chuỗi ngược lại là: " + reversed_string)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Đảo Ngược Chuỗi")

# Đặt kích thước cửa sổ
root.geometry("400x200")

# Tạo nhãn hướng dẫn
label_prompt = tk.Label(root, text="Nhập một từ:")
label_prompt.pack(pady=10)

# Tạo hộp văn bản để nhập chuỗi
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Tạo nút để thực hiện việc đảo ngược chuỗi
reverse_button = tk.Button(root, text="Đảo ngược", command=reverse_string)
reverse_button.pack(pady=10)

# Tạo nhãn để hiển thị kết quả
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Chạy vòng lặp chính của Tkinter
root.mainloop()
