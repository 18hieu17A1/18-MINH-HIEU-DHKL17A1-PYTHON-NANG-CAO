import json

# Đối tượng Python mẫu
data = {
    "students": [
        {
            "id": 1,
            "name": "Nguyễn Văn A",
            "age": 20,
            "gender": "Nam"
        },
        {
            "id": 2,
            "name": "Trần Thị B",
            "age": 22,
            "gender": "Nữ"
        },
        {
            "id": 3,
            "name": "Lê Văn C",
            "age": 21,
            "gender": "Nam"
        }
    ]
}

# Chuyển đổi đối tượng Python thành chuỗi JSON
json_string = json.dumps(data, ensure_ascii=False, indent=4)

# In ra chuỗi JSON
print("Chuỗi JSON:")
print(json_string)

# In ra tất cả các giá trị trong đối tượng Python
print("\nCác giá trị trong đối tượng Python:")
for student in data['students']:
    for key, value in student.items():
        print(f"{key}: {value}")
