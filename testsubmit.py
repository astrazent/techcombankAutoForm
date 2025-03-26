import threading
import time

# Hàm mà luồng sẽ chạy
def print_numbers():
    for i in range(7):
        time.sleep(1)
        print("luồng 2: " + str(str(i)))

# Tạo luồng
thread = threading.Thread(target=print_numbers)

# Bắt đầu luồng
thread.start()

for i in range(5):
    print("luồng 1: " + str(i))
    time.sleep(1)

# Chờ cho luồng kết thúc
thread.join()

for i in range(15):
    print("luồng 3: " + str(i))
    time.sleep(1)

print("Hoàn thành")
