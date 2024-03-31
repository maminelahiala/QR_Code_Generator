import qrcode
insert = input("Insert your website link like this: example.com \n")
website_link = f"https://www.{insert}/"
version = int(input("Insert the version you want to use (1 - 40)"
                "this parameter controls the size of the QR Code \n"))
box_size = int(input("Insert the amount of pixels each box of the QR code is \n"))
border = int(input("Insert the border i pixels of the QR code boxes\n"))
qr = qrcode.QRCode(version = version, box_size = box_size, border = border)
qr.add_data(website_link)
qr.make()
fill_color = input("Insert the color you want in the boxes\n")
back_color = input("Insert the color you want in the background\n")
img = qr.make_image(fill_color = fill_color, back_color = back_color)
name_file = input("what you want to name the file?\n")
img.save(f'{name_file}.png')