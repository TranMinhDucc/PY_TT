# Danh sách các sách trong cửa hàng (mỗi cuốn là một dictionary)
books = [
    {"ten": "Python Cơ Bản", "gia": 75000, "ton_kho": 20, "ban_duoc": 15},
    {"ten": "Lập Trình Java", "gia": 120000, "ton_kho": 5, "ban_duoc": 3},
    {"ten": "C++ Nâng Cao", "gia": 95000, "ton_kho": 0, "ban_duoc": 7},
    {"ten": "Khoa Học Dữ Liệu", "gia": 150000, "ton_kho": 12, "ban_duoc": 20},
    {"ten": "Học Máy Cơ Bản", "gia": 45000, "ton_kho": 7, "ban_duoc": 11},
]
# Thông tin khách hàng
ten_khach = "Minh Duc"
loai_khach = "VIP"  # hoặc "thuong"
# Hàm tính tổng tiền hóa đơn


def calculate_bill(ten_sach, so_luong_mua, loai_khach):
    # Kiểm tra đầu vào
    if not isinstance(so_luong_mua, int) or so_luong_mua <= 0:
        return "Lỗi: Số lượng phải là số nguyên dương."

    for book in books:
        if book["ten"] == ten_sach:
            if book["ton_kho"] == 0:
                return "Sách đã hết hàng."
            elif book["ton_kho"] < so_luong_mua:
                return "Không đủ sách trong kho."

            tong_tien = book["gia"] * so_luong_mua

            # Giảm giá nếu là khách VIP
            if loai_khach.lower() == "vip":
                tong_tien *= 0.9  # Giảm 10%

            return float(tong_tien)  # Trả về kiểu float

    return "Không tìm thấy sách."
# Hàm kiểm tra tồn kho và phân loại giá


def check_stock(ten_sach, so_luong_mua):
    for book in books:
        if book["ten"] == ten_sach:
            # Kiểm tra tồn kho
            if book["ton_kho"] >= so_luong_mua:
                print("Còn hàng.")
                stock_status = True
            else:
                print("Hết hàng hoặc không đủ.")
                stock_status = False

            # Phân loại giá
            match book["gia"]:
                case gia if gia < 50000:
                    phan_loai = "Sách giá rẻ"
                case gia if 50000 <= gia <= 100000:
                    phan_loai = "Sách trung bình"
                case _:
                    phan_loai = "Sách cao cấp"

            return stock_status, phan_loai

    return False, "Không tìm thấy sách."

# Lambda tạo mã giảm giá


def ma_giam_gia(ten, loai): return ten.upper() + \
    ("_VIP" if loai.lower() == "vip" else "_REG")


# In mã giảm giá
print("Mã giảm giá của bạn là:", ma_giam_gia(ten_khach, loai_khach))
# In các sách bán chạy (số lượng bán > 10)
print("Danh sách sách bán chạy:")
for book in books:
    if book["ban_duoc"] > 10:
        print("-", book["ten"])

# Tìm sách bán chạy nhất
i = 0
max_ban = -1
sach_ban_chay_nhat = None

while i < len(books):
    if books[i]["ban_duoc"] > max_ban:
        max_ban = books[i]["ban_duoc"]
        sach_ban_chay_nhat = books[i]
    i += 1

print("Sách bán chạy nhất là:", sach_ban_chay_nhat["ten"])
print("Số lượng bán:", sach_ban_chay_nhat["ban_duoc"])
# Hàm chính


def main():
    # Tính hóa đơn ví dụ
    hoa_don = calculate_bill("Python Cơ Bản", 2, loai_khach)
    print("Tổng tiền cần thanh toán:", hoa_don)

    # Kiểm tra tồn kho và loại sách
    status, phan_loai = check_stock("Python Cơ Bản", 2)
    print("Phân loại sách:", phan_loai)

    # Mã giảm giá
    print("Mã giảm giá:", ma_giam_gia(ten_khach, loai_khach))

    # In sách bán chạy
    print("Các sách bán chạy:")
    for book in books:
        if book["ban_duoc"] > 10:
            print("-", book["ten"])

    # In sách bán chạy nhất
    i = 0
    max_ban = -1
    best_seller = None
    while i < len(books):
        if books[i]["ban_duoc"] > max_ban:
            best_seller = books[i]
            max_ban = books[i]["ban_duoc"]
        i += 1

    print("Sách bán chạy nhất:",
          best_seller["ten"], "-", best_seller["ban_duoc"], "cuốn")


# Gọi hàm main để chạy chương trình
main()
