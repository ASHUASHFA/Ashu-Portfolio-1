import streamlit as st
import time
from PIL import Image

st.markdown("<h4 style='color: #fdfdcf; font-style: italic; font-size: 12; font-weight: bold;'>Projects </h4>", unsafe_allow_html=True)
def proj_11():
    st.video("proj-img/animat-1.mp4")

def proj_12():
    st.video("proj-img/animat-2.mp4")

def proj_13():
    st.video("proj-img/animat-3.mp4")

def proj_14():
    st.video("proj-img/animat-4.mp4")

# List of functions
projects = [proj_14, proj_11, proj_12, proj_13]

# Session state for index
if "project_index" not in st.session_state:
    st.session_state.project_index = 0

# Call current project function
projects[st.session_state.project_index]()

# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Previous") and st.session_state.project_index > 0:
        st.session_state.project_index -= 1
with col2:
    if st.button("Next") and st.session_state.project_index < len(projects) - 1:
        st.session_state.project_index += 1

st.subheader(" ", divider="rainbow")


row1 = st.columns(2)
row2 = st.columns(2)
row3 = st.columns(2)
row4 = st.columns(2)
row5 = st.columns(2)
row6 = st.columns(2)
row7 = st.columns(2)

grid = [col.container(border=True) for col in row1 + row2 + row3 + row4 + row5 + row6 + row7]


def proj_1():
    time.sleep(1)
    image = Image.open("proj-img/proj-1.jpg")
    fixed_width, fixed_height = 500,500
    resized_image = image.resize((fixed_width, fixed_height))
    st.image(resized_image)

def proj_2():
    time.sleep(1)
    image = Image.open("proj-img/proj-2.jpg")
    fixed_width, fixed_height = 500,500
    resized_image = image.resize((fixed_width, fixed_height))
    st.image(resized_image)
    

def proj_3():
    time.sleep(1)
    # Load and resize the image
    image = Image.open("proj-img/proj-3.jpg")
    fixed_width, fixed_height = 500,500  # Desired width and height
    resized_image = image.resize((fixed_width, fixed_height))
    # Display the resized image
    st.image(resized_image)


def proj_4():
    time.sleep(1)
    image = Image.open("proj-img/proj-4.jpg")
    fixed_width, fixed_height = 500, 500
    resized_image = image.resize((fixed_width, fixed_height))
    st.image(resized_image)


def proj_5():
    time.sleep(1)
    image = Image.open("proj-img/proj-5.jpg")
    fixed_width, fixed_height = 500,500
    resized_image = image.resize((fixed_width, fixed_height))
    st.image(resized_image)

def proj_6():
    time.sleep(1)
    image = Image.open("proj-img/proj-6.jpg")
    fixed_width, fixed_height = 500, 500
    resized_image = image.resize((fixed_width, fixed_height))
    st.image(resized_image)

def proj_7():
    time.sleep(1)
    image = Image.open("proj-img/proj-7.jpg")
    fixed_width, fixed_height = 500,500
    resized_image = image.resize((fixed_width, fixed_height))
    st.image(resized_image)


def proj_8():
    time.sleep(1)
    image = Image.open("proj-img/proj-8.jpg")
    fixed_width, fixed_height = 500, 500
    resized_image = image.resize((fixed_width, fixed_height))
    st.image(resized_image)


def proj_9():
    time.sleep(1)
    image = Image.open("proj-img/proj-9.jpg")
    fixed_width, fixed_height = 500, 500
    resized_image = image.resize((fixed_width, fixed_height))
    st.image(resized_image)


def proj_10():
    time.sleep(1)
    image = Image.open("proj-img/proj-10.jpg")
    fixed_width, fixed_height = 500,500
    resized_image = image.resize((fixed_width, fixed_height))
    st.image(resized_image)




with grid[0]:
    proj_1()
with grid[1]:
    proj_2()
with grid[2]:
    proj_3()
with grid[3]:
    proj_4()
with grid[4]:
    proj_5()
with grid[5]:
    proj_6()
with grid[6]:
    proj_7()
with grid[7]:
    proj_8()
with grid[8]:
    proj_9()
with grid[9]:
    proj_10()

