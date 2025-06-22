from utils.validator import validate_email, validate_course_code, validate_name
import pendulum  # Cài đặt: pip install pendulum


def get_user_input():
    while True:
        try:
            name = input("Nhập họ tên: ")
            validate_name(name)

            email = input("Nhập email: ")
            if not validate_email(email):
                raise ValueError("Email không hợp lệ. Vui lòng nhập lại.")

            course_code = input("Nhập mã khóa học (ví dụ: KH001): ")
            if not validate_course_code(course_code):
                raise ValueError("Mã khóa học không đúng định dạng (KHxxx).")

            registration_date = pendulum.now().to_date_string()
            return name, email, course_code, registration_date
        except ValueError as ve:
            print(f"Lỗi: {ve}")
