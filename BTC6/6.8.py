import threading
import random

# Hàm tính tổng của một phần danh sách
def tinh_tong(start, end, data, result, index):
    partial_sum = sum(data[start:end])
    result[index] = partial_sum
    print(f"Thread {index} tính tổng từ chỉ số {start} đến {end-1}: {partial_sum}")

# Hàm chạy chương trình chính
def main():
    n = 100  # Số phần tử trong danh sách
    num_threads = 4  # Số lượng luồng
    data = [random.randint(0, 10) for _ in range(n)]  # Tạo danh sách ngẫu nhiên

    print(f"Danh sách ban đầu: {data}")

    # Kích thước mỗi phần cần tính
    chunk_size = n // num_threads
    threads = []
    result = [0] * num_threads  # Mảng chứa kết quả tính tổng của mỗi luồng

    # Tạo và bắt đầu các luồng
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else n
        thread = threading.Thread(target=tinh_tong, args=(start, end, data, result, i))
        threads.append(thread)
        thread.start()

    # Đảm bảo tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

    # Tính tổng cuối cùng từ các kết quả của các luồng
    total_sum = sum(result)
    print(f"Tổng của tất cả các phần tử trong danh sách là: {total_sum}")

# Chạy chương trình
if __name__ == "__main__":
    main()
