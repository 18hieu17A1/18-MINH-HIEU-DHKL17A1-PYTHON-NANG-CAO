import json
from datetime import datetime

# Danh sách giao dịch mẫu
giao_dich_tien_va_vang = [
    {"loai": "Tiền", "so_luong": 1000},
    {"loai": "Vàng", "so_luong": 2}
]

# Hàm lấy thông tin ngày giờ hiện tại theo định dạng yêu cầu
def lay_ngay_gio_hien_tai():
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# Hỏi người dùng có muốn ghi vào tập tin JSON không
lua_chon = input("Bạn có muốn ghi giao dịch vào tập tin không? (1: Có, 0: Không): ")

if lua_chon == "1":
    # Lấy ngày giờ hiện tại
    ten_tap_tin = lay_ngay_gio_hien_tai() + ".json"
    
    # Ghi danh sách giao dịch vào tập tin JSON
    with open(ten_tap_tin, "w", encoding="utf-8") as tap_tin:
        json.dump(giao_dich_tien_va_vang, tap_tin, ensure_ascii=False, indent=4)
    
    print(f"Ghi giao dịch thành công vào tệp tin: {ten_tap_tin}")
else:
    print("Không ghi giao dịch.")