import numpy as np

# 1. Đọc dữ liệu từ 2 tập tin vào các list
try:
    # Cung cấp đường dẫn tuyệt đối hoặc tương đối
    file_path_efficiency = 'D:/17A1KHDL/LAB2/DATA/efficiency.txt'  # Thay bằng đường dẫn chính xác của bạn
    file_path_shifts = 'D:/17A1KHDL/LAB2/DATA/shifts.txt'  # Thay bằng đường dẫn chính xác của bạn
    
    # Đọc dữ liệu từ file efficiency.txt
    with open(file_path_efficiency, 'r') as file:
        efficiency = [int(line.strip()) for line in file.readlines()]

    # Đọc dữ liệu từ file shifts.txt
    with open(file_path_shifts, 'r') as file:
        shifts = [line.strip() for line in file.readlines()]

    # In ra dữ liệu đã đọc để kiểm tra
    print("Efficiency Data: ", efficiency)
    print("Shifts Data: ", shifts)

except FileNotFoundError as e:
    print(f"Lỗi: Không tìm thấy tập tin {e.filename}")
    exit()

# 2. Tạo numpy array np_shifts từ list shifts và kiểm tra kiểu dữ liệu của np_shifts
np_shifts = np.array(shifts)
print("\nKiểu dữ liệu của np_shifts:", np_shifts.dtype)

# 3. Tạo numpy array np_efficiency từ list efficiency và kiểm tra kiểu dữ liệu của np_efficiency
np_efficiency = np.array(efficiency)
print("\nKiểu dữ liệu của np_efficiency:", np_efficiency.dtype)

# 4. Tính hiệu suất sản xuất trung bình của những nhân viên làm việc vào ca 'Morning'
morning_efficiency = np_efficiency[np_shifts == 'Morning']
average_morning_efficiency = np.mean(morning_efficiency) if len(morning_efficiency) > 0 else 0
print(f"\nHiệu suất trung bình của nhân viên làm việc vào ca 'Morning': {average_morning_efficiency}")

# 5. Tính hiệu suất sản xuất trung bình của những nhân viên làm việc trong các ca khác (Không phải là 'Morning')
non_morning_efficiency = np_efficiency[np_shifts != 'Morning']
average_non_morning_efficiency = np.mean(non_morning_efficiency) if len(non_morning_efficiency) > 0 else 0
print(f"Hiệu suất trung bình của nhân viên làm việc không phải ca 'Morning': {average_non_morning_efficiency}")

# 6. Tạo mảng dữ liệu có cấu trúc (Structure Array)
# Định nghĩa cấu trúc dữ liệu cho mảng workers: mỗi phần tử chứa 'shift' và 'efficiency'
dtype = [('shift', 'U10'), ('efficiency', 'f4')]  # 'U10' cho văn bản dài tối đa 10 ký tự, 'f4' cho kiểu float
workers = np.array(list(zip(np_shifts, np_efficiency)), dtype=dtype)

# 7. Sắp xếp mảng workers theo 'efficiency'
sorted_workers = np.sort(workers, order='efficiency')

# In ra mảng đã sắp xếp
print("\nMảng workers đã sắp xếp theo hiệu suất:")
print(sorted_workers)

# Xác định ca làm việc nào có hiệu suất cao nhất và thấp nhất
highest_efficiency_worker = sorted_workers[-1]  # Nhân viên có hiệu suất cao nhất (cuối mảng)
lowest_efficiency_worker = sorted_workers[0]  # Nhân viên có hiệu suất thấp nhất (đầu mảng)

print(f"\nNhân viên có hiệu suất cao nhất: {highest_efficiency_worker}")
print(f"Nhân viên có hiệu suất thấp nhất: {lowest_efficiency_worker}")
