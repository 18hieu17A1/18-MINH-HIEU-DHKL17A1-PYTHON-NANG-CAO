import threading
import requests

# Hàm tải tệp
def tai_tep(url, ten_tep):
    try:
        # Gửi yêu cầu tải xuống tệp
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra nếu có lỗi xảy ra trong quá trình tải
        # Lưu tệp vào ổ đĩa
        with open(ten_tep, 'wb') as f:
            f.write(response.content)
        print(f"Tải tệp {ten_tep} thành công.")
    except requests.exceptions.RequestException as e:
        print(f"Đã xảy ra lỗi khi tải tệp {ten_tep}: {e}")

# Danh sách các URL tệp cần tải xuống
url_tep = [
    ("https://example.com/file1.jpg", "file1.jpg"),
    ("https://example.com/file2.jpg", "file2.jpg"),
    ("https://example.com/file3.jpg", "file3.jpg")
]

# Tạo và bắt đầu các luồng
threads = []
for url, ten_tep in url_tep:
    thread = threading.Thread(target=tai_tep, args=(url, ten_tep))
    threads.append(thread)
    thread.start()

# Đảm bảo tất cả các luồng hoàn thành
for thread in threads:
    thread.join()

print("Tất cả các tệp đã được tải xuống.")
