from art_caesar_cipher import logo
from data_caesar_cipher import valid_characters

# print(logo)
# encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n\t")
encode_or_decode = "encode"

# msg = str(input("Type your massage: \n\t").lower())
msg = "hi"
# shift_number = int(input("Type the shift number: \n\t"))
shift_number = 3


def split_msg(msg):
    """این جا پیامی که گرفته میشه رو اسپلیت میکنم و میشکنیمش"""
    msg_list = msg.split(" ")

    return msg_list


def check_data():
    """
    دیتا رو چک میکنیم

    این اصلا نیازی به فانکشن اسپلیت نداره
    """
    for letter in msg:
        is_found = False

        for valid in valid_characters:
            if valid == letter:
                is_found = True
                break

        if not is_found:
            print(f"{letter} is invalid")
            exit()


def encode():
    """این جا ما پیام رو رمز نگاری میکنیم"""
    msg_list = split_msg(msg)

    msg_encode = msg_list
    return msg_encode


def main(encode_or_decode, msg, shift_number):
    check_data()

    if encode_or_decode == "encode":
        # هنوز ما خود انکود کردن رو شروع نکردیم
        msg_encode = encode()

        print(f"Here's the encoded result: {msg_encode}")

    elif encode_or_decode == "decode":
        print("decode")

    else:
        print("your input not 'encode' or 'decode'")


main(encode_or_decode, msg, shift_number)
