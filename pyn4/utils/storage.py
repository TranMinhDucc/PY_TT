import json
import os

FILE_NAME = "registrations.json"


def save_registration(registration):
    data = []
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Tệp JSON bị lỗi, sẽ ghi đè lên dữ liệu cũ.")

    data.append(registration)

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_registrations():
    if not os.path.exists(FILE_NAME):
        print("Chưa có đăng ký nào.")
        return

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            registrations = json.load(file)
            for reg in registrations:
                print(
                    f"Đăng ký của {reg['name']}: Khóa học {reg['course_code']}, Ngày {reg['date']}, Chi phí {reg['cost']} VNĐ")
    except Exception as e:
        print(f"Lỗi khi đọc tệp JSON: {e}")
