import cv2
import pytesseract
import numpy as np
import pandas as pd


pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ADMIN\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
# Đọc ảnh
image_path = "pic1.jpg"
image = cv2.imread(image_path)

# Tiền xử lý ảnh (chuyển sang grayscale, làm nét, threshold)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3,3), 0)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)

# Tìm đường viền bảng
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sắp xếp contour theo vị trí để xử lý từ trên xuống
contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[1])

data = []

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if w > 50 and h > 20:  # Lọc các vùng nhỏ không phải ô bảng
        roi = image[y:y+h, x:x+w]
        text = pytesseract.image_to_string(roi, config='--psm 6').strip()
        data.append(text)

# Định dạng lại thành DataFrame 6 cột
num_cols = 6
rows = [data[i:i+num_cols] for i in range(0, len(data), num_cols)]
df = pd.DataFrame(rows, columns=[f"Cột {i+1}" for i in range(num_cols)])

# Xuất ra CSV
df.to_csv("table_data.csv", index=False, encoding="utf-8-sig")
print(df)
