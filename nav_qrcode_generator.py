from PIL import Image,ImageDraw
import qrcode
data=input("Enter your name to get QRcode:-")
img=qrcode.make(data)
img.save("qr1.png")
