from flask import Flask, request, send_file, jsonify
import io
import qrcode

app = Flask(__name__)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json
    link = data.get('link')
    if not link:
        return jsonify({"error": "No link provided"}), 400

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    # Save to an in-memory file
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
