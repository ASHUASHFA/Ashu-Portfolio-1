import streamlit as st
import smtplib
from email.mime.text import MIMEText
import time
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Use circular version if available
image_base64 = get_base64_image("ashu-logo.jpg")  # Replace with 'sezo-logo-circle.png' if you have it

css_html = f"""
<style>

/* Background pulse */
@keyframes background-pulse {{
  0% {{ background-color: #001f3f; }}
  50% {{ background-color: #003366; }}
  100% {{ background-color: #001f3f; }}
}}

body {{
  animation: background-pulse 7s ease-in-out infinite;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}}

/* Main container */
.container {{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}}

/* Wrapper */
.logo-wrapper {{
  position: relative;
  width: 260px;
  height: 260px;
  margin: 60px auto;
}}



/* Main logo image */
.logo-img {{
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: contain;
  z-index: 1;
  border-radius: 50%;
  animation: 
    logo-enter 1.2s cubic-bezier(0.2, 0.8, 0.3, 1.2) forwards,
    subtle-float 6s ease-in-out infinite;
  filter: drop-shadow(0 0 10px rgba(0, 192, 255, 0.3));
}}

@keyframes logo-enter {{
  0% {{ transform: scale(0.5) rotate(-15deg); opacity: 0; }}
  80% {{ transform: scale(1.05) rotate(5deg); }}
  100% {{ transform: scale(1) rotate(0deg); opacity: 1; }}
}}

@keyframes subtle-float {{
  0%, 100% {{ transform: translateY(0); }}
  50% {{ transform: translateY(-10px); }}
}}


/* Outer ring animation */
.outer-ring {{
  position: absolute;
  width: 110%;
  height: 110%;
  top: -5%;
  left: -5%;
  border-radius: 50%;
  border: 2px solid rgba(0, 192, 255, 0.3);
  animation: ring-pulse 4s ease-out infinite;
  z-index: 0;
}}

@keyframes ring-pulse {{
  0% {{ transform: scale(1); opacity: 0.7; }}
  70% {{ transform: scale(1.1); opacity: 0; }}
  100% {{ transform: scale(1); opacity: 0; }}
}}

</style>

<div class="logo-wrapper">
  <div class="outer-ring"></div>
  <div class="rotating-arc"></div>
  <img class="logo-img" src="data:image/png;base64,{image_base64}" alt="ashu Logo" />
</div>
"""

# Hero section
col1, col2 = st.columns(2, gap = "small", vertical_alignment = "center")
with col1:
    # Render the HTML and CSS
    st.markdown(css_html, unsafe_allow_html=True)
with col2:
    st.title("Ashfaq Ahmed.M", anchor = False)
    st.markdown("<div class='custom-write1'>Graphic Designer with a creative approach to visual storytelling. My work mainly focuses on branding, promotions, and collaboration projects, where I aim to bring fresh and impactful designs to life.</div>",
    unsafe_allow_html=True)
    st.write(" ")
        

# Experience & Qualifications
st.write("\n")
st.subheader("About", anchor = False, divider = "rainbow")
st.write(
    """
    -   I’m Ashfaq Ahmed.M, currently pursuing B.E. in Computer Science and Engineering
    -   I’m always open to new collaborations and opportunities that challenge my skills and help me grow as a designer
    -   I’m also associated with "The Poster Mart", a platform that allows me to showcase my creativity and connect with like-minded individuals.
    """
)

# Skills
st.write("\n")
st.subheader("Hard Skills", anchor = False, divider = "rainbow")
st.write(
    """
    - 🎨 Adobe Photoshop 
    - ✒️ Vector Illustration (Illustrator) 
    - 🖥️ UI/UX Design (Figma, XD) 
    - 📐 Print Design (ibisPaint X) 
    - 🎞️ Motion Graphics 
    """
)

# Sites
st.write("\n")
st.subheader("Websites", anchor = False, divider = "rainbow")
col3, col4, col5, col6 = st.columns(4, gap = "small", vertical_alignment = "center")
with col3:
    st.link_button("GitHub Link", 'https://github.com/ASHUASHFA')
with col4:
    st.link_button("LinkedIn Link", 'https://www.linkedin.com/in/ashfaq-ahmed-m-b3a49a2a5')
with col5:
    st.link_button("Instagram Link", 'https://www.instagram.com/ax_faq_?igsh=OWhqZDMzY3JmNGc=')
with col6:
    st.link_button("Figma Link", 'https://www.figma.com/make/duF5T5vjyBsg2Dq38DkkK6/Portfolio-Website-for-Ashfaq-Ahmed?node-id=0-1&p=f')
