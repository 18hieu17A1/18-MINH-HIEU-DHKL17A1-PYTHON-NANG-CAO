import numpy as np

# 1. Tạo Dữ Liệu Mô Phỏng Nhiệt Độ
temperatures = np.round(np.random.uniform(15, 35, 30), 2)

# Hiển thị dữ liệu nhiệt độ
print("Nhiệt độ hàng ngày trong tháng:")
print(temperatures)

# Tính nhiệt độ trung bình trong tháng
average_temperature = np.mean(temperatures)
print("\nNhiệt độ trung bình trong tháng:", round(average_temperature, 2))

# 2. Phân Tích Xu Hướng Nhiệt Độ
# - Xác định ngày có nhiệt độ cao nhất và thấp nhất

# Ngày có nhiệt độ cao nhất
max_temp = np.max(temperatures)
max_temp_day = np.argmax(temperatures) + 1  # Cộng 1 vì chỉ số mảng bắt đầu từ 0
print(f"\nNhiệt độ cao nhất là {max_temp}°C vào ngày {max_temp_day}")

# Ngày có nhiệt độ thấp nhất
min_temp = np.min(temperatures)
min_temp_day = np.argmin(temperatures) + 1
print(f"Nhiệt độ thấp nhất là {min_temp}°C vào ngày {min_temp_day}")

# - Thống kê sự chênh lệch nhiệt độ giữa các ngày và tìm ngày có sự biến đổi nhiệt độ cao nhất

# Tính sự biến đổi nhiệt độ giữa các ngày
temperature_diff = np.abs(np.diff(temperatures))

# Ngày có sự biến đổi nhiệt độ cao nhất
max_diff = np.max(temperature_diff)
max_diff_day = np.argmax(temperature_diff) + 2  # Cộng 2 vì diff giảm một phần tử so với temperatures
print(f"\nSự biến đổi nhiệt độ cao nhất là {max_diff}°C giữa ngày {max_diff_day - 1} và ngày {max_diff_day}")

# 3. Áp dụng Fancy Indexing

# - Tìm các ngày có nhiệt độ cao hơn 20°C
days_above_20 = np.where(temperatures > 20)[0] + 1  # Cộng 1 để chỉ số ngày bắt đầu từ 1
print(f"\nCác ngày có nhiệt độ trên 20°C: {days_above_20}")

# - Lấy nhiệt độ của ngày 5, 10, 15, 20, và 25
specific_days = [5, 10, 15, 20, 25]
print("\nNhiệt độ của các ngày 5, 10, 15, 20, 25:")
for day in specific_days:
    print(f"Ngày {day}: {temperatures[day - 1]}°C")

# - Tìm nhiệt độ của các ngày có nhiệt độ trên trung bình
days_above_average = temperatures[temperatures > average_temperature]
print(f"\nNhiệt độ của các ngày có nhiệt độ trên trung bình: {days_above_average}")

# - Ngày chẵn
even_days_temps = temperatures[1::2]  # Bắt đầu từ chỉ số 1 (ngày 2, 4, 6, ...)
print(f"\nNhiệt độ của các ngày chẵn: {even_days_temps}")

# - Ngày lẻ
odd_days_temps = temperatures[::2]  # Bắt đầu từ chỉ số 0 (ngày 1, 3, 5, ...)
print(f"Nhiệt độ của các ngày lẻ: {odd_days_temps}")
