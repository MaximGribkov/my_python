import qrcode

link = input('Enter info')
img = qrcode.make("{}".format(link))
img.save("qr_cod.png")
