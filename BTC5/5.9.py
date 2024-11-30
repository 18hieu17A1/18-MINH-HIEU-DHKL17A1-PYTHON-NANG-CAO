import pandas as pd

# Đọc file CSV
file_path = 'region.csv'
df = pd.read_csv(file_path)

# Thay đổi số lượng dòng hiển thị mặc định (sử dụng None để hiển thị tất cả)
pd.set_option('display.max_rows', None)

# Hiển thị tất cả các dòng trong DataFrame
print(df)
