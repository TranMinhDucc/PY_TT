def calculate_cost(course_code, quantity, promo_code):
    course_catalog = {
        "KH001": 1000000,
        "KH002": 1200000,
        "KH003": 900000,
    }

    if course_code not in course_catalog:
        raise ValueError("Mã khóa học không tồn tại trong danh sách.")

    base_price = course_catalog[course_code]
    total = base_price * quantity

    discount = 0
    if promo_code == "SUMMER25":
        discount = 0.25
    elif promo_code == "EARLYBIRD":
        discount = 0.15

    final_price = round(total * (1 - discount), 2)
    return final_price
