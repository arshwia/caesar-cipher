from data_caesar_cipher import valid_characters


def check_data(msg):
    """بررسی می‌کند که همه کاراکترهای پیام معتبر باشند."""

    for letter in msg:
        is_found = False

        for valid in valid_characters:
            if valid == letter:
                is_found = True
                break

        if not is_found:
            print(f"{letter} is invalid")
            return False

    return True


def encode(msg, shift_number):
    """اینجا بعداً الگوریتم رمزنگاری را کامل می‌کنیم."""

    encoded = ""

    for letter in msg:
        if letter == " ":
            encoded += " "
            continue

        for index, char in enumerate(valid_characters):
            if letter == char:
                new_index = (index + shift_number) % 26
                encoded += valid_characters[new_index]

    return encoded


def decode(msg, shift_number):
    decoded = ""

    for letter in msg:
        if letter == " ":
            decoded += " "
            continue

        for index, char in enumerate(valid_characters):
            if letter == char:
                new_index = (index - shift_number) % 26
                decoded += valid_characters[new_index]
                break

    return decoded
