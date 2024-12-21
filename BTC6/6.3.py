import threading

# Hàm để tìm và in các số chẵn
def in_so_chan():
    print("Các số chẵn từ 30 đến 50:")
    for i in range(30, 51):
        if i % 2 == 0:
            print(i)

# Hàm để tìm và in các số lẻ
def in_so_le():
    print("Các số lẻ từ 30 đến 50:")
    for i in range(30, 51):
        if i % 2 != 0:
            print(i)

# Tạo 2 luồng cho việc in số chẵn và số lẻ
thread_chan = threading.Thread(target=in_so_chan)
thread_le = threading.Thread(target=in_so_le)

# Bắt đầu cả hai luồng
thread_chan.start()
thread_le.start()

# Đảm bảo rằng cả hai luồng hoàn thành trước khi chương trình chính kết thúc
thread_chan.join()
thread_le.join()

print("Hoàn thành việc in số chẵn và số lẻ.")
