import streamlit as st
from PIL import Image
import time
import base64
from pathlib import Path

# === Config ===
IMAGE_FOLDER = Path("collob-img")
IMAGE_DATA = [
    {"file": "meesho-img.jpg", "label": "Meesho"},
    {"file": "swizz-img.jpg", "label": "Swizz Codes"},
    {"file": "college-img.jpg", "label": "C. Abdul Hakeem College of Engineering and Technology"},
]
IMAGE_WIDTH = 300
ANIMATION_DURATION = 1.5  # seconds
AUTO_SLIDE_INTERVAL = 3   # seconds

# === Helper Functions ===
def load_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def render_fade_zoom(img_b64, label):
    return f"""
    <div style="
        display: flex;
        flex-direction: column;
        align-items: center;
        animation: fadeZoom {ANIMATION_DURATION}s ease-in-out;
    ">
        <img src="data:image/png;base64,{img_b64}"  style="border-radius:12px;">
        <div style="font-size: 20px; margin-top: 10px;">{label}</div>
    </div>
    <style>
        @keyframes fadeZoom {{
            0% {{ opacity: 0; transform: scale(0.8); }}
            100% {{ opacity: 1; transform: scale(1); }}
        }}
    </style>
    """

# === Session State ===
if "index" not in st.session_state:
    st.session_state.index = 0
if "img_b64_list" not in st.session_state:
    st.session_state.img_b64_list = [
        load_image_base64(IMAGE_FOLDER / item["file"]) for item in IMAGE_DATA
    ]

st.subheader("🧾 My Colloboration")
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.write(" ")

col1, col2 = st.columns(2, gap = "small", vertical_alignment = "center")

with col1:
    image = Image.open("collob-img/meesho-img.jpg")
    fixed_width, fixed_height = 300, 250
    resized_image = image.resize((fixed_width, fixed_height))
    st.image(resized_image)
with col2:
    st.subheader("Meesho", divider = "rainbow")
    st.write("Collaborated with Meesho on a creative project, producing original artwork for their [campaign/product/brand visuals]. Contributed to design concepts that aligned with their brand identity and marketplace audience.")


col3, col4 = st.columns(2, gap = "small", vertical_alignment = "center")

with col3:
    image1 = Image.open("collob-img/swizz-img.jpg")
    fixed_width, fixed_height = 300, 250
    resized_image1 = image1.resize((fixed_width, fixed_height))
    st.image(resized_image1)

with col4:
    st.subheader("SWIZZ CODES", divider = "rainbow")
    st.write("I worked with the marketing team of SWIZZ CODES contributing to promotional and branding initiatives")


col5, col6 = st.columns(2, gap = "small", vertical_alignment = "center")

with col5:
    image1 = Image.open("collob-img/college-img.jpg")
    fixed_width, fixed_height = 300, 250
    resized_image1 = image1.resize((fixed_width, fixed_height))
    st.image(resized_image1)

with col6:
    st.subheader("C. Abdul Hakeem College of Engineering and Technology", divider = "rainbow")
    st.write("I am a student and editor of my college which is grateful to build a designing works for my college")

st.write(" ")

with st.container(border=True):
    # === Show Slide ===
    current = st.session_state.index
    img_b64 = st.session_state.img_b64_list[current]
    label = IMAGE_DATA[current]["label"]
    slide = st.empty()
    slide.markdown(render_fade_zoom(img_b64, label), unsafe_allow_html=True)

    # === Auto Loop ===
    time.sleep(AUTO_SLIDE_INTERVAL)
    st.session_state.index = (st.session_state.index + 1) % len(IMAGE_DATA)
    st.rerun()