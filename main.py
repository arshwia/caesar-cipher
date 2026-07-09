from art_caesar_cipher import logo
from functions import check_data
from functions import encode
from functions import decode

print(logo)

while True:
    encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n\t")
    msg = str(input("Type your massage: \n\t").lower())
    shift_number = int(input("Type the shift number: \n\t"))

    def main(encode_or_decode, msg, shift_number):

        if not check_data(msg):
            return

        if encode_or_decode == "encode":
            msg_encode = encode(msg, shift_number)
            print(f"Here's the encoded result: {msg_encode}")

        elif encode_or_decode == "decode":
            msg_decode = decode(msg, shift_number)
            print(f"Here's the decoded result: {msg_decode}")

        else:
            print("Your input must be 'encode' or 'decode'")

    main(encode_or_decode, msg, shift_number)

    again = input("\nDo you want to use the program again? (Y/N): ").lower()
    if again != "y":
        print("SeeU")
        break
