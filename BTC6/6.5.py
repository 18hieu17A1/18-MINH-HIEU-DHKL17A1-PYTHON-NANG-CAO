import threading
import requests

# Hàm gửi yêu cầu HTTP GET
def gui_yeu_cau_http(url, index):
    try:
        # Gửi yêu cầu GET đến URL
        response = requests.get(url)
        
        # Kiểm tra trạng thái trả về
        if response.status_code == 200:
            print(f"Yêu cầu {index} thành công. Mã trạng thái: {response.status_code}")
        else:
            print(f"Yêu cầu {index} thất bại. Mã trạng thái: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Yêu cầu {index} gặp lỗi: {e}")

# Danh sách các URL cần gửi yêu cầu HTTP
urls = [
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/posts",
    "https://api.github.com",
    "https://www.google.com"
]

# Tạo danh sách để lưu các luồng
threads = []

# Tạo và bắt đầu các luồng để gửi yêu cầu HTTP
for i, url in enumerate(urls):
    thread = threading.Thread(target=gui_yeu_cau_http, args=(url, i+1))
    threads.append(thread)
    thread.start()

# Đảm bảo tất cả các luồng hoàn thành trước khi kết thúc chương trình
for thread in threads:
    thread.join()

print("Tất cả yêu cầu HTTP đã hoàn thành.")
