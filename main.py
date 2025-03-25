import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
import pygame
import io
from gtts import gTTS

# Đọc dữ liệu từ file CSV
data_file = "test.csv"  # Đường dẫn đến file CSV
df = pd.read_csv(data_file)

# Cấu hình Selenium
options = Options()
options.headless = False
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Mở form
form_url = "https://forms.office.com/Pages/ResponsePage.aspx?id=6A4wK-aYa0C_-NiZmIWkw1P8sBeFZWJFmf4o0atKnxpUQllPSkk5QkxMWDBTNjkzNzRDVEtPUVA0Ri4u&origin=QRCode"
driver.get(form_url)
time.sleep(2)

# Khởi tạo pygame mixer một lần duy nhất
pygame.mixer.init()

def doan_gioi_tinh_api(ten):
    url = f"https://api.genderize.io/?name={ten}"
    response = requests.get(url).json()
    gender = response.get("gender")
    
    if gender == "male":
        return True
    elif gender == "female":
        return False
    return None  # Trả về None nếu không xác định được giới tính

def speak(text, lang="vi"):
    """
    Chuyển văn bản thành giọng nói và phát ngay lập tức mà không load lại pygame.
    """
    try:
        # Tạo giọng nói từ văn bản
        tts = gTTS(text=text, lang=lang)

        # Lưu vào bộ nhớ RAM
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        # Khởi động pygame và phát âm thanh với tốc độ nhanh hơn
        pygame.mixer.init()
        pygame.mixer.music.load(mp3_fp, "mp3")
        pygame.mixer.music.play()

        # Chờ cho phát xong
        while pygame.mixer.music.get_busy():
            continue

    except Exception as e:
        print(f"Lỗi phát giọng nói: {e}")




for index, row in df.iterrows():
    full_name = row["Full Name"]
    phone_number = str(row["Phone Number"]).zfill(10)
    id_number = str(row["ID"])
    sale_id = str(row["Sale"])
    
    # 1. Chọn địa điểm
    driver.find_element(By.XPATH, "//span[@data-automation-id='radio' and @data-automation-value='MICRO0126-R5A-HGA-ĐH Kiến trúc']/input").click()

    # 2. Họ tên khách hàng
    name_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="QuestionId_r4b8eb40b1fa54739990ff1246cf7434f QuestionInfo_r4b8eb40b1fa54739990ff1246cf7434f"]')))
    name_field.send_keys(full_name)

    gender = 0
    # 3. Giới tính khách hàng
    if(doan_gioi_tinh_api(full_name)):
        driver.find_element(By.XPATH, "//input[@value='Nam' and @type='radio']").click()
    else:
        driver.find_element(By.XPATH, "//input[@value='Nữ' and @type='radio']").click()
        gender = 1
    
    # 4. Số điện thoại khách hàng
    phone_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="QuestionId_rfab26831a3df4a29ab8260aecb061f14 QuestionInfo_rfab26831a3df4a29ab8260aecb061f14"]')))
    phone_field.send_keys(phone_number)
    
    # 5. Căn cước công dân
    id_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="QuestionId_r29f4b78e06ee4f38aa86b110b5622ffa QuestionInfo_r29f4b78e06ee4f38aa86b110b5622ffa"]')))
    id_field.send_keys(id_number)
    
    # 6. Ngân hàng giao dịch
    driver.find_element(By.XPATH, "//span[@data-automation-id='checkbox' and @data-automation-value='MB']/input").click()
    
    # 7. Dịch vụ sử dụng
    driver.find_element(By.XPATH, "//span[@data-automation-id='checkbox' and @data-automation-value='Tài khoản mới']/input").click()
    driver.find_element(By.XPATH, "//span[@data-automation-id='checkbox' and @data-automation-value='AE+']/input").click()
    
    # 8. Nhu cầu tư vấn
    driver.find_element(By.XPATH, "//span[@data-automation-id='checkbox' and @data-automation-value='Tài khoản']/input").click()
    
    # 9. Loại quà tặng
    driver.find_element(By.XPATH, "//input[@value='Không có quà tặng' and @type='radio']").click()
    
    # 10. ID Sale
    sale_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="QuestionId_rc905ba604c0f40a7ae0c089919b2d1d4 QuestionInfo_rc905ba604c0f40a7ae0c089919b2d1d4"]')))
    sale_field.send_keys(sale_id)
    
    # 11. Chức danh
    driver.find_element(By.XPATH, "//input[@value='UB' and @type='radio']").click()
    
    # 12. Mã chi nhánh
    branch_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="QuestionId_ra39c7b4e46f64477a5938833ed8b5abb QuestionInfo_ra39c7b4e46f64477a5938833ed8b5abb"]')))
    branch_field.send_keys("NHN")

    if(not gender):
        speak("...Tên: " + full_name + '.' + "Điện thoại: " + phone_number + '.' + "Giới tính: " + "Nam" + '.' + "ID: " + sale_id)
    else:
        speak("...Tên: " + full_name + '.' + "Điện thoại: " + phone_number + '.' + "Giới tính: " + "Nữ" + '.' + "ID: " + sale_id)
    
    # Chờ trước khi điền dữ liệu tiếp theo
    input("Nhấn Enter để tiếp tục nhập dữ liệu...")

# Đóng trình duyệt
driver.quit()