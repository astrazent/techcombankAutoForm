from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Cài đặt các tùy chọn trình duyệt
options = Options()
options.headless = False  # Đặt thành True nếu bạn muốn chạy không hiển thị giao diện

# Khởi tạo WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Mở trang web cần tương tác
driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=6A4wK-aYa0C_-NiZmIWkw1P8sBeFZWJFmf4o0atKnxpUQllPSkk5QkxMWDBTNjkzNzRDVEtPUVA0Ri4u&origin=QRCode")  # Thay thế URL với trang web của bạn

# Chờ một chút cho trang tải
time.sleep(2)



# 1. Tên Địa điểm hoạt động triển khai
radio_button = driver.find_element(By.XPATH, '//span[@data-automation-id="radio" and @data-automation-value="MICRO0126-R5A-HGA-ĐH Kiến trúc"]/input')
if not radio_button.is_selected():
    radio_button.click()

# 2. Họ tên khách hàng
input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="QuestionId_r4b8eb40b1fa54739990ff1246cf7434f QuestionInfo_r4b8eb40b1fa54739990ff1246cf7434f"]'))
)

input_field.send_keys("Câu số 2")

# 3. Giới tính Khách hàng
radio_button = driver.find_element(By.XPATH, "//input[@value='Nam' and @type='radio']")
if not radio_button.is_selected():
    radio_button.click()

# 4. Số điện thoại khách hàng (VD: 0983123456)
input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="QuestionId_rfab26831a3df4a29ab8260aecb061f14 QuestionInfo_rfab26831a3df4a29ab8260aecb061f14"]'))
)

input_field.send_keys("Câu số 4")

# 5. Căn cước công dân của khách hàng (VD: 03112345678)
input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="QuestionId_r29f4b78e06ee4f38aa86b110b5622ffa QuestionInfo_r29f4b78e06ee4f38aa86b110b5622ffa"]'))
)

input_field.send_keys("Câu số 5")

# 6. Khách hàng đang giao dịch tài khoản tại ngân hàng nào
bank_checkbox = driver.find_element(By.XPATH, '//span[@data-automation-id="checkbox" and @data-automation-value="TCB"]/input')
if not bank_checkbox.is_selected():
    bank_checkbox.click()

# 7. Khách hàng đồng ý sử dụng SPDV nào (Deal)
bank_checkbox = driver.find_element(By.XPATH, '//span[@data-automation-id="checkbox" and @data-automation-value="Tài khoản mới"]/input')
if not bank_checkbox.is_selected():
    bank_checkbox.click()

# 8. Trong thời gian tới khách hàng có nhu cầu tư vấn SPDV nào?
bank_checkbox = driver.find_element(By.XPATH, '//span[@data-automation-id="checkbox" and @data-automation-value="Tài khoản"]/input')
if not bank_checkbox.is_selected():
    bank_checkbox.click()

# 9. KH đã được tặng loại quà nào
radio_button = driver.find_element(By.XPATH, "//input[@value='Bút bi' and @type='radio']")
if not radio_button.is_selected():
    radio_button.click()

# 10. ID sale của chuyên viên chăm sóc (ID sale: 12345678)
input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="QuestionId_rc905ba604c0f40a7ae0c089919b2d1d4 QuestionInfo_rc905ba604c0f40a7ae0c089919b2d1d4"]'))
)

input_field.send_keys("Câu số 10")

# 11. Chức danh của chuyên viên
radio_button = driver.find_element(By.XPATH, "//input[@value='UB' and @type='radio']")
if not radio_button.is_selected():
    radio_button.click()

# 12. Mã chi nhánh: (Ví dụ: TLG)
input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="QuestionId_ra39c7b4e46f64477a5938833ed8b5abb QuestionInfo_ra39c7b4e46f64477a5938833ed8b5abb"]'))
)

input_field.send_keys("Câu số 12")

# Chờ một chút để xem kết quả
time.sleep(10)

# Đóng trình duyệt
driver.quit()
