import json

# Dữ liệu mẫu trong JSON (có thể thay bằng việc đọc từ tệp)
du_lieu_json = '''
{
    "cong_ty": {
        "ten": "Công ty TNHH Đất Việt",
        "dia_chi": "abc Giải Phóng - Hà Nội",
        "cac_don_vi": [
            {"ten_don_vi": "Đơn vị A1", "so_nhan_vien": 50},
            {"ten_don_vi": "Đơn vị A2", "so_nhan_vien": 30},
            {"ten_don_vi": "Đơn vị A3", "so_nhan_vien": 20},
            {"ten_don_vi": "Đơn vị A4", "so_nhan_vien": 10}
        ]
    }
}
'''

# Đọc dữ liệu từ JSON
du_lieu = json.loads(du_lieu_json)

# Lấy thông tin công ty và các đơn vị
ten_cong_ty = du_lieu['cong_ty']['ten']
dia_chi_cong_ty = du_lieu['cong_ty']['dia_chi']
cac_don_vi = du_lieu['cong_ty']['cac_don_vi']

# Tính tổng số nhân viên
tong_so_nhan_vien = sum(don_vi['so_nhan_vien'] for don_vi in cac_don_vi)

# In thông tin công ty
print(f"Tên công ty: {ten_cong_ty}")
print(f"Địa chỉ: {dia_chi_cong_ty}")
print(f"Tổng số nhân viên: {tong_so_nhan_vien}")
print("-----Thống kê nhân viên theo đơn vị-----")

# In thống kê theo từng đơn vị
for i, don_vi in enumerate(cac_don_vi, start=1):
    ten_don_vi = don_vi['ten_don_vi']
    so_nhan_vien = don_vi['so_nhan_vien']
    ty_le = (so_nhan_vien / tong_so_nhan_vien) * 100
    print(f"{i}. Tên đơn vị: {ten_don_vi}")
    print(f"   - Số nhân viên: {so_nhan_vien}")
    print(f"   - Tỷ lệ: {ty_le:.2f}%")