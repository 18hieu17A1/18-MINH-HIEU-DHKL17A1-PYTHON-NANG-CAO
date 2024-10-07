import json

# Đối tượng từ điển mẫu
data = {
    'banana': 1,
    'apple': 2,
    'orange': 3,
    'kiwi': 4
}

# Chuyển đổi đối tượng từ điển thành JSON, sắp xếp theo khóa và thụt lề 4
json_data = json.dumps(data, sort_keys=True, indent=4)

# In ra dữ liệu JSON
print(json_data)

