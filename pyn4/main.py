from utils.input_handler import get_user_input
from utils.calculator import calculate_cost
from utils.storage import save_registration, load_registrations


def main():
    print("=== Hệ thống đăng ký khóa học trực tuyến ===")
    name, email, course_code, date = get_user_input()

    try:
        quantity = int(input("Nhập số lượng khóa học muốn đăng ký: "))
        promo_code = input("Nhập mã ưu đãi (nếu có): ").strip()

        cost = calculate_cost(course_code, quantity, promo_code)
        print(f"Tổng chi phí cho {quantity} khóa học là: {cost} VNĐ.")

        print(
            f"Chúc mừng {name} đã đăng ký khóa học {course_code} vào ngày {date}!")

        registration = {
            "name": name,
            "email": email,
            "course_code": course_code,
            "date": date,
            "cost": cost
        }

        save_registration(registration)
        print("\n--- Danh sách đăng ký hiện tại ---")
        load_registrations()

    except ValueError as ve:
        print(f"Lỗi: {ve}")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")


if __name__ == "__main__":
    main()
