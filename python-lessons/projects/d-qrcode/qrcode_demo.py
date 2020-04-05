# encoding: utf-8

# pip install qrcode
# pip install pillow


import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
img = qr.make_image(fill_color="black", back_color="white")
print(img)
