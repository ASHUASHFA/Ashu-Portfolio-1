import streamlit as st
from PIL import Image

col1, col2 = st.columns(2, gap = "small", vertical_alignment = "center")

with col1:
    image = Image.open("cert_img/cert-1.jpg")
    fixed_width, fixed_height = 300, 250
    resized_image = image.resize((fixed_width, fixed_height))
    st.image(resized_image, caption="Issued by Great Learning, on August 2024")
with col2:
    st.subheader("Into to Graphic Design with Photoshop", divider = "rainbow")
    st.write("I have learned a basic level of desining with Adobe Photoshop in effective manner")


col3, col4 = st.columns(2, gap = "small", vertical_alignment = "center")

with col3:
    image1 = Image.open("cert_img/cert-2.jpg")
    fixed_width, fixed_height = 300, 250
    resized_image1 = image1.resize((fixed_width, fixed_height))
    st.image(resized_image1, caption = "Issued by Great Learning, on August 2024")

with col4:
    st.subheader("Java Programming", divider = "rainbow")
    st.write("This course helps me to build a java application which handles classes and objects in systematic order")


col5, col6 = st.columns(2, gap = "small", vertical_alignment = "center")

with col5:
    image1 = Image.open("cert_img/cert-3.jpg")
    fixed_width, fixed_height = 300, 250
    resized_image1 = image1.resize((fixed_width, fixed_height))
    st.image(resized_image1, caption = "Issued by Simpli Learn, on June 2025")

with col6:
    st.subheader("Introduction to Cyber Security", divider = "rainbow")
    st.write("In this course, I had learned about Cyber Security where to protect from unauthorized access and adapt program securely")