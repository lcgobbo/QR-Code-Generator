import qrcode
import os

output_folder = "qrcode images"
os.makedirs(output_folder, exist_ok=True)

data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename: ').strip() 

if not filename.lower().endswith(".png"):
    filename += ".png"

filepath = os.path.join(output_folder, filename)

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filepath)

print(f'QR code saved as {filename}')