import threading

# Hàm sẽ được thực thi bởi mỗi luồng
def in_ten_luong():
    # In tên của luồng
    print(f"Đây là luồng có tên: {threading.current_thread().name}")

# Số lượng luồng muốn tạo
so_luong_luong = 5

# Tạo và bắt đầu các luồng
threads = []
for i in range(so_luong_luong):
    thread = threading.Thread(target=in_ten_luong)
    threads.append(thread)
    thread.start()

# Đảm bảo tất cả các luồng hoàn thành trước khi kết thúc chương trình chính
for thread in threads:
    thread.join()

print("Tất cả các luồng đã hoàn thành.")
