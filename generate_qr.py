import qrcode
from PIL import Image
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Generate a QR code.")
parser.add_argument(
    "url", type=str, help="The URL for which the QR code will be generated."
)
args = parser.parse_args()

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # QR code side
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=0,  # no border
)

# Add the URL data to the QR code
qr.add_data(args.url)
qr.make(fit=True)

# Create an image and save it
img = qr.make_image(fill_color="white", back_color="transparent")
img = img.convert("RGBA")
img.save("qr_code.png")
print("QR code generated and saved as 'qr_code.png'.")
