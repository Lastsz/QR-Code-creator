import qrcode

site = input("Texto: ") #Texto do QR Code. Também pode conter links.
# ESCREVA AS CORES EM INGLÊS
cor1 = input("Cor: ") #Cor padrão: black.
cor2 = input("Fundo: ") #Cor padrão: white.
tam = input("Tamanho: ") #Tamanho da imagem. (20, 21, 22...)
bor = input("Borda: ") #Tamanho da borda.

codqr = qrcode.QRCode(version=1,
                     error_correction=qrcode.constants.ERROR_CORRECT_L,
                     box_size=tam,
                     border=bor)

codqr.add_data(site)
codqr.make(fit=True)

img = codqr.make_image(fill_color=cor1, back_color=cor2)
img.save("qr.png")
print("QR Code criado!")
