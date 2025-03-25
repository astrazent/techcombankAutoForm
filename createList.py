import csv

# Define the updated data
data = [
    ["Full Name", "ID", "Phone Number", "Sale"],
    ["Lương Gia Bảo", "50704448", "0813728351", "33921820"],
    ["Nguyễn Văn Tùng", "50704397", "0392131168", "33921820"],
    ["Vũ Tuấn Anh", "50704369", "0976796025", "33921820"],
    ["Đào Khánh Ly", "50704169", "0856630006", "33921820"],
    ["Đinh Thu Thảo", "50704110", "0986421258", "33921820"],
    ["Nguyễn Mậu Tùng", "50704045", "0961987233", "33921820"],
    ["Trần Thị Bích Phượng", "50703873", "0332723908", "33921820"],
    ["Lý Thị Diệu Linh", "50703840", "0816212710", "33921820"],
    ["Phạm Diệu Linh", "50703758", "0986258216", "33921820"],
    ["Lưu Phương Anh", "50703725", "0396197827", "33921820"],
    ["Lê Duy Hưng", "50703243", "0569423611", "33921820"],
    ["Nguyễn Thành An", "50703153", "0941254724", "33921820"],
    ["Bùi Thanh Bình", "50702920", "0983047545", "33921820"],
    ["Nguyễn Thị Hà Vy", "50695611", "0869969526", "33921820"],
    ["Trương Thị Thanh Thảo", "50695601", "0372160980", "33921820"],
    ["Đào Thị Tố Chinh", "50695498", "0867044950", "33921820"],
    ["Phạm Thu Trang", "50695376", "0333099203", "33921820"]
]

# Define the file name
filename = "employee_data_with_sale.csv"

# Write the data to a CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file created successfully: {filename}")
