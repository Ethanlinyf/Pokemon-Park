"""
This is a Python program to create a QR code.
"""


import qrcode


def create_a_QR_code(message):
    image_pok = qrcode.make(message)
    image_pok.show()
    # image_pok.save(name)


def main():
    create_a_QR_code("Https://thethingsengine.org")


if __name__ == "__main__":
    main()
