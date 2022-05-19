#Documentation -> https://pypi.org/project/qrcode/
import qrcode
from qrcode.image.svg import SvgPathImage

'''
#Wifi URI template
wifiName = "****"
authType = "WPA"   #WEP/WPA/-blank-
wifiPass = "****"  #Ignore if T is -blank-
isHidden = "false" #true/false
data = f"WIFI:S:{wifiName};T:{authType};P:{wifiPass};H:{isHidden};;"
'''
data = "https://www.google.com/"

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L, #readability under ware
    box_size=10, #outputSize
    version=1,   #QR code cube complexity
    border=1,    #Border from image end
)
QRcode.add_data(data)
QRcode.make(fit=True)


QRimg = QRcode.make_image(fill_color=(0, 0, 0), back_color=(255, 255, 255)).convert("RGB")
QRimg.save("QR.png")

QRsvg = QRcode.make_image(image_factory=SvgPathImage)
QRsvg.save("QR.svg")

#Todo -> https://adambrianbright.github.io/qrcode_styled/