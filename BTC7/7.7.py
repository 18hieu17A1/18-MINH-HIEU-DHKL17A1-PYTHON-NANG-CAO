import tkinter as tk

# Hàm tính tổng từ 1 đến N
def calculate_sum():
    try:
        # Lấy giá trị N từ hộp văn bản
        N = int(entry.get())
        
        # Tính tổng của các số từ 1 đến N
        total_sum = sum(range(1, N + 1))
        
        # Hiển thị kết quả
        label_result.config(text=f"Tổng của 1 + 2 + ... + {N} là: {total_sum}")
    except ValueError:
        # Nếu nhập không phải số nguyên
        label_result.config(text="Vui lòng nhập một số nguyên hợp lệ.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Tính Tổng Số")

# Đặt kích thước cửa sổ
root.geometry("400x200")

# Thêm nhãn hướng dẫn
label_prompt = tk.Label(root, text="Nhập một số nguyên N:")
label_prompt.pack(pady=10)

# Thêm hộp văn bản để người dùng nhập N
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# Thêm nút để tính tổng
button_calculate = tk.Button(root, text="Tính tổng", command=calculate_sum)
button_calculate.pack(pady=10)

# Thêm nhãn để hiển thị kết quả
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Chạy vòng lặp chính của Tkinter
root.mainloop()
