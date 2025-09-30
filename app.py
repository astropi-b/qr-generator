import streamlit as st
import qrcode
from PIL import Image, ImageDraw, ImageFont
import io

# --- Title ---
st.title("🔗 Custom QR Code Generator")
st.write("Creator: **Anumanchi Agastya Sai Ram Likhit**")

# --- Input URL ---
url = st.text_input("Enter URL to encode:", "https://github.com/astropi-b/")

# --- QR Options ---
st.sidebar.header("⚙️ Customize QR Code")
box_size = st.sidebar.slider("Box Size (scale)", 5, 20, 10)
border_size = st.sidebar.slider("Border Size", 2, 10, 4)
fill_color = st.sidebar.color_picker("Foreground Color", "#000000")
back_color = st.sidebar.color_picker("Background Color", "#FFFFFF")

# --- Generate QR ---
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=box_size,
    border=border_size,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

# --- Add Creator Name ---
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
text = "Anumanchi Agastya Sai Ram Likhit"
text_width, text_height = draw.textsize(text, font=font)
canvas = Image.new("RGB", (img.size[0], img.size[1] + 40), back_color)
canvas.paste(img, (0, 0))
draw = ImageDraw.Draw(canvas)
draw.text(((canvas.size[0] - text_width) // 2, img.size[1] + 5), text, font=font, fill=fill_color)

# --- Display QR ---
st.image(canvas, caption="Generated QR Code", use_column_width=True)

# --- Download Button ---
buf = io.BytesIO()
canvas.save(buf, format="PNG")
st.download_button("📥 Download QR Code", buf.getvalue(), "qr_code.png", "image/png")
