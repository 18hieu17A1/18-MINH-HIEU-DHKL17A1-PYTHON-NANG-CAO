import threading
import random

# Hàm tìm giá trị lớn nhất trong một phần của danh sách
def find_max(start, end, data, result, index):
    partial_max = max(data[start:end])  # Tìm max trong phần danh sách con
    result[index] = partial_max
    print(f"Thread {index} tìm max từ chỉ số {start} đến {end-1}: {partial_max}")

# Hàm chạy chương trình chính
def main():
    n = 100  # Số phần tử trong danh sách
    num_threads = 4  # Số lượng luồng
    data = [random.randint(0, 100) for _ in range(n)]  # Tạo danh sách ngẫu nhiên

    print(f"Danh sách ban đầu: {data}")

    # Kích thước mỗi phần cần tính
    chunk_size = n // num_threads
    threads = []
    result = [0] * num_threads  # Mảng chứa kết quả max của mỗi luồng

    # Tạo và bắt đầu các luồng
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else n
        thread = threading.Thread(target=find_max, args=(start, end, data, result, i))
        threads.append(thread)
        thread.start()

    # Đảm bảo tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

    # Tìm giá trị lớn nhất cuối cùng từ các kết quả của các luồng
    total_max = max(result)
    print(f"Giá trị lớn nhất trong danh sách là: {total_max}")

# Chạy chương trình
if __name__ == "__main__":
    main()
