import threading

# Hàm tính giai thừa cho một phạm vi
def tinh_giai_thua(start, end, result, index):
    product = 1
    for i in range(start, end + 1):
        product *= i
    result[index] = product

# Hàm tính giai thừa của n bằng cách chia công việc cho nhiều luồng
def tinh_giai_thua_voi_luong(n, so_luong_luong=4):
    # Chia n thành các phần công việc cho các luồng
    range_size = n // so_luong_luong
    threads = []
    result = [1] * so_luong_luong

    # Tạo các luồng
    for i in range(so_luong_luong):
        start = i * range_size + 1
        # Đảm bảo phần cuối cùng bao gồm tất cả các số còn lại
        end = (i + 1) * range_size if i != so_luong_luong - 1 else n
        thread = threading.Thread(target=tinh_giai_thua, args=(start, end, result, i))
        threads.append(thread)
        thread.start()

    # Chờ tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

    # Kết hợp kết quả từ các luồng
    giai_thua = 1
    for val in result:
        giai_thua *= val

    return giai_thua

# Ví dụ sử dụng
n = 10  # Tính giai thừa của số 10
so_luong_luong = 4  # Số lượng luồng

giai_thua = tinh_giai_thua_voi_luong(n, so_luong_luong)
print(f"Giai thừa của {n} là: {giai_thua}")
