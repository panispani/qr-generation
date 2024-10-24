import qrcode
from PIL import Image
import argparse
import os
from qrcode.image.svg import SvgPathImage
from xml.dom import minidom


FILL_COLOR = "white"  # 'black'
BACK_COLOR = "transparent"  # 'white'


def get_available_filename(base_name, extension):
    """
    If a file exists, increment a counter like 'file(1).ext'.
    """
    counter = 1
    file_name = f"{base_name}.{extension}"
    while os.path.exists(file_name):
        file_name = f"{base_name}({counter}).{extension}"
        counter += 1
    return file_name


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a QR code in PNG or SVG format."
    )
    parser.add_argument(
        "url", type=str, help="The URL for which the QR code will be generated."
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["png", "svg"],
        default="png",
        help="Output format: png or svg (default: png)",
    )
    args = parser.parse_args()

    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # size of QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,  # no border
    )

    # Add the URL data to the QR code
    qr.add_data(args.url)
    qr.make(fit=True)

    # Generate and save image
    if args.format == "png":
        img = qr.make_image(fill_color=FILL_COLOR, back_color=BACK_COLOR).convert(
            "RGBA"
        )
        filename = get_available_filename("qr_code", "png")
        img.save(filename)
        print(f"QR code saved as {filename}.")
    elif args.format == "svg":
        filename = get_available_filename("qr_code", "svg")
        qr_svg = qr.make_image(image_factory=SvgPathImage)

        if FILL_COLOR == "black":
            with open(filename, "wb") as f:
                qr_svg.save(f)
        else:  # Only 'white' for now
            # Parse the SVG content and update the fill color of paths to white
            svg_content = qr_svg.to_string()
            svg_doc = minidom.parseString(svg_content)
            paths = svg_doc.getElementsByTagName("path")
            for path in paths:
                path.setAttribute(
                    "fill", "#FFFFFF"
                )  # TODO: create a map from colors to HEX or use a ready one

            # Remove the background rect to make it transparent
            rects = svg_doc.getElementsByTagName("rect")
            for rect in rects:
                rect.parentNode.removeChild(rect)

            with open(filename, "w") as f:
                svg_doc.writexml(f)

        print(f"QR code saved as {filename}.")
