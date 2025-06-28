import numpy as np
from scipy import stats, optimize
import os


def create_and_save_data(filename="performance.npy"):
    np.random.seed(42)
    hours = np.random.uniform(30, 45, (4, 5))
    tasks = np.random.randint(3, 8, (4, 5))
    data = np.stack((hours, tasks), axis=2)
    np.save(filename, data)
    return filename


def basic_analysis(filename="performance.npy"):
    if not os.path.exists(filename):
        print(" File dữ liệu không tồn tại.")
        return

    data = np.load(filename)
    for week_idx, week in enumerate(data):
        avg_hours = np.mean(week[:, 0])
        std_hours = np.std(week[:, 0])
        total_tasks = np.sum(week[:, 1])
        best_member_idx = np.argmax(week[:, 1])
        best_member_tasks = week[best_member_idx, 1]

        print(f"Phân tích tuần {week_idx + 1}:")
        print(f"- Trung bình giờ làm: {avg_hours:.2f}")
        print(f"- Độ lệch chuẩn giờ: {std_hours:.2f}")
        print(f"- Tổng nhiệm vụ: {int(total_tasks)}")
        print(
            f"- Thành viên xuất sắc: Thành viên {best_member_idx + 1} ({int(best_member_tasks)} nhiệm vụ)\n")


def advanced_analysis(filename="performance.npy"):
    if not os.path.exists(filename):
        print(" File dữ liệu không tồn tại.")
        return

    data = np.load(filename)
    hours_all = data[:, :, 0].flatten()
    tasks_all = data[:, :, 1].flatten()

    slope, intercept, r_value, _, _ = stats.linregress(hours_all, tasks_all)
    corr, _ = stats.pearsonr(hours_all, tasks_all)

    mean_hours = np.mean(hours_all)
    std_hours = np.std(hours_all)
    outliers = hours_all[(hours_all < mean_hours - 2 * std_hours)
                         | (hours_all > mean_hours + 2 * std_hours)]

    print("Hồi quy tuyến tính:")
    print(f"- Độ dốc: {slope:.4f}")
    print(f"- Hệ số tương quan: {corr:.4f}")
    print(f"- Giá trị ngoại lai (giờ làm): {outliers}\n")

    return slope, intercept


def optimize_workload(slope, intercept, n_members=5):
    def objective(x):
        return -np.sum(slope * x + intercept)

    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 200})
    bounds = [(30, None)] * n_members  # Tối thiểu 30 giờ mỗi người
    init_guess = np.full(n_members, 40.0)

    result = optimize.minimize(
        objective, init_guess, bounds=bounds, constraints=constraints)

    if result.success:
        hours = result.x
        print("Phân bổ giờ làm tuần tới:")
        for i, h in enumerate(hours):
            print(f"- Thành viên {i + 1}: {h:.2f} giờ")
    else:
        print(" Tối ưu hóa thất bại.")


def main():
    filename = create_and_save_data()
    basic_analysis(filename)
    slope, intercept = advanced_analysis(filename)
    optimize_workload(slope, intercept)


if __name__ == "__main__":
    main()
