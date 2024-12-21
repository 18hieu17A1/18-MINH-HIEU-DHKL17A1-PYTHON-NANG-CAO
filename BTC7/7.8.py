import tkinter as tk

# Hàm tìm tất cả các ước của một số
def find_divisors():
    try:
        # Lấy giá trị N từ hộp văn bản
        N = int(entry.get())
        
        # Kiểm tra nếu N là một số nguyên dương
        if N <= 0:
            label_result.config(text="Vui lòng nhập một số nguyên dương.")
            return
        
        # Tìm tất cả các ước của N
        divisors = [i for i in range(1, N + 1) if N % i == 0]
        
        # Hiển thị các ước
        label_result.config(text=f"Các ước của {N} là: {', '.join(map(str, divisors))}")
    
    except ValueError:
        # Nếu nhập không phải số nguyên
        label_result.config(text="Vui lòng nhập một số nguyên hợp lệ.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Liệt kê các ước của số N")

# Đặt kích thước cửa sổ
root.geometry("400x200")

# Thêm nhãn hướng dẫn
label_prompt = tk.Label(root, text="Nhập một số nguyên N:")
label_prompt.pack(pady=10)

# Thêm hộp văn bản để người dùng nhập N
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# Thêm nút để tìm các ước
button_calculate = tk.Button(root, text="Tính các ước", command=find_divisors)
button_calculate.pack(pady=10)

# Thêm nhãn để hiển thị kết quả
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Chạy vòng lặp chính của Tkinter
root.mainloop()
