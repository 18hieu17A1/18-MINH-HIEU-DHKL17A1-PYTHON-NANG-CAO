import tkinter as tk
import math

# Hàm tính Ước số chung lớn nhất GCD
def calculate_gcd():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        
        # Tính GCD bằng hàm gcd của thư viện math
        gcd_result = math.gcd(a, b)
        
        # Hiển thị kết quả
        label_gcd.config(text=f"GCD của {a} và {b} là: {gcd_result}")
    except ValueError:
        label_gcd.config(text="Vui lòng nhập hai số nguyên hợp lệ.")

# Hàm tính Bội số chung nhỏ nhất LCM
def calculate_lcm():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        
        # Tính LCM bằng công thức: LCM(a, b) = |a * b| / GCD(a, b)
        lcm_result = abs(a * b) // math.gcd(a, b)
        
        # Hiển thị kết quả
        label_lcm.config(text=f"LCM của {a} và {b} là: {lcm_result}")
    except ValueError:
        label_lcm.config(text="Vui lòng nhập hai số nguyên hợp lệ.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Tính GCD và LCM")

# Đặt kích thước cửa sổ
root.geometry("400x250")

# Thêm nhãn hướng dẫn
label_prompt = tk.Label(root, text="Nhập hai số nguyên:")
label_prompt.pack(pady=10)

# Thêm hộp văn bản để người dùng nhập số A
label_a = tk.Label(root, text="Số A:")
label_a.pack(pady=5)
entry_a = tk.Entry(root, width=20)
entry_a.pack(pady=5)

# Thêm hộp văn bản để người dùng nhập số B
label_b = tk.Label(root, text="Số B:")
label_b.pack(pady=5)
entry_b = tk.Entry(root, width=20)
entry_b.pack(pady=5)

# Thêm nút để tính GCD
button_gcd = tk.Button(root, text="Tính GCD", command=calculate_gcd)
button_gcd.pack(pady=5)

# Thêm nút để tính LCM
button_lcm = tk.Button(root, text="Tính LCM", command=calculate_lcm)
button_lcm.pack(pady=5)

# Thêm nhãn để hiển thị kết quả GCD
label_gcd = tk.Label(root, text="")
label_gcd.pack(pady=10)

# Thêm nhãn để hiển thị kết quả LCM
label_lcm = tk.Label(root, text="")
label_lcm.pack(pady=10)

# Chạy vòng lặp chính của Tkinter
root.mainloop()
