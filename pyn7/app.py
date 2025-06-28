import pandas as pd
import matplotlib.pyplot as plt
import os


def create_initial_data():
    data = [
        ['An', 1, 5, 8.5],
        ['Bình', 1, 4, 7.0],
        ['Cường', 1, 6, 9.0],
        ['Dương', 1, 3, 6.0],
        ['Hoa', 1, 5, 8.0],
        ['An', 2, 6, 9.0],
        ['Bình', 2, 5, 8.0],
        ['Cường', 2, 6, 9.5],
        ['Dương', 2, 4, 7.0],
        ['Hoa', 2, 6, 9.0],
        ['An', 3, 7, 9.5],
        ['Bình', 3, 5, 8.0],
        ['Cường', 3, 6, 9.5],
        ['Dương', 3, 5, 7.5],
        ['Hoa', 3, 7, 9.5],
    ]

    df = pd.DataFrame(data, columns=['Tên', 'Tuần', 'Bài tập', 'Điểm'])
    df.to_csv('progress.csv', index=False)  # Lưu vào file CSV
    print(" Dữ liệu đã được tạo và lưu vào progress.csv")


def analyze_weekly_progress(week):
    if not os.path.exists('progress.csv'):
        print("Tập tin progress.csv không tồn tại.")
        return

    df = pd.read_csv('progress.csv')

    df_week = df[df['Tuần'] == week]

    if df_week.empty:
        print(f"Không có dữ liệu cho tuần {week}")
        return

    avg_exercises = df_week['Bài tập'].mean()
    avg_score = df_week['Điểm'].mean()
    top_student = df_week[df_week['Điểm'] == df_week['Điểm'].max()].iloc[0]

    print(f"\n Phân tích tuần {week}:")
    print(f"- Bài tập trung bình: {avg_exercises:.2f}")
    print(f"- Điểm trung bình: {avg_score:.2f}")
    print(f"- Học viên xuất sắc: {top_student['Tên']} ({top_student['Điểm']})")

    print("\n Học viên làm trên 4 bài tập:")
    print(df_week[df_week['Bài tập'] > 4])


def visualize_progress():
    df = pd.read_csv('progress.csv')

    plt.figure()
    for name in df['Tên'].unique():
        student_data = df[df['Tên'] == name]
        plt.plot(student_data['Tuần'],
                 student_data['Điểm'], marker='o', label=name)

    plt.title("Xu hướng điểm trung bình qua các tuần")
    plt.xlabel("Tuần")
    plt.ylabel("Điểm")
    plt.legend()
    plt.savefig("trend.png")
    plt.close()

    plt.figure()
    weekly_avg = df.groupby('Tuần')['Bài tập'].mean()
    weekly_avg.plot(kind='bar')
    plt.title("Số bài tập trung bình theo tuần")
    plt.xlabel("Tuần")
    plt.ylabel("Số bài tập")
    plt.savefig("comparison.png")
    plt.close()

    print(" Đã lưu biểu đồ trend.png và comparison.png")


def generate_weekly_report():
    df = pd.read_csv('progress.csv')

    total_exercises = df.groupby('Tên')['Bài tập'].sum()
    avg_scores = df.groupby('Tên')['Điểm'].mean()

    week1 = df[df['Tuần'] == 1].set_index('Tên')['Điểm']
    week3 = df[df['Tuần'] == 3].set_index('Tên')['Điểm']
    progress = (week3 - week1).dropna()
    most_improved = progress.idxmax()
    improvement_value = progress.max()

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(" Báo cáo tổng kết:\n")
        for name in total_exercises.index:
            f.write(f"- Tổng bài tập của {name}: {total_exercises[name]}\n")
            f.write(f"- Điểm trung bình của {name}: {avg_scores[name]:.2f}\n")
        f.write(
            f"- Học viên tiến bộ nhất: {most_improved} (tăng {improvement_value:.2f} điểm)\n")

    # Vẽ biểu đồ tròn
    plt.figure()
    total_exercises.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Tỷ lệ đóng góp bài tập của học viên")
    plt.ylabel("")
    plt.savefig("contribution.png")
    plt.close()

    print(" Đã lưu report.txt và contribution.png")


def main():
    create_initial_data()
    analyze_weekly_progress(2)
    visualize_progress()
    generate_weekly_report()


if __name__ == "__main__":
    main()
