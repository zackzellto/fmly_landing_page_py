from datetime import datetime


def get_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


EMAIL = {
    "Email": "zackzelltodev@gmail.com",
    "timestamp": get_timestamp(),
}


def get_email():
    return list(EMAIL.values())
