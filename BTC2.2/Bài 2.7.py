import json

# Dữ liệu JSON mẫu
json_data = '''
{
    "name": "Nguyễn Văn A",
    "age": 25,
    "is_student": false,
    "courses": ["Toán", "Lý", "Hóa"],
    "address": {
        "street": "123 Đường ABC",
        "city": "Hà Nội"
    }
}
'''

# Chuyển đổi dữ liệu JSON thành đối tượng Python
python_object = json.loads(json_data)

# In ra đối tượng Python
print(python_object)

# Truy cập các thuộc tính
print(f"Tên: {python_object['name']}")
print(f"Tuổi: {python_object['age']}")
print(f"Các khóa học: {', '.join(python_object['courses'])}")
print(f"Địa chỉ: {python_object['address']['street']}, {python_object['address']['city']}")
