import streamlit as st
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="Custom QR Code", page_icon="🔗")

# --- Title ---
st.title("🔗 Custom QR Code Generator")

st.markdown("""
**Creator:** Anumanchi Agastya Sai Ram Likhit  
**GitHub:** [https://github.com/astropi-b/](https://github.com/astropi-b/)
""")

# --- Input URL ---
url = st.text_input("Enter URL to encode:", "https://github.com/astropi-b/")

# --- QR Options ---
st.sidebar.header("⚙️ Customize QR Code")
box_size = st.sidebar.slider("Box Size (scale)", 5, 20, 10)
border_size = st.sidebar.slider("Border Size", 0, 10, 4)
fill_color = st.sidebar.color_picker("Foreground Color", "#000000")
back_color = st.sidebar.color_picker("Background Color", "#FFFFFF")

# --- Generate QR ---
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=box_size,
    border=border_size,
)
qr.add_data(url.strip())
qr.make(fit=True)
img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

# --- Display (use_container_width) ---
st.image(img, caption=f"QR for: {url}", use_container_width=True)

# --- Download Button ---
buf = io.BytesIO()
img.save(buf, format="PNG")
st.download_button("📥 Download QR Code", buf.getvalue(), "qr_code.png", "image/png")
