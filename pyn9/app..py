import mysql.connector


def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
    )


def setup_database():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS project_progress")
    cursor.execute("USE project_progress")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            member_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            role VARCHAR(50)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weekly_progress (
            progress_id INT AUTO_INCREMENT PRIMARY KEY,
            member_id INT,
            week_number INT,
            hours_worked FLOAT CHECK (hours_worked >= 0),
            tasks_completed INT,
            notes TEXT,
            FOREIGN KEY (member_id) REFERENCES members(member_id)
        )
    """)

    conn.commit()
    conn.close()


def add_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("USE project_progress")

    members = [
        ("An", "Developer"),
        ("Bình", "Tester"),
        ("Cường", "Designer"),
        ("Dũng", "Manager"),
        ("Hà", "QA")
    ]
    cursor.executemany(
        "INSERT INTO members (name, role) VALUES (%s, %s)", members)

    cursor.execute("SELECT member_id FROM members")
    member_ids = [row[0] for row in cursor.fetchall()]

    progress_data = [
        (member_ids[0], 1, 40, 5, "Làm API xong"),
        (member_ids[1], 1, 38, 4, "Test 3 tính năng"),
        (member_ids[2], 1, 35, 3, "Thiết kế xong UI"),
        (member_ids[3], 1, 45, 6, "Quản lý nhóm"),
        (member_ids[4], 1, 30, 2, "Kiểm tra chất lượng"),
        (member_ids[0], 2, 42, 6, "Fix lỗi API"),
        (member_ids[1], 2, 40, 5, "Test chức năng mới"),
        (member_ids[2], 2, 37, 4, "Sửa giao diện"),
        (member_ids[3], 2, 44, 5, "Quản lý dự án"),
        (member_ids[4], 2, 32, 3, "Kiểm thử thêm")
    ]
    cursor.executemany("""
        INSERT INTO weekly_progress (member_id, week_number, hours_worked, tasks_completed, notes)
        VALUES (%s, %s, %s, %s, %s)
    """, progress_data)

    conn.commit()
    conn.close()


def query_progress(week_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("USE project_progress")

    cursor.execute("""
        SELECT m.name, wp.hours_worked, wp.tasks_completed, wp.notes
        FROM weekly_progress wp
        JOIN members m ON wp.member_id = m.member_id
        WHERE wp.week_number = %s
        ORDER BY wp.tasks_completed DESC
        LIMIT 5
    """, (week_number,))

    results = cursor.fetchall()
    print(f"Tuần {week_number}:")
    for row in results:
        print(f"- {row[0]}: {row[1]} giờ, {row[2]} nhiệm vụ, Ghi chú: {row[3]}")

    conn.close()


def update_progress(progress_id, hours_worked, notes):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("USE project_progress")

    cursor.execute("""
        UPDATE weekly_progress
        SET hours_worked = %s, notes = %s
        WHERE progress_id = %s
    """, (hours_worked, notes, progress_id))

    conn.commit()
    if cursor.rowcount > 0:
        print(" Đã cập nhật bản ghi.")
    else:
        print(" Không tìm thấy bản ghi.")
    conn.close()


def delete_progress(week_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("USE project_progress")

    cursor.execute(
        "DELETE FROM weekly_progress WHERE week_number = %s", (week_number,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f" Đã xoá {cursor.rowcount} bản ghi tuần {week_number}.")
    else:
        print(" Không có bản ghi nào để xoá.")
    conn.close()


def generate_summary():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("USE project_progress")

    cursor.execute("""
        SELECT m.name, SUM(wp.hours_worked), SUM(wp.tasks_completed)
        FROM weekly_progress wp
        JOIN members m ON wp.member_id = m.member_id
        GROUP BY m.name
    """)

    results = cursor.fetchall()
    print("Báo cáo tổng kết:")
    for row in results:
        print(f"- {row[0]}: Tổng {row[1]} giờ, {row[2]} nhiệm vụ")
    conn.close()


def cleanup_database():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("USE project_progress")
    cursor.execute("DROP TABLE IF EXISTS weekly_progress")
    print(" Đã xoá bảng weekly_progress.")
    conn.commit()
    conn.close()


def main():
    setup_database()
    add_data()
    query_progress(1)
    update_progress(1, 45.0, "Hoàn thành sớm")
    delete_progress(2)
    generate_summary()

    confirm = input("Bạn có muốn xoá bảng weekly_progress? (y/n): ")
    if confirm.lower() == 'y':
        cleanup_database()


if __name__ == "__main__":
    main()
