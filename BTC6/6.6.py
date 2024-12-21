import threading

# Hàm in các số chẵn
def in_so_chan(nguong):
    print("Các số chẵn:")
    for i in range(2, nguong, 2):
        print(i)

# Hàm in các số lẻ
def in_so_le(nguo):
    print("Các số lẻ:")
    for i in range(1, nguo, 2):
        print(i)

# Ngưỡng cần in số
ngưỡng = 20  # bạn có thể thay đổi giá trị này để kiểm tra với ngưỡng khác

# Tạo các luồng
thread_chan = threading.Thread(target=in_so_chan, args=(ngưỡng,))
thread_le = threading.Thread(target=in_so_le, args=(ngưỡng,))

# Bắt đầu các luồng
thread_chan.start()
thread_le.start()

# Đảm bảo tất cả các luồng hoàn thành trước khi kết thúc chương trình
thread_chan.join()
thread_le.join()

print("Hoàn thành việc in số chẵn và số lẻ.")
