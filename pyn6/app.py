import os


def create_weekly_log():
    try:
        week = int(input("Nhập số tuần: "))
        hours = float(input("Nhập số giờ làm việc: "))
        tasks = int(input("Nhập số nhiệm vụ hoàn thành: "))
        notes = input("Nhập ghi chú: ")

        filename = f"week_{week}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Tuần: {week}\n")
            file.write(f"Số giờ làm việc: {hours}\n")
            file.write(f"Nhiệm vụ hoàn thành: {tasks}\n")
            file.write(f"Ghi chú: {notes}\n")

        print(f"Đã tạo nhật ký tuần {week}")
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng số.")


def read_weekly_log():
    try:
        week = int(input("Nhập số tuần cần đọc: "))
        filename = f"week_{week}.txt"
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                print("\n--- Nội dung nhật ký ---")
                print(file.read())
        else:
            print(f"Nhật ký tuần {week} không tồn tại.")
    except ValueError:
        print("Lỗi: Vui lòng nhập số tuần hợp lệ.")


def update_weekly_log():
    try:
        week = int(input("Nhập số tuần cần cập nhật: "))
        hours = float(input("Nhập số giờ mới: "))
        tasks = int(input("Nhập số nhiệm vụ mới: "))
        notes = input("Nhập ghi chú mới: ")

        filename = f"week_{week}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Tuần: {week}\n")
            file.write(f"Số giờ làm việc: {hours}\n")
            file.write(f"Nhiệm vụ hoàn thành: {tasks}\n")
            file.write(f"Ghi chú: {notes}\n")

        print(f"Đã cập nhật nhật ký tuần {week}")
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng.")


def delete_weekly_log():
    try:
        week = int(input("Nhập số tuần cần xóa: "))
        filename = f"week_{week}.txt"
        if os.path.exists(filename):
            os.remove(filename)
            print(f"🗑️ Đã xóa nhật ký tuần {week}")
        else:
            print(f"⚠️ Không tìm thấy nhật ký tuần {week}")
    except ValueError:
        print("Lỗi: Nhập số tuần không hợp lệ.")


def generate_summary():
    total_weeks = 0
    total_hours = 0.0
    total_tasks = 0

    for file in os.listdir():
        if file.startswith("week_") and file.endswith(".txt"):
            total_weeks += 1
            with open(file, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if "Số giờ làm việc:" in line:
                        total_hours += float(line.strip().split(":")[1])
                    elif "Nhiệm vụ hoàn thành:" in line:
                        total_tasks += int(line.strip().split(":")[1])

    print("\n📊 Báo cáo tổng kết:")
    print(f"Tổng số tuần: {total_weeks}")
    print(f"Tổng số giờ làm việc: {total_hours}")
    print(f"Tổng nhiệm vụ hoàn thành: {total_tasks}")


def main():
    while True:
        print("\n Menu:")
        print("1. Tạo nhật ký tuần mới")
        print("2. Đọc nhật ký tuần")
        print("3. Cập nhật nhật ký tuần")
        print("4. Xóa nhật ký tuần")
        print("5. Tạo báo cáo tổng kết")
        print("6. Thoát")

        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            create_weekly_log()
        elif choice == "2":
            read_weekly_log()
        elif choice == "3":
            update_weekly_log()
        elif choice == "4":
            delete_weekly_log()
        elif choice == "5":
            generate_summary()
        elif choice == "6":
            print("👋 Thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 6.")


if __name__ == "__main__":
    main()
