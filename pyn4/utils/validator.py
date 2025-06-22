import re


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_course_code(course_code):
    pattern = r'^KH\d{3}$'
    return re.match(pattern, course_code) is not None


def validate_name(name):
    if len(name.strip()) < 2:
        raise ValueError("Tên quá ngắn. Vui lòng nhập lại.")
    return True
