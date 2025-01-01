import qrcode

def link_to_qr(link, output_file):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code, higher value means bigger size
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Control the error correction used for the QR code
        box_size=10,  # Size of each box (pixel size)
        border=4  # Thickness of the border
    )

    # Add the link to the QR code
    qr.add_data(link)
    qr.make(fit=True)  # Fit the QR code according to the input data

    # Generate the image for the QR code
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a file
    img.save(output_file)

if __name__ == "__main__":
    # Example usage
    link = input("Enter the link: ")
    output_file = "qr_code.png"
    link_to_qr(link, output_file)
    print(f"QR code generated and saved as {output_file}")
